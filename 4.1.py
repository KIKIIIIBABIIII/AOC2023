def stringtoarray(string):
    #convert string to array
    number_strings = string.split()
    return [int(num) for num in number_strings]

def getcount(line):
    #calculate number credit 
    #把line变成card_string变成
    count = 0
    colon_index = line.find(":")
    content_after_colon = line[colon_index + 1:].strip()
    #print(content_after_colon)

    #按分隔符分成两个string
    separator_index = content_after_colon.index("|")
    winnerstring = content_after_colon[:separator_index].strip()
    winnerarray = stringtoarray(winnerstring)
    #print(winnerarray)
    checkstring = content_after_colon[separator_index + 1:].strip()
    checkarray = stringtoarray(checkstring)
    #print(checkarray)
    for i in range(len(winnerarray)):
        if winnerarray[i] in checkarray:
            count += 1
            #print(winnerarray[i])
    return count

dicnumber = {}
for card_number in range(1, 199):
    dicnumber[card_number] = 1
print(dicnumber)

with open('4.txt', 'r') as file:
    cardid = 1
    for line in file:
        matches = getcount(line)
        for i in range(0,matches):
            dicnumber[cardid+1+i] +=  dicnumber[cardid]
            print("一张卡赢的卡的数量", matches)
            print("总共赢的卡的数量",dicnumber[cardid] * matches)
        cardid += 1
result = 0
for card_number in range(1, 199):
    result += dicnumber[card_number]

print("最终结果是：",result)
#print(dicnumber)

