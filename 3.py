def make2d(file_path):
    """
    从指定文件路径读取数据，创建一个二维字符列表。

    参数：
    - file_path (str): 包含数据的文件路径。

    返回值：
    list of list of str: 由文件中的字符组成的二维字符列表。

    该函数打开指定路径的文件，逐行读取文件内容，每行中的字符形成一个子列表，然后将这些子列表组合成一个二维字符列表并返回。

    示例：
    >>> make2d('example.txt')
    [['a', 'b', 'c'], ['1', '2', '3'], ['x', 'y', 'z']]

    注意：
    - 文件应包含字符数据，每行表示一个子列表。
    - 行末的换行符将被忽略。
    """
    with open(file_path, 'r') as file:
        twodearray = []
        for line in file:
            twodearray_row = []
            for char in line:
                if char == '\n':
                    continue
                twodearray_row.append(char)
            twodearray.append(twodearray_row)
    return twodearray


def getvalue(i,j,x):
    """
    从字符串 x[i][j] 中提取数字值，考虑连续的数字字符。

    参数：
    - i (int): 在二维列表 x 中的行索引。
    - j (int): 在字符串 x[i] 中的列索引。
    - x (list of str): 二维字符串列表。

    返回值：
    int: 通过组合 x[i][j] 位置上的连续数字字符得到的整数值。

    该函数查找 x[i][j] 字符左右的数字字符，直到遇到非数字字符为止，将它们组合起来，返回得到的整数值。

    示例：
    >>> getvalue(0, 2, [['a', '1', '23', 'b'], ['c', '456', 'd']])
    123  # 考虑从 x[0][2] 中的 '1' 和 '23'

    注意：
    如果未找到数字字符，函数将返回0。
    """
    if i < 0 or i >= len(x) or j<0 or j >= len(x[i]):
        return 0
    if not x[i][j].isdigit():
        return 0
    left_digits = ""
    index = j
    while index >= 0 and x[i][index].isdigit():          
        left_digits = x[i][index] + left_digits
        x[i][index] = 'x'
        index -= 1
    right_digits = ""
    index = j + 1
    while index < len(x[i]) and x[i][index].isdigit():
        right_digits += x[i][index]
        x[i][index] = 'x'
        index += 1
    total = int(left_digits + right_digits)
    return total


def check(i,j,x):
    result = 0
    if x[i][j] in ['=', '*', '/', '-', '%', '$', '+', '#', '@', '&']:
        result += getvalue(i-1,j-1,x)
        result += getvalue(i,j-1,x)
        result += getvalue(i-1,j,x)
        result += getvalue(i+1,j-1,x)
        result += getvalue(i-1,j+1,x)
        result += getvalue(i+1,j,x)
        result += getvalue(i,j+1,x)
        result += getvalue(i+1,j+1,x)
    return result

def checkgear(i,j,x):
    count = 0
    result = 1
    if x[i][j] != '*':
        return 0
    difference = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
    for diffi,diffj in difference :
        a = getvalue(i+diffi,j+diffj,x)
        if a!= 0:
            count += 1
            result = result * a   
    if count == 2:
        return result
    else:
        return 0
twodearray2 = make2d('3.txt')
twodearray = make2d('3.txt')
symbols = set()
for i in range(len(twodearray)):
    for j in range(len(twodearray[i])):
        if twodearray[i][j] != '.' and not twodearray[i][j].isdigit():
            symbols.add(twodearray[i][j])
print(symbols)
result = 0
gearresult = 0
for i in range(len(twodearray)):
    for j in range(len(twodearray[i])):
        result += check(i,j,twodearray)
#print(result)

for i in range(len(twodearray2)):
    for j in range(len(twodearray2[i])):
        gearresult += checkgear(i,j,twodearray2)

print(gearresult)


def write_2d_array_to_file(two_d_array, output_file):
    with open(output_file, 'w') as file:
        for row in two_d_array:
            # Join elements of the row into a string and write to the file
            file.write(' '.join(map(str, row)) + '\n')

# Output file path
output_file_path = 'output.txt'

# Write the two-dimensional array to the output file
#write_2d_array_to_file(twodearray, output_file_path)
write_2d_array_to_file(twodearray2, output_file_path)
