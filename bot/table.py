from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import config


class Sheets:
    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', config.Config.SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('sheets', 'v4', credentials=creds)

    def read_material(self, video):
        """
        If you want to get video materials
        instsall video = True, if dp materials
        install video = False
        :param video:
        :return: list[list[]]
        """

        if video:
            rng = config.Config.PLACE_VIDEO_MAT
        else:
            rng = config.Config.PLACE_ELSE_MAT

        result = self.service.spreadsheets().values().get(
            spreadsheetId=config.Config.SPREADSHEET_ID,
            range=rng
        ).execute()
        values = result.get('values', [])
        return values


if __name__ == '__main__':
    # just for debug
    data = Sheets()
    print(data.read_material(True))
