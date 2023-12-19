import math
def ways(time, distance):
    result = 0
    left = round((time + math.sqrt(time**2 - 4*distance))/2)
    right = int((time + math.sqrt(time**2 + 4*distance))/2)
    return right - left

    return result

time = [41968894]
distance = [214178911271055]
multi_result = 1

for i in range(1):
    multi_result *= ways(time[i],distance[i])

print(multi_result)