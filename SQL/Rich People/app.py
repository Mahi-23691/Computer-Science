from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = r'C:\PersonalUse\School\Computer Science\SQL\Rich People\Data\rich_people.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def filtering(sort_by=None, country=None, gender=None):
    db = connect_db()
    cursor = db.cursor()

    query = 'SELECT person_id, rank, name, age, country, city, gender, net_worth_billion FROM People'
    choice = []
    user_input = []

    if country:
        choice.append("country = ?")
        user_input.append(country)

    if gender:
        choice.append("gender = ?")
        user_input.append(gender)

    if choice:
        query += " WHERE " + " AND ".join(choice)

    if sort_by in ["rank", "name", "age", "country", "city", "gender", "net_worth_billion"]:
        query += f" ORDER BY {sort_by} ASC"

    cursor.execute(query, user_input)
    peoples = cursor.fetchall()
    db.close()
    return peoples

def get_summary(person_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT People.name, Summary.organization_name, Summary.position_in_organization, Summary.self_made
        FROM People
        LEFT JOIN Summary ON People.person_id = Summary.person_id
        WHERE People.person_id = ?;
    ''', (person_id,))

    summary = cursor.fetchone()
    db.close()
    return summary

@app.route('/')
def homepage():
    sort_by = request.args.get('sort')
    country = request.args.get('country')
    gender = request.args.get('gender')

    peoples = filtering(sort_by, country, gender)

    return render_template('index.html', peoples=peoples, sort_by=sort_by, country=country, gender=gender)

@app.route('/summary/<int:person_id>')
def person_summary(person_id):
    summary = get_summary(person_id)

    if not summary:
        return "Person not found"
    
    name, organization, position, self_made = summary
    origin = "Self-Made" if self_made == 1 else ("Inherited" if self_made == 0 else "[N/A]")

    return render_template('summary.html', name=name, organization=organization, position=position, origin=origin)

if __name__ == '__main__':
    app.run(debug=True)
