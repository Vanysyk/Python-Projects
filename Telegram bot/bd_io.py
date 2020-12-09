import telebot
import sqlite3

def create_new_record (u_id, f_name):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS history 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id int, file text, datetime int, result text, user_mark int, parameter text, comment text)""")

    data = (u_id, f_name)

    cursor.execute("""INSERT INTO history (id, user_id, file, datetime, result, user_mark, parameter, comment)
    VALUES (NULL,?,?,NULL,NULL,NULL,NULL,NULL)""", data)
    conn.commit()

    cursor.execute("select id from history where user_id=:u_id ORDER BY id DESC LIMIT 1", {"u_id": u_id})

    bd_response = cursor.fetchall()
    if len(bd_response) < 1 or len(bd_response[0]) < 1:
        print("Без данных в бд")
        conn.close()
        return 0
    else:
        conn.close()
        return bd_response[0][0]

# ff = 1234581234
# f_name = ('ahsmfnbkv')
# create_new_record(ff, f_name)