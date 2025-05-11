# Google Sheets: https://docs.google.com/spreadsheets/d/1hmNyJQ3KSWIeKQd7KvyhWjI4bkDVh51wTk656Hi9tdw/edit?usp=sharing

"""
Rich People Database Application by Mahi Mahatab - 2025
"""
#Imports
import sqlite3

# Constants and Variables
DATABASE = r'C:\PersonalUse\School\Computer Science\SQL\Rich People\rich_people.db'

# Working Functions
def connect_db():
    return sqlite3.connect(DATABASE)

def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Functions

#View Everything
def view_all_people():
    db = connect_db()
    cursor = db.cursor()
    
    cursor.execute('SELECT * FROM People;')
    people = cursor.fetchall()

    print_header("All Billionaires")

    for person in people:
        print(f"{person[0]:>3}) {person[1]}, Age: {person[3]}, Country: {person[5]}, City: {person[6]}, Net Worth: ${person[8]}B")
    
    db.close()

# Main Sorting Function
def sort_by(attribute):
    db = connect_db()
    cursor = db.cursor()
    sql = f'SELECT name, age, country, city, rank, net_worth_billion FROM People ORDER BY {attribute} DESC;'

    cursor.execute(sql)
    results = cursor.fetchall()

    print_header(f"Sorted by {attribute.replace('_', ' ').title()}")
    for result in results:
        print(f"{result[0]} | Age: {result[1]} | {result[2]}, {result[3]} | Rank: {result[4]} | Net Worth: ${result[5]}B")
    
    db.close()

# Filter by location with input
def filter_by_location():
    country = input("Enter a country: ").strip()
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('SELECT name, city, net_worth_billion FROM People WHERE country = ? COLLATE NOCASE;', (country,))
    results = cursor.fetchall()

    print_header(f"Billionaires in {country}")

    if results:
        for result in results:
            print(f"{result[0]} from {result[1]} | Net Worth: ${result[2]}B")
    else:
        print("No data found.")
    
    db.close()

# Summary
def view_summary():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('''
        SELECT People.name, Summary.organization_name, Summary.position_in_organization, Summary.self_made
        FROM People JOIN Summary ON People.person_id = Summary.person_id;
    ''')
    results = cursor.fetchall()

    print_header("Organization Information")

    for result in results:
        print(f"{result[0]} | {result[1]} - {result[2]} | {'Self-Made' if str(result[3]).lower() == 'true' else 'Inherited'}")
    
    db.close()

# View Wealth Source
def view_wealth_sources():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('''
        SELECT People.name, WealthSource.business_industries
        FROM People JOIN WealthSource ON People.person_id = WealthSource.person_id;
    ''')
    results = cursor.fetchall()

    print_header("Wealth Sources")

    for result in results:
        print(f"{result[0]} | Industry: {result[1]}")
    
    db.close()

# Main
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1) View all billionaires")
        print("2) Sort by age")
        print("3) Sort by rank")
        print("4) Sort by net worth")
        print("5) Filter by country")
        print("6) View organization info")
        print("7) View wealth sources")
        print("8) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_all_people()
        elif choice == '2':
            sort_by("age")
        elif choice == '3':
            sort_by("rank")
        elif choice == '4':
            sort_by("net_worth_billion")
        elif choice == '5':
            filter_by_location()
        elif choice == '6':
            view_summary()
        elif choice == '7':
            view_wealth_sources()
        elif choice == '8':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run
if __name__ == '__main__':
    main()
