INPUTMIN = 240298
INPUTMAX = 784956

potentialPasswordCount = 0

for password in range(INPUTMIN, INPUTMAX):
    # check adjacent
    hasAdjacent = False
    password = str(password)
    for digit in password:
        if str(int(digit)*11) in password and str(int(digit)*111) not in password:
            hasAdjacent = True
    # check decrease
    neverDecrease = True
    for index in range(1, len(password)):
        if int(password[index-1]) > int(password[index]):
            neverDecrease = False

    if (hasAdjacent and neverDecrease):
        potentialPasswordCount += 1

print(f'Count: {potentialPasswordCount}')
