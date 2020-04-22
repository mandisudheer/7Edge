
from collections import Counter
import operator

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count

l=[]


List = [2, 1, 2, 2, 1, 3,3,3,3,3,7,4,7,6,8,9,6,5,4,5,4,54]

result=most_frequent(List)

sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_x)

for i in sorted_x:
    for j in range(i[1]):
        l.append(i[0])

print(l)


# print(l)


