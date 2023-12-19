
mydict = {
    "one": "1",
    "two": "2",         
    "three":"3",
    "four" : "4",
    "five":"5",     
    "six":"6",    
    "seven":"7",
    "eight":"8",
    "nine":"9",
} 
def getnumber(line,i):
    for number in mydict:
        if line.startswith(number,i):
            return mydict[number] 
    return line[i]
def getnewline(line):
    new_line = ""
    for i in range(len(line)):
           new_line +=  getnumber(line,i)
    return new_line

with open('1.txt', 'r') as file:
    result = 0
    for line in file:
        print("old line is:",line)
        line = getnewline(line)
        print("new line is:",line)
        new_list = []
        for char in line:
            if char.isdigit():
                new_list.append(char)
        result += 10 * int(new_list[0]) + int(new_list[-1])
        #print(line,10 * int(new_list[0]) + int(new_list[-1]))
#print("the answer is:", result)




    
