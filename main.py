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
#def printV():
#    rows=sheet.get_all_values()
#    for row in rows:
#        for each col 
#        print(row)
# Function to write winner records to the spreadsheet
def write_winner_to_sheet(winner, Looser):
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M:%S")
    row = [dt_string,winner, Looser]
    sheet.append_row(row)



import random
import time
from sense_hat import SenseHat
# from time import sleep
sense = SenseHat()
cursorColor = (255, 255, 0)
playerTurn = 1
gameOver = False
LastMove = 0
# Yellow
playerColor = (0, 0, 224)  # Blue
computerColor = (204, 0, 0)  # Red
black = (0, 0, 0)
GREEN = (0, 204, 0)
PLAYER = 1
COMPUTER = 2
CURSOR = 3
gameLevel = 2


def printGreenBar():
    row1 = 2
    row2 = 5
    col1 = 2
    col2 = 5
    for x in range(8):
        sense.set_pixel(row1, x, GREEN)
        sense.set_pixel(row2, x, GREEN)
        sense.set_pixel(x, col1, GREEN)
        sense.set_pixel(x, col2, GREEN)


def printBoard(boxNo, color, type):
    col1 = 0
    col2 = 1
    row1 = 0
    row2 = 1
    if(boxNo == 1 or boxNo == 2 or boxNo == 3):
        col1 = 0
        col2 = 1
    if(boxNo == 4 or boxNo == 5 or boxNo == 6):
        col1 = 3
        col2 = 4
    if(boxNo == 7 or boxNo == 8 or boxNo == 9):
        col1 = 6
        col2 = 7
    if(boxNo == 1 or boxNo == 4 or boxNo == 7):
        row1 = 0
        row2 = 1
    if(boxNo == 2 or boxNo == 5 or boxNo == 8):
        row1 = 3
        row2 = 4
    if(boxNo == 3 or boxNo == 6 or boxNo == 9):
        row1 = 6
        row2 = 7
    if(type == PLAYER):
        sense.set_pixel(row1, col1, color)
        sense.set_pixel(row1, col2, black)
        sense.set_pixel(row2, col1, black)
        sense.set_pixel(row2, col2, color)
    if(type == COMPUTER):
        sense.set_pixel(row1, col1, black)
        sense.set_pixel(row1, col2, color)
        sense.set_pixel(row2, col1, color)
        sense.set_pixel(row2, col2, black)
    if(type == CURSOR):
        sense.set_pixel(row1, col1, color)
        sense.set_pixel(row1, col2, color)
        sense.set_pixel(row2, col1, color)
        sense.set_pixel(row2, col2, color)


game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
currentPos = 1
lastPos = 1


def setCursorPos(pos):
    global lastPos
    global currentPos

    if lastPos == 1:
        if not(pos == 2 or pos == 4):
            pos = 1
    elif lastPos == 2:
        if not(pos == 1 or pos == 3 or pos == 5):
            pos = 2
    elif lastPos == 3:
        if not(pos == 2 or pos == 6):
            pos = 3
    elif lastPos == 4:
        if not(pos == 1 or pos == 5 or pos == 7):
            pos = 4
    elif lastPos == 6:
        if not(pos == 3 or pos == 5 or pos == 9):
            pos = 6
    elif lastPos == 7:
        if not(pos == 4 or pos == 8):
            pos = 7
    elif lastPos == 8:
        if not(pos == 7 or pos == 5 or pos == 9):
            pos = 8
    elif lastPos == 9:
        if not(pos == 8 or pos == 6):
            pos = 9
    currentPos = pos
    lastPos = currentPos


def moveOn():
    global LastMove
    ret = 0
    if game[currentPos-1] == 0:
        game[currentPos-1] = playerTurn
        ret = 1
        LastMove = currentPos

    else:
        ret = 0
    if ret == 1:
        checkWinOrDraw()
    return ret


def wincheck(ph, fr):
    w = 0
    for i in range(len(ph)):
        if len(fr) == 3:
            if ph[i] == fr[0] or ph[i] == fr[1] or ph[i] == fr[2]:
                w = w+1
        elif len(fr) == 2:
            if ph[i] == fr[0] or ph[i] == fr[1]:
                w = w+1
    return w


def checkWinner(phouse):
    win = 0

    if (wincheck(phouse, "123") == 3 or wincheck(phouse, "147") == 3
            or wincheck(phouse, "159") == 3 or wincheck(phouse, "258") == 3
            or wincheck(phouse, "369") == 3 or wincheck(phouse, "357") == 3 or wincheck(phouse, "456") == 3
            ):
        win = 1
    return win


def computerTurn():
    global playerTurn
    rndPos = random.randrange(0, 8)
    ret = 0
    if game[rndPos] == 0:
        game[rndPos] = playerTurn
        ret = 1
        currentPos = rndPos + 1
    else:
        ret = 0
    if(ret == 0):
        for x in range(9):
            if(game[x] == 0):
                game[x] = playerTurn
                ret = 1
                break
    if ret == 1:
        checkWinOrDraw()
    playerTurn = PLAYER
    return ret


def computerTurnProLevel():
    global LastMove
    global playerTurn
    global game
    rnd = 0
    ret = 0
    cont = ""
    for x in range(9):
        if(game[x] == COMPUTER):
            cont = cont + str(x+1)

    if len(cont) >= 2:
        if game[2] == 0 and (wincheck(cont, "12") == 2 or wincheck(cont, "57") == 2 or wincheck(cont, "69") == 2):
            rnd = 3
        elif game[0] == 0 and (wincheck(cont, "23") == 2 or wincheck(cont, "47") == 2 or wincheck(cont, "59") == 2):
            rnd = 1
        elif game[1] == 0 and (wincheck(cont, "13") == 2 or wincheck(cont, "58") == 2):
            rnd = 2
        elif game[3] == 0 and (wincheck(cont, "17") == 2 or wincheck(cont, "56") == 2):
            rnd = 4
        elif game[4] == 0 and (wincheck(cont, "19") == 2 or wincheck(cont, "38") == 2 or wincheck(cont, "46") == 2):
            rnd = 5
        elif game[5] == 0 and (wincheck(cont, "39") == 2 or wincheck(cont, "45") == 2):
            rnd = 6
        elif game[6] == 0 and (wincheck(cont, "14") == 2 or wincheck(cont, "35") == 2 or wincheck(cont, "89") == 2):
            rnd = 7
        elif game[7] == 0 and (cont == "79" or cont == "25"):
            rnd = 8
        elif game[8] == 0 and (wincheck(cont, "36") == 2 or wincheck(cont, "15") == 2 or wincheck(cont, "78") == 2):
            rnd = 9
    cont = ""
    for x in range(9):
        if(game[x] == PLAYER):
            cont = cont + str(x+1)

    if rnd > 0:
        if game[rnd - 1] == 0:
            game[rnd - 1] = playerTurn
            ret = 1
        else:
            ret = 0
    if ret > 0:
        cont = ""

    if (LastMove == 5 and cont == "5" and ret == 0):
        rnd = random.choice([2, 4, 8, 6])
        cont = ""
    print(game)
    np=-1
    if ret == 0 and len(cont)==1:
      
      if LastMove==1:
        if game[4]==0:
          np=4
        elif game[3]==0:
          np=3
        elif game[1]==0:
          np=1
      elif LastMove==2:
        if game[4]==0:
          np=4
        elif game[2]==0:
          np=2
        elif game[0]==0:
          np=0
      elif LastMove==3:
        if game[4]==0:
          np=4
        elif game[5]==0:
          np=5
        elif game[1]==0:
          np=1
      elif LastMove==4:
        if game[4]==0:
          np=4
        elif game[6]==0:
          np=6
        elif game[0]==0:
          np=0
      elif LastMove==5:
        if game[0]==0:
          np=0
        elif game[1]==0:
          np=1
        elif game[2]==0:
          np=2
      elif LastMove==6:
        if game[4]==0:
          np=4
        elif game[8]==0:
          np=8
        elif game[2]==0:
          np=2
      elif LastMove==7:
        if game[4]==0:
          np=4
        elif game[7]==0:
          np=7
        elif game[3]==0:
          np=3
      elif LastMove==8:
        if game[4]==0:
          np=4
        elif game[8]==0:
          np=8
        elif game[6]==0:
          np=6
      elif LastMove==9:
        if game[4]==0:
          np=4
        elif game[7]==0:
          np=7
        elif game[5]==0:
          np=5

      if np>=0:
        game[np] = playerTurn
        ret = 1
        cont = ""
    
    if len(cont) >= 2:
        if game[2] == 0 and (wincheck(cont, "12") == 2 or wincheck(cont, "57") == 2 or wincheck(cont, "69") == 2):
            rnd = 3
        elif game[0] == 0 and (wincheck(cont, "23") == 2 or wincheck(cont, "47") == 2 or wincheck(cont, "59") == 2):
            rnd = 1
        elif game[1] == 0 and (wincheck(cont, "13") == 2 or wincheck(cont, "58") == 2):
            rnd = 2
        elif game[3] == 0 and (wincheck(cont, "17") == 2 or wincheck(cont, "56") == 2):
            rnd = 4
        elif game[4] == 0 and (wincheck(cont, "19") == 2 or wincheck(cont, "37") == 2 or wincheck(cont, "28") == 2 or wincheck(cont, "46") == 2):
            rnd = 5
        elif game[5] == 0 and (wincheck(cont, "39") == 2 or wincheck(cont, "45") == 2):
            rnd = 6
        elif game[6] == 0 and (wincheck(cont, "14") == 2 or wincheck(cont, "35") == 2 or wincheck(cont, "89") == 2):
            rnd = 7
        elif game[7] == 0 and (cont == "79" or cont == "25"):
            rnd = 8
        elif game[8] == 0 and (wincheck(cont, "36") == 2 or wincheck(cont, "15") == 2 or wincheck(cont, "78") == 2):
            rnd = 9

    if rnd > 0 and ret == 0:
        if game[rnd - 1] == 0:
            game[rnd - 1] = playerTurn
            ret = 1
        else:
            ret = 0

    if(ret == 0):
        ret = computerTurn()
    checkWinOrDraw()
    playerTurn = PLAYER
    return ret


def checkWinOrDraw():
    global gameOver
    draw = 1
    playerHouse = ""
    computerHouse = ""
    for x in range(9):
        if(game[x] == 0):
            draw = 0
        elif(game[x] == PLAYER):
            playerHouse = playerHouse + str(x+1)
        elif(game[x] == COMPUTER):
            computerHouse = computerHouse + str(x+1)

    if checkWinner(playerHouse) == 1:
        sense.show_message("You are a winner")
        write_winner_to_sheet ("Harikant","Aastha")
        gameOver = True
        playerTurn = COMPUTER
        draw = 0
    if checkWinner(computerHouse) == 1:
        printGrid()
        time.sleep(1)
        write_winner_to_sheet ("Aastha","Harikantt")
        sense.show_message("Computer Winner")
        gameOver = True
        draw = 0
    if(draw == 1):
        sense.show_message("Game Over")
        gameOver = True
    if gameOver:
        clearGame()


def printGrid():
    sense.clear()
    printGreenBar()
    for x in range(9):
        if(game[x] == 1):
            printBoard(x+1, playerColor, PLAYER)
        elif(game[x] == 2):
            printBoard(x+1, computerColor, COMPUTER)


def clearGame():
    global playerTurn
    global currentPos
    global gameOver
    global game
    global LastMove
    gameOver = False
    playerTurn = 1
    LastMove = 0
    for x in range(9):
        game[x] = 0
    gameLevel = 2
    currentPos = 1
    showCursor = 1


showCursor = 1
while True:
    time.sleep(0.3)
    if gameLevel == 0:
        for event in sense.stick.wait_for_events():
            if event.action == "pressed":
                print("pressed")
                if event.direction == "left":
                    print("left")
                    gameLevel = 1
                if event.direction == "right":
                    print("right")
                    gameLevel = 2
    if gameOver:
        clearGame()

    if gameLevel > 0:
        printGrid()
    if playerTurn == 1:
        if showCursor == 1:
            printBoard(currentPos, cursorColor, CURSOR)
        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":
                showCursor = 1
                # Check which direction
                if event.direction == "up":
                    currentPos = currentPos - 3
                    # sense.show_letter("U")      # Up arrow
                elif event.direction == "down":
                    currentPos = currentPos + 3
                    # sense.show_letter("D")      # Down arrow
                elif event.direction == "left":
                    print("left")
                    currentPos = currentPos - 1
                    # sense.show_letter("L")      # Left arrow
                elif event.direction == "right":
                    currentPos = currentPos + 1
                elif event.direction == "middle":
                    # sense.show_letter("M")      # Enter key
                    if moveOn() == 1:
                        playerTurn = 2
                        printGrid()
                        showCursor = 0
                setCursorPos(currentPos)
    else:
        if gameLevel == 1:
            if computerTurn() == 1:
                playerTurn = 1
                time.sleep(1)
        if gameLevel == 2:
            if computerTurnProLevel() == 1:
                playerTurn = 1
                time.sleep(1)
