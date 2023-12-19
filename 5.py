# 查找下一个目标的函数，基于当前数字和源到目标的映射
import time

start_time = time.time()
def getseeds(startnumber,rangenumber):
    array = []
    for i in range(0,rangenumber,1):
        array.append(startnumber + i)
    return array

def findnext(currentnumber, sourceToDestinationMap):
    """
    根据当前数字和源到目标的映射，查找下一个目标。

    参数：
    - currentnumber（int）：要查找下一个目标的当前数字。
    - sourceToDestinationMap（list）：包含元组（目标，源，范围）的列表。

    返回：
    - int：基于提供的映射，下一个目标。
    """
    for destination, source, theRange in sourceToDestinationMap:
        if currentnumber >= source and currentnumber < source + theRange:
            diff = currentnumber - source
            return destination + diff
    
    # 当前数字不在任何范围内，因此必须映射到其自身
    return currentnumber


# 从文件内容中提取某个映射的值数组的函数
def getarray(certainmap):
    """
    从文件内容中提取某个映射的值数组。

    参数：
    - certainmap（str）：要在文件内容中搜索的映射标识符。

    返回：
    - list：从指定映射中提取的值列表。
    """
    file_path = '5.txt'  # 替换为您的文件路径
    toReturn = []

    with open(file_path, 'r') as file:
        content = file.read()
        start_index = content.find(certainmap)
        if start_index != -1:
            map_content = content[start_index:]

            for line in map_content.splitlines():
                if not line.strip():  # 在空行上停止解析
                    break

                if any(char.isdigit() for char in line):
                    values = list(map(int, line.split()))
                    toReturn.append(values)
    return toReturn


# 代码的主要部分
file_path = '5.txt'  # 替换为您的文件路径
with open(file_path, 'r') as file:
    content = file.read()

# 从文件中的'seeds'映射中提取种子数组
seeds_start = content.find('seeds:')
if seeds_start != -1:
    seeds_start += len('seeds:')
    seeds_end = content.find('\n', seeds_start)
    seeds_str = content[seeds_start:seeds_end].strip()
    seeds_array = list(map(int, seeds_str.split()))


range_array = []
new_seeds_array = []
result = 0
for i in range(len(seeds_array)):
    if i % 2 != 0:
        range_array.append(seeds_array[i])
        result += seeds_array[i]
    else:
        new_seeds_array.append(seeds_array[i])
       
seeds_total_number = []

for i in  range(len(new_seeds_array)):
    new = getseeds(new_seeds_array[i],range_array[i])
    print(i)
    seeds_total_number.extend(new)

seeds_array = seeds_total_number


# 从文件中不同映射中加载各种数组
seed_to_soil_array = getarray("seed-to-soil map:")
soil_to_fertilizer_array = getarray('soil-to-fertilizer map:')
fertilizer_to_water_array = getarray('fertilizer-to-water map:')
water_to_light_array = getarray('water-to-light map:')
light_to_temperature_array = getarray('light-to-temperature map:')
temperature_to_humidity_array = getarray('temperature-to-humidity map:')
humidity_to_location_array = getarray("humidity-to-location map:")

# 处理每个种子以找到相应的位置，并将结果存储在'locations'列表中
min_location = 999999999999999999
min_seed = 0
i = 0
for seed in seeds_array:
    print(f"{i}/{len(seeds_array)}")
    soil = findnext(seed, seed_to_soil_array)
    fertilizer = findnext(soil, soil_to_fertilizer_array)
    water = findnext(fertilizer, fertilizer_to_water_array)
    light = findnext(water, water_to_light_array)
    temperature = findnext(light, light_to_temperature_array)
    humidity = findnext(temperature, temperature_to_humidity_array)
    location = findnext(humidity, humidity_to_location_array)
    if location < min_location:
        min_location = location
        min_seed = seed
    i += 1

# 打印最小位置值
print(min_location,min_seed)


# Your code here

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

