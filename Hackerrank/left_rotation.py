def rotLeft(a, d):
    #d = number of rotations, a = array
    result = []
    index = d%len(a)
    while(len(result) < len(a)):
        if index == len(a):
            index = 0
        result.append(a[index])
        index += 1
    return result