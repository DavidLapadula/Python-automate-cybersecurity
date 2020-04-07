dog1 = {'name': 'Garfield', 'color': 'orange'}
dog2 = {'name': 'Patrick', 'color': 'purple'}

allDogs = []
allDogs.append(dog1)
allDogs.append(dog2)

board = {
        'top-L' : ' ', 
        'top-M' : ' ', 
        'top-R' : ' ', 
        'mid-L' : ' ',
        'mid-M' : ' ',
        'mid-R' : ' ',
        'low-L' : ' ',
        'low-M' : ' ',
        'low-R' : ' '
    }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('----------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('----------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(board)