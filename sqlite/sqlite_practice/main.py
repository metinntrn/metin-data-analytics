import sqlite3
import os


def create_db():
    if os.path.exists("Students.db"):
        os.remove("Students.db")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()

    return conn, cursor


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE Students(
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            age INTEGER,
            email VARCHAR(255),
            city VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE Courses(
            id INTEGER PRIMARY KEY,
            course_name VARCHAR(255),
            instructor VARCHAR(255),
            credits INTEGER
        );
    """)


def insert_sample_data(cursor):
    students = [
        (1, "Alice Johnson", 20, "alice@gmail.com", "New York"),
        (2, "Bob Smith", 19, "bob@gmail.com", "Chicago"),
        (3, "Carol White", 21, "carol@gmail.com", "Boston"),
        (4, "David Brown", 20, "david@gmail.com", "New York"),
        (5, "Emma Davis", 22, "emma@gmail.com", "Seattle")
    ]

    cursor.executemany(
        "INSERT INTO Students VALUES (?,?,?,?,?)",
        students
    )

    courses = [
        (1, "Python Programming", "Dr. Anderson", 3),
        (2, "Web Development", "Prof. Wilson", 4),
        (3, "Data Science", "Dr. Taylor", 3),
        (4, "Mobile Apps", "Prof. Garcia", 2)
    ]

    cursor.executemany(
        "INSERT INTO Courses VALUES (?,?,?,?)",
        courses
    )

    print("Sample data inserted successfully")


def basic_sql_operation(cursor):

    # 1 - SELECT ALL
    print("----- Select All -----")

    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()

    for row in records:
        print(
            f"Id: {row[0]} | "
            f"Name: {row[1]} | "
            f"Age: {row[2]} | "
            f"E-mail: {row[3]} | "
            f"City: {row[4]}"
        )

    # 2 - SELECT COLUMNS
    print("----- Select Columns -----")

    cursor.execute("SELECT name, age FROM Students")
    records_2 = cursor.fetchall()

    print(records_2)

    # 3 - WHERE CLAUSE
    print("----- Where age = 20 -----")

    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records_3 = cursor.fetchall()

    print(records_3)

    # 4 - ORDER BY
    print("----- Order By -----")

    cursor.execute("SELECT * FROM Students ORDER BY age")
    records_4 = cursor.fetchall()

    print(records_4)


def sql_update_delete_insert_operations(conn, cursor):

    # INSERT
    cursor.execute("""
        INSERT INTO Students
        VALUES (6, 'Frank Miller', 23, 'frankmill@gmail.com', 'Maryland')
    """)

    cursor.execute("""
        INSERT INTO Students
        VALUES (7, 'Peter Parker', 18, 'spiidy__@gmail.com', 'Queens')
    """)

    conn.commit()

    # UPDATE
    cursor.execute("""
        UPDATE Students
        SET age = 69
        WHERE id = 6
    """)

    conn.commit()

    # DELETE
    cursor.execute("""
        DELETE FROM Students
        WHERE id = 2
    """)

    conn.commit()


def aggregate_func(cursor):

    # COUNT
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()

    print(f"Count: {result}")

    # AVERAGE
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()

    print(f"Average age: {result}")

    # MAX - MIN
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchall()

    print(f"MAX / MIN: {result}")

    # GROUP BY
    cursor.execute("""
        SELECT city, COUNT(*)
        FROM Students
        GROUP BY city
    """)

    result = cursor.fetchall()

    print(result)


def questions(cursor):
    """
    Basit

    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Queens'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı

    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Queens' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    """

    # 1
    cursor.execute("SELECT * FROM Courses")
    result = cursor.fetchall()
    print(result)

    # 2
    cursor.execute("""
        SELECT course_name, instructor
        FROM Courses
    """)
    result = cursor.fetchall()
    print(result)

    # 3
    cursor.execute("""
        SELECT *
        FROM Students
        WHERE age = 21
    """)
    result = cursor.fetchall()
    print(result)

    # 4
    cursor.execute("""
        SELECT *
        FROM Students
        WHERE city = 'Queens'
    """)
    result = cursor.fetchall()
    print(result)

    # 5
    cursor.execute("""
        SELECT course_name
        FROM Courses
        WHERE instructor = 'Dr. Anderson'
    """)
    result = cursor.fetchone()
    print(result)

    # 6
    cursor.execute("""
        SELECT *
        FROM Students
        WHERE name LIKE 'A%'
    """)
    result = cursor.fetchall()
    print(result)

    # 7
    cursor.execute("""
        SELECT course_name
        FROM Courses
        WHERE credits >= 3
    """)
    result = cursor.fetchall()
    print(result)

    # Detaylı 1
    cursor.execute("""
        SELECT *
        FROM Students
        ORDER BY name
    """)
    result = cursor.fetchall()
    print(result)

    # Detaylı 2
    cursor.execute("""
        SELECT *
        FROM Students
        WHERE age > 20
        ORDER BY name
    """)
    result = cursor.fetchall()
    print(result)

    # Detaylı 3
    cursor.execute("""
        SELECT name, city
        FROM Students
        WHERE city IN ('New York', 'Queens')
    """)
    result = cursor.fetchall()
    print(result)

    # Detaylı 4
    cursor.execute("""
        SELECT name, city
        FROM Students
        WHERE city != 'New York'
    """)
    result = cursor.fetchall()
    print(result)


def main():

    conn, cursor = create_db()

    try:
        create_table(cursor)
        insert_sample_data(cursor)
        basic_sql_operation(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_func(cursor)
        questions(cursor)

        conn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
