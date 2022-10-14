from dataclasses import dataclass

@dataclass
class Config:
    SPREADSHEET_ID = '1RTsLHeGOxF6B6PKLFpSK1LmNvL52LVDYsg7BkSivDNs'
    # do not change
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    PLACE_VIDEO_MAT = ('Лист1!A:A')
    PLACE_ELSE_MAT = ('Лист1!B:B')
    BOT_TOKEN = '5715386004:AAGzt0o5x9YUyiBG9g4x3wxseXj4OeoEVjQ'


    # messages
    START_msg ='как часто напоминать тебе учиться в днях?'
    NOTIF = 'Пора учиться!!!'
