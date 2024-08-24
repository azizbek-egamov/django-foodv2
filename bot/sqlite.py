import sqlite3


def sql_connect():
    try:
        connection = sqlite3.connect("../db.sqlite3")  # SQLite3 bazasiga bog'lanish
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def sql_connection():
    connection = sqlite3.connect("../db.sqlite3")  # SQLite3 bazasiga bog'lanish
    connection.commit()
    return connection

def add_information(uid, full_name, username, balance, orders, payment, offer, ban):
    conn = sql_connection()
    if conn:
        try:
            r = one_table_info("users", "uid", uid)
            if r == False:
                cursor = conn.cursor()
                cursor.execute(
                    """INSERT INTO users (uid, full_name, username, balance, orders, payment, offer, ban) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (uid, full_name, username, balance, orders, payment, offer, ban),
                )
                conn.commit()
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            conn.close()
    return False

def AddLangInformation(uid, lang):
    conn = sql_connection()
    if conn:
        try:
            r = one_table_info("main_lang", "uid", uid)
            if r == False:
                cursor = conn.cursor()
                cursor.execute(
                    """INSERT INTO main_lang (uid, lang) VALUES (?, ?)""",
                    (uid, lang),
                )
                conn.commit()
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            conn.close()
    return False


def select_info(id):
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {id}")

        res = cursor.fetchall()
        conn.commit()
        l = list()
        if not res:
            return False
        else:
            for i in res:
                l.append(i)
            return l
    else:
        return False


def delete_table(da, ta, keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {da} WHERE {ta} = {keys}")
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def drop_table(keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"drop table {keys}")
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def UpdateRaferalCount(id, count):
    if sql_connect() == True:
        try:
            con = sql_connection()
            cur = con.cursor()
            cur.execute("UPDATE users SET offer = ? WHERE uid = ?", (count, id))
            con.commit()
            print(f"Updated ID: {id} with offer: {count}")  # Logging
            return True
        except:
            return False
    else:
        return False
    
def UpdateLang(id, lang):
    if sql_connect() == True:
        try:
            con = sql_connection()
            cur = con.cursor()
            cur.execute("UPDATE main_lang SET lang = ? WHERE uid = ?", (lang, id))
            con.commit()
            print(f"Updated ID: {id} with lang: {lang}")  # Logging
            return True
        except:
            return False
    else:
        return False



def table_info(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()

        if not res:
            return False
        else:
            return res
    else:
        return False


def one_table_info(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchone()
        conn.commit()

        if not res:
            return False
        else:
            return res
    else:
        return False


def AddUserInfo(uid, username, phone):
    if sql_connect() == True:
        conn = sql_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO main_users (user_id, username, phone) VALUES (?, ?, ?)""",
                (uid, username, phone),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            conn.close()
    else:
        return False
