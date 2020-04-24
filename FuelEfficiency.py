import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('/client_secret.json',scope)

client = gspread.authorize(creds)

sheet = client.open('fuel_efficiency').sheet1

def calc():
    infoCorrect = False

    while infoCorrect == False:

        print('What is the date you filled up?')
        date = input()

        print('\nWhat is the odometer currently at?')
        currentOdom = int(input())

        prevOdom = sheet.cell(3,2).value

        difference = currentOdom - int(prevOdom)

        print('\nHow many litres put in?')
        litresFilled = float(input())

        litresPer100 = (litresFilled / (difference / 100))

        print('\nNotes? If no, leave blank.')
        note = input()

        print('\n-------------------------------------------------')
        print('Is the following info correct? [Yes/No]\n')
        print('Date: ' + date +'\n')
        print('Current Odometer: ' + str(currentOdom) +'\n')
        print('Litres Filled: ' + str(litresFilled) +'\n')

        if note == ' ':
            pass
        else:
            print('Notes: ' + str(note) + '\n')

        verify = input()

        if verify == "Yes":
            infoCorrect = True
            sheet.insert_row([date, currentOdom, (round(litresPer100, 2)), note],3)
            break
        elif verify != "Yes":
            infoCorrect = False
            print('Try that again...')

calc()
