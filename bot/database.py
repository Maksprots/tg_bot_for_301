import sqlite3
from datetime import date



class Database:

    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                      (id INTEGER  PRIMARY KEY,
                       interval INTEGER,
                        last_day_notif TEXT)''')
        self.connection.commit()


    def write_user(self, id, interval):
        date_now = (date.today())
        self.cursor.execute(f'''INSERT INTO Users(id, interval , last_day_notif)
         VALUES ({id}, {interval}, '{date_now.strftime('%Y:%m:%d')}');''')
        self.connection.commit()


    def del_user(self, id):
        try:
            self.cursor.execute(f'''DELETE FROM 
             Users WHERE id = {id}''')
            self.connection.commit()
        except sqlite3.Error as er:
            print('Скорее всего  id нет в бд, но'
                  'почитай', er)

    def get_user_stat(self, id):
        try:
            self.cursor.execute(f'''SELECT * FROM Users WHERE id = {id}''')
            self.connection.commit()
            records = self.cursor.fetchall()
            records[0]
            return 1
        except :
            return 0
    def get_all_users(self):
        self.cursor.execute(f'''SELECT * FROM Users''')
        self.connection.commit()
        records = self.cursor.fetchall()
        return records



