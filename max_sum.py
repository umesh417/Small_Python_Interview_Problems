
def most_frequent(list):
    count = []
    max_count = 0
    max_item = None

    for i in list:
        if i not in count:
            count[i] = 1

        else:
            count[i]+=1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item

print(most_frequent([1,3,4,5,3,2,1,1,3,4,1,3,4,3]))
