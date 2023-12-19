def stringtoarray(string):
    #convert string to array
    number_strings = string.split()
    return [int(num) for num in number_strings]

def getcredit(line):
    #calculate number credit 
    #把line变成card_string变成
    count = 0
    colon_index = line.find(":")
    content_after_colon = line[colon_index + 1:].strip()
    print(content_after_colon)

    #按分隔符分成两个string
    separator_index = content_after_colon.index("|")
    winnerstring = content_after_colon[:separator_index].strip()
    winnerarray = stringtoarray(winnerstring)
    print(winnerarray)
    checkstring = content_after_colon[separator_index + 1:].strip()
    checkarray = stringtoarray(checkstring)
    print(checkarray)
    for i in range(len(winnerarray)):
        if winnerarray[i] in checkarray:
            count += 1
            print(winnerarray[i])
    if count == 0:
        credit = 0
    else:
        credit = 2**(count - 1)
    #print(winnerarray)
    #print(checkarray)
    return credit

with open('4.txt', 'r') as file:
    result = 0
    for line in file:
        result += getcredit(line)

print(result)
    