# The Good Ranges 
# https://www.hackerearth.com/problem/algorithm/the-good-ranges-1456e1a2-e908a292/


def getOutput (element):
    global query_count,global_sum,min_range,max_range,visited_elems
    if str(element) in visited_elems:
        return global_sum
    visited_elems[str(element)] = 1
    if (query_count == 1):
        global_sum += min_range + max_range
        min_range = element
        max_range = element
        query_count += 1
    else:
        if(X > max_range):
            global_sum += (element-1) + (max_range+1)
            max_range = element
        elif(X < min_range):
            global_sum += (element+1) + (min_range-1)
            min_range = element
        else:
            global_sum += (element+1) + (element-1)
    return global_sum



N, M = map(int, input().split())
query_count,global_sum,min_range,max_range = 1,0,N+1,0
visited_elems = dict()
 
while M > 0:
    X = int(input())
    out_ = getOutput(X)
    print (out_)
    M -= 1