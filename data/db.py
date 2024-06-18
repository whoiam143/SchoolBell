import sqlite3 as sql


def create_bd():
    with sql.connect("data/music.sqlite3") as con:
        cur = con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS music(
            lesson INTEGER,
            ring_number INTEGER,
            time TEXT,
            path_to_music TEXT);
            """)

        con.commit()


def get_path_to_music(time):
    with sql.connect("data/music.sqlite3") as bd:
        cur = bd.cursor()

        res = cur.execute("""SELECT path_to_music FROM music WHERE time == ? """,
                          (time,))
        return res


def get_all_time():
    with sql.connect("data/music.sqlite3") as bd:
        cur = bd.cursor()

        res = cur.execute("""SELECT time FROM music""")
        time_list = [i[0] for i in list(res)]
        return time_list


def add_result(lesson, ring_number, time, path):
    with sql.connect("data/music.sqlite3") as bd:
        cr = bd.cursor()

        info = cr.execute("""SELECT * FROM music WHERE lesson = ? AND ring_number = ?""",
                          (lesson, ring_number))

        if info.fetchone() is None:
            cr.execute("""INSERT INTO music VALUES (?, ?, ?, ?)""",
                       (lesson, ring_number, time, path))
        else:
            print(time, path, lesson, ring_number)
            cr.execute("""UPDATE music SET time = ? WHERE lesson = ? AND ring_number = ?""",
                       (time, lesson, ring_number))
            cr.execute("""UPDATE music SET path_to_music = ? WHERE lesson = ? AND ring_number = ?""",
                       (path, lesson, ring_number))

        bd.commit()
