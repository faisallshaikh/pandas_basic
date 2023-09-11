

def high(val):
    list_of_high = []
    highest = 0
# # l.sort()
# # print(l)
# x = sorted(l)
# print(x[-2])
    
    for i in val:
        if i > highest:
            highest = i

            list_of_high.append(highest)
    return list_of_high


l = [12,10,9,8,15,16,19,95,20,25,78]
high(l)
