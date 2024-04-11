from flask import Flask
from sense_hat import SenseHat
app = Flask(__name__)
##sense = SenseHat()
import gspread
from datetime import datetime


from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials to access Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ttsheet.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheetffs spreadsheet
sheet = client.open('ttSheet123').sheet1
sh=""
# Function to write winner records to the spreadsheet
@app.route('/')
def index():
    


    val="<table><tr><td>No.</td><td>Time<td><td>Winner></td>Opponet<td></td></tr"

    sno=1
    rows=sheet.get_all_values()
    for row in rows:
       if 1==0:
           val=val
 
       else:
              
          val=val+"<tr><td>" +str(sno)+"</td>"
          val=val+"<td>"+row[0]+"</td>"
          val=val+"<td>"+row[1]+"</td>"
          val=val+"<td>"+row[2]+"</td></tr>"
    val=val+"</table>"
   
    return val

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
