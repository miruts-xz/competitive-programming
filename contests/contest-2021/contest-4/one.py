n = int(input())
count = 0
while n:
    n = abs(n)
    string = str(n)
    size = len(string)
    below = '1'*size
    above = '1'*(size+1)
    n1 = int(below)-n
    n2 = int(above)-n
    if abs(n1) > abs(n2)+1:
        count += size+1
        n = n2
    else:
        n = n1
        count += size
print(count)
        


