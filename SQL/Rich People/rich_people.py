"""Database about Rich People by Mahi Mahatab, May 2025"""
"""This is a simple CLI based program!!!"""

#Imports
import sqlite3

# Constants and Variables
DATABASE = r'C:\PersonalUse\School\Computer Science\SQL\Rich People\Data\rich_people.db'

# Work Functions

# Connecting Database
def connect_db():
    return sqlite3.connect(DATABASE)

# Header
def print_header(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")

# Allign with gaps and print out N/A if needed
def gap(value, width):
    if value is None:
        return "[N/A]".ljust(width)
    if isinstance(value, float):
        if value.is_integer():
            return f"{int(value)}B".ljust(width)
        else:
            return f"{value:.1f}B".ljust(width)
    return str(value).ljust(width)

# Functions

# View all billionaires
def view_all_people():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM People;')
    people = cursor.fetchall()

    print_header("All Billionaires")
    print(f"{'ID':<3} {'Name':<25} {'Age':<5} {'Country':<15} {'City':<15} {'Net Worth ($B)':<15}")
    print("-" * 85)

    for person in people:
        print(f"{person[0]:<3} {gap(person[1], 25):<25} {gap(person[3], 5):<5} {gap(person[5], 15):<15} {gap(person[6], 15):<15} ${gap(person[8], 10):<}")

    db.close()

# Main Soritng
def sort_by(attribute):
    db = connect_db()
    cursor = db.cursor()
    sql = f'SELECT name, age, country, city, rank, net_worth_billion FROM People ORDER BY {attribute} DESC;'
    cursor.execute(sql)
    results = cursor.fetchall()

    print_header(f"Sorted by {attribute.replace('_', ' ').title()}")
    print(f"{'Name':<25} {'Age':<5} {'Country':<15} {'City':<15} {'Rank':<6} {'Net Worth ($B)':<15}")
    print("-" * 95)

    for result in results:
        print(f"{gap(result[0], 25):<25} {gap(result[1], 5):<5} {gap(result[2], 15):<15} {gap(result[3], 15):<15} {gap(result[4], 6):<6} ${gap(result[5], 10):<}")

    db.close()

# Filter by country with input
def filter_by_location():
    country = input("Enter a country: ").strip()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT name, city, net_worth_billion FROM People WHERE country = ? COLLATE NOCASE;', (country,))
    results = cursor.fetchall()

    print_header(f"Billionaires in {country}")
    print(f"{'Name':<25} {'City':<20} {'Net Worth ($B)':<15}")
    print("-" * 65)

    if results:
        for result in results:
            print(f"{gap(result[0], 25):<25} {gap(result[1], 20):<20} ${gap(result[2], 10):<}")
    else:
        print("No data found.")

    db.close()

# Filter by gender with input
def filter_by_gender():
    gender = input("Enter a gender (Male / Female): ").strip()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT name, gender, net_worth_billion FROM People WHERE gender = ? COLLATE NOCASE;', (gender,))
    results = cursor.fetchall()

    print_header(f"{gender} Billionaires")
    print(f"{'Name':<25} {'Gender':<20} {'Net Worth ($B)':<15}")
    print("-" * 65)

    if results:
        for result in results:
            print(f"{gap(result[0], 25):<25} {gap(result[1], 20):<20} ${gap(result[2], 10):<}")
    else:
        print("No data found.")

    db.close()

# View organization and position
def view_summary():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT People.name, Summary.organization_name, Summary.position_in_organization, Summary.self_made
        FROM People LEFT JOIN Summary ON People.person_id = Summary.person_id;
    ''')
    results = cursor.fetchall()

    print_header("Organization Information")
    print(f"{'Name':<25} {'Organization':<30} {'Position':<25} {'Origin':<10}")
    print("-" * 95)

    for result in results:
        name = gap(result[0], 25)
        organization = gap(result[1] if result[1] else None, 30)
        position = gap(result[2] if result[2] else None, 25)

        if not result[3] in (0, 1):
            origin = "[N/A]"
        else:
            origin = "Self-Made" if result[3] == 1 else "Inherited"

        print(f"{name}{organization}{position}{gap(origin, 10)}")

    db.close()

# View business industries
def view_wealth_sources():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT People.name, WealthSource.business_industries
        FROM People JOIN WealthSource ON People.person_id = WealthSource.person_id;
    ''')
    results = cursor.fetchall()

    print_header("Wealth Sources")
    print(f"{'Name':<25} {'Industry':<40}")
    print("-" * 70)

    for result in results:
        print(f"{gap(result[0], 25):<25} {gap(result[1], 40):<40}")

    db.close()

# Main function
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
        print("9) Filter by gender")

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
        elif choice == '9':
            filter_by_gender()
        else:
            print("Invalid option. Please try again.")

# Run
if __name__ == '__main__':
    main()
