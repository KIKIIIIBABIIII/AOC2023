import re

def parse_line( line ):
    """解析输入文件中的单行（游戏），如果游戏可能，则返回true，否则返回false"""
    segments = line.strip().split(';')
    greennumber = 0
    bluenumber = 0
    rednumber = 0
    for segment in segments:
        if 'Game' in segment:
            segment = segment.replace("Game : ", "")
        newline = segment.strip()
        newsegments = newline.strip().split(',')
        for newsegment in newsegments:
            matchblue = re.search(r'(\d+)\s+blue', newsegment)
            matchred = re.search(r'(\d+)\s+red', newsegment)
            matchgreen = re.search(r'(\d+)\s+green', newsegment)
            if matchblue:
                matchblue = re.search(r'(\d+)\s+blue', newsegment)
                bluenumber = int(matchblue.group(1))
                if(int(matchblue.group(1))>14):
                    return False
            if matchred:
                matchred = re.search(r'(\d+)\s+red', newsegment)
                rednumber = int(matchred.group(1))
                if(int(matchred.group(1))>12):
                    return False
            if matchgreen:
                matchgreen = re.search(r'(\d+)\s+green', newsegment)
                greennumber = int(matchgreen.group(1))
                if(int(matchgreen.group(1))>13):
                    return False
            sum =  rednumber + greennumber + bluenumber
            if sum > 39:
                return False
    return True

with open('2.txt', 'r') as file:
    result = 0
    gameID = 1
    for line in file:
        if parse_line(line):
            result += gameID
        gameID += 1
    print(result)

