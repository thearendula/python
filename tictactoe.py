board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def isSpaceFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")
    print("-----------")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b, l):

    return ((b[1] == l and b[2] == l and b[3] == l) or 
    (b[4] == l and b[5] == l and b[6] == l) or 
    (b[7] == l and b[8] == l and b[9] == l) or 
    (b[1] == l and b[5] == l and b[9] == l) or 
    (b[2] == l and b[5] == l and b[8] == l) or 
    (b[3] == l and b[5] == l and b[7] == l) or 
    (b[3] == l and b[6] == l and b[9] == l) or 
    (b[1] == l and b[4] == l and b[7] == l))

def playerMove():
    
    run = True

    while run:
        move = input("Please select the position to enter the X between boxes 1 to 9 : ")
        
        try:
            move = int(move)
            
            if move > 0 and move < 10:
                
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)
            
                else:
                    print("\nThis place is occupied")
            
            else:
                print("\nPlease type a number between 1 to 9 : ")
        
        except:
            print("Please type a number : ")

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def compMove():
    possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['0', 'X']:
        for i in possibleMove:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMove:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if  5 in possibleMove:
        move = 5
        return move

    
    edgesOpen = []
    for i in possibleMove:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def main():
    
    print("Welcome to the game")
    

    while not(isBoardFull(board)):
    
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("\n\nYou Loose")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print(" ")
            
            else:
                insertLetter('O', move)
                print("\nComputer placed an O on the position", move, ":")
                printBoard(board)
        else:
            print("\nCongo! You Win")
            break

        if isBoardFull(board):
            print("Game Tied")


while (True):
    
    x = input("\n\nDo you want to play again : (Y/N) : ")

    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("----------------------")
        main()
    else:
        break