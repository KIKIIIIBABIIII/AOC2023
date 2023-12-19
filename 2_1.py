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
                bluenumber = max(int(matchblue.group(1)),bluenumber)
            if matchred:
                matchred = re.search(r'(\d+)\s+red', newsegment)
                rednumber = max(int(matchred.group(1)),rednumber)
            if matchgreen:
                matchgreen = re.search(r'(\d+)\s+green', newsegment)
                greennumber = max(int(matchgreen.group(1)),greennumber)
    return rednumber * greennumber * bluenumber
    

with open('2.txt', 'r') as file:
    result = 0
    gameID = 1
    for line in file:
        result += parse_line( line )
    print(result)

