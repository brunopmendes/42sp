def number_in_line():
    arq = open("numbers.txt", 'r') 
    for number in arq:
        currentLine = number.split(',')
        for x in currentLine:
            print(x)

if __name__ == '__main__':
    number_in_line()