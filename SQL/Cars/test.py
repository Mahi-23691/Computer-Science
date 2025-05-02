import sqlite3

DATABASE = 'SQL\Cars\cars.db'

def print_all_cars():
    with sqlite3.connect(DATABASE) as db:

        speed = input("What Speed: ")

        cursor = db.cursor()
        sql = 'SELECT * FROM Car WHERE top_speed > ?;'
        cursor.execute(sql, (speed,))
        results = cursor.fetchall()

        #Print Propersly
        for car in results:
            print(f"Car: {car[1]} || Top Speed: {car[2]}")

if __name__ == '__main__':
    print_all_cars()
