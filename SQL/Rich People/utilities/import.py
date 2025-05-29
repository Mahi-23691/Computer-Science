import sqlite3
import csv

# Paths
CSV_FILE = r"C:\PersonalUse\School\Computer Science\SQL\Rich People\Data\rich_people.csv"
DB_FILE = r"C:\PersonalUse\School\Computer Science\SQL\Rich People\Data\rich_people.db"

# Connect
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# ----------- DROP OLD TABLES -------------
cursor.executescript('''
DROP TABLE IF EXISTS WealthSource;
DROP TABLE IF EXISTS Summary;
DROP TABLE IF EXISTS People;
''')

# ----------- RECREATE TABLES -------------
cursor.executescript('''
CREATE TABLE People (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birth_date TEXT,
    age INTEGER,
    gender TEXT,
    country TEXT,
    city TEXT,
    rank INTEGER,
    net_worth_billion REAL
);

CREATE TABLE Summary (
    summary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    organization_name TEXT,
    position_in_organization TEXT,
    self_made BOOLEAN,
    FOREIGN KEY (person_id) REFERENCES People(person_id)
);

CREATE TABLE WealthSource (
    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    business_industries TEXT,
    FOREIGN KEY (person_id) REFERENCES People(person_id)
);
''')

print("✅ Tables dropped and recreated.")

# ----------- IMPORT DATA -------------
with open(CSV_FILE, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if not row['full_name'].strip():
            continue  # skip empty rows

        name = row['full_name'].strip()
        birth_date = row['birth_date'].strip()
        
        # Safe conversion
        age = int(row['age']) if row['age'].strip().isdigit() else None
        rank = int(row['rank']) if row['rank'].strip().isdigit() else None
        
        try:
            net_worth = float(row['net_worth']) if row['net_worth'].strip() else None
        except ValueError:
            net_worth = None

        gender = row['gender'].strip()
        country = row['country_of_residence'].strip()
        city = row['city_of_residence'].strip()

        # Insert into People
        cursor.execute('''
            INSERT INTO People (name, birth_date, age, gender, country, city, rank, net_worth_billion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, birth_date, age, gender, country, city, rank, net_worth))

        person_id = cursor.lastrowid

        # Insert into Summary
        cursor.execute('''
            INSERT INTO Summary (person_id, organization_name, position_in_organization, self_made)
            VALUES (?, ?, ?, ?)
        ''', (
            person_id,
            row['organization_name'].strip(),
            row['position_in_organization'].strip(),
            row['self_made'].strip().upper() == 'TRUE'
        ))

        # Insert into WealthSource
        cursor.execute('''
            INSERT INTO WealthSource (person_id, business_industries)
            VALUES (?, ?)
        ''', (
            person_id,
            row['business_category'].strip()
        ))

# Finalize
conn.commit()
conn.close()
print("✅ Fresh data imported successfully.")
