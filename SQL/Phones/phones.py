"""
Phones database application by -Mahi Mahatab on 2nd May 2025
"""

#imports
import sqlite3

#CONSTANTS || Variables
DATABASE = 'SQL\Phones\phones.db'

#Functions

#printing all the phones properly
def print_all_phones():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"Phone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()

#prints the data sorted by release date of the phones in a descending order
def by_release_date():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones ORDER BY release_date DESC;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"\n\nPhone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()
    
#prints the data sorted by release date of the phones in a descending order
def by_release_date():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones ORDER BY release_date DESC;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"\n\nPhone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()

#prints the data sorted by screen size of the phones in a descending order
def by_screen_size():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones ORDER BY screen_size DESC;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"\n\nPhone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()

#prints the data sorted by battery capacity of the phones in a descending order
def by_battery_capacity():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones ORDER BY battery_capacity DESC;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"\n\nPhone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()

#prints the data sorted by price of the phones in a descending order
def by_price():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM phones ORDER BY price_usd DESC;'
    cursor.execute(sql)

    results = cursor.fetchall()

    #looping through the results
    print(f"\n\nPhone Name{" " * 9} Release Date   Operating System    Screen Size   Battery   Price\n{"_"*87}")
    for phone in results:
        print(f"{phone[1]:<20}{phone[3]:<15}{phone[4]:<20}{phone[5]:<14}{phone[6]:<10}{phone[7]:<10}")

    #exit
    db.close()


# Main Code
while True:
    user = input("\nWhat would you like to do?\n1) Print all the phones data\n2) Print all the phones data sorted by release date\n3) Print all the phones data sorted by screen size\n4) Print all the phones data sorted by battery capacity\n5) Print all the phones data sorted by price\n6) Exit\nYour Choice: ")
    
    if user == '1':
        print_all_phones()
    elif user == '2':
        by_release_date()
    elif user == '3':
        by_screen_size()
    elif user == '4':
        by_battery_capacity()
    elif user == '5':
        by_price()
    elif user == '6':
        break
    else:
        print("That was not an option!")
