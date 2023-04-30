# Create a function that takes a users list and finds the max value.

def find_max_value(list):
    max = 0

    for i in range(0,len(list)):
        if (list[i] > max):
            max = list[i]
    return max

print(find_max_value([1,2,9,4,68,6,21,8,55.8]))