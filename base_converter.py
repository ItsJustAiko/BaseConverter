nb = input("Number:")
baseDuNb = input("Num base:")
baseSouhaitee = input("Wanted base:")

def convertToBaseTen(number, fromBase):
    if fromBase == 10:
        return number

    # Convert to base 10
    base10 = 0
    string = ''
    for i, digit in enumerate(reversed(str(number))):
        string += digit + '*' + str(fromBase) + '^' + str(i) + ' + '
        base10 += int(digit) * (int(fromBase) ** i)
    return {'result': int(base10), 'operation': string[:-3]}

def base(number, fromBase, toBase):

    if int(toBase) > 32 or int(fromBase) > 32:
        print("Base too high")
        return

    if int(fromBase) == int(toBase):
        return number

    # If number is hexadecimal, convert it to int
    if int(fromBase) == 16:
        number = int(number, 16)
        baseTenConverted = { 'result': number, 'operation': number }
    else:
        baseTenConverted = convertToBaseTen(number, fromBase)


    if toBase == 10:
        return baseTenConverted['operation'] + ' = ' + str(baseTenConverted['result'])

    baseTenTwo = baseTenConverted['result']

    # Convert to toBase
    newNumber = ''
    strNumber = ''
    string = ''
    nbDigit = 1
    while baseTenTwo > 0:
        newNumber = str(int(baseTenTwo) % int(toBase)) + newNumber
        baseTenTwo //= int(toBase)
        string += str(baseTenTwo) + '/' + str(toBase) + ' = ' + str(baseTenTwo // int(toBase)) + ' reste ' + str(baseTenTwo % int(toBase)) + ' + '

    ## Add a space every 4 digits in newNumber
    for i, digit in enumerate(reversed(newNumber)):
        if i % 4 == 0 and i != 0:
            strNumber = ' ' + strNumber
        strNumber = digit + strNumber

    return string[:-2] + ' = ' + strNumber

print(base(nb, baseDuNb, baseSouhaitee))
