import sqlite3


def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS course(courseID INTEGER PRIMARY KEY AUTOINCREMENT,name text , duration text , charges text , description text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY ,name text, email text, gender text, dob text, contact text, admission text, course text, state text, city text, pin text , address text)"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY ,roll text, name text, course text, marks_ob text, full_marks text , per text)"
    )
    con.commit()

    con.close()

    # roll, name, email, gender, dob,contact,admission,course,state,city,pin,address


create_db()
