from datetime import datetime
import database
import config
import threading



class Sendler:
    def __init__(self, bot):
        self.db = database.Database()
        self.bot = bot


    def __call__(self, *args, **kwargs):
        thread = threading.Thread(target=self.main)
        thread.start()

    def main(self):
        db = database.Database()
        while True:
            users = db.get_all_users()
            for i in range(len(users)):
                lst_date = datetime.strptime(users[i][2], '%Y:%m:%d')
                nw =  datetime.now()
                dif = nw - lst_date
                if dif == users[i][1]:
                     self.bot.send_message(
                         users[i][0],
                         config.Config.NOTIF)



