"""Simple Database application with Flask and Python by Mahi Mahatab"""
"""This is my final result for this assessment based on GUI"""

# Imports
from flask import Flask, render_template, request, redirect
import sqlite3

# Initializing App and Database Path
app = Flask(__name__)
DATABASE = r'SQL\Rich People\Data\rich_people.db'

# Database connection
def connect_db():
    return sqlite3.connect(DATABASE)

# Filtering and sorting based on user input
def filtering(sort_by=None, country=None, gender=None):
    db = connect_db()
    cursor = db.cursor()
    
    # Base SQL query
    query = 'SELECT person_id, rank, name, age, country, city, gender, net_worth_billion FROM People'
    choice = []# To store filter conditions
    user_input = []# To store actual values for filter conditions

    # Checks if the user typed a country name for the filter
    if country:
        choice.append("country = ?")
        user_input.append(country)# Adds the input country to user_input list

    # Checks if the user selected a gender from dropdown and adds it to the filter
    if gender:
        choice.append("gender = ?")
        user_input.append(gender)# Adds the selected gender to user_input list

    # If the user used any filter, add WHERE to base query
    if choice:
        query += " WHERE " + " AND ".join(choice)

    # Checks if the user selected any sorting option and adds ORDER BY that user selecetion
    if sort_by in ["rank", "name", "age", "country", "city", "gender", "net_worth_billion"]:
        query += f" ORDER BY {sort_by} ASC"

    # Execute the final query with the user inputs
    cursor.execute(query, user_input)
    peoples = cursor.fetchall()# Store the results in a variable
    db.close()
    return peoples# Return the filtered/sorted people list

# Get summary information about one person
def get_summary(person_id):
    db = connect_db()
    cursor = db.cursor()

    # SQL query that joins People and Summary table based on person_id
    cursor.execute('''
        SELECT People.name, Summary.organization_name, Summary.position_in_organization, Summary.self_made
        FROM People
        LEFT JOIN Summary ON People.person_id = Summary.person_id
        WHERE People.person_id = ?;
    ''', (person_id,))

    summary = cursor.fetchone()# Get the summary info
    db.close()
    return summary# Return the summary info

# Main homepage route
@app.route('/')
def homepage():
    # Get values from URL parameters (sort, country, gender)
    sort_by = request.args.get('sort')
    country = request.args.get('country')
    gender = request.args.get('gender')

    # Get people based on filters and sorting
    peoples = filtering(sort_by, country, gender)

    # If there are no results show a message card
    if not peoples:
        return render_template('no_results.html', country=country)

    # Load the index page with the result data and filters
    return render_template('index.html', peoples=peoples, sort_by=sort_by, country=country, gender=gender)

# Route for summary about one person
@app.route('/summary/<int:person_id>')
def person_summary(person_id):
    summary = get_summary(person_id)

    # If no summary was found for the person_id then return message for the user
    if not summary:
        return "Person not found"
    
    # Takes the values from summary and checls origin if self-made or not
    name, organization, position, self_made = summary
    origin = "Self-Made" if self_made == 1 else ("Inherited" if self_made == 0 else "[N/A]")

    # Load the summary card template with person details
    return render_template('summary.html', name=name, organization=organization, position=position, origin=origin)

# Runs the server
if __name__ == '__main__':
    app.run(debug=True)
