l = [5,8,1,3,2]

still_swaping = True

while still_swaping:
    still_swaping = False
    for i in range(len(l) - 1):
        print(l)
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            still_swaping = True
    