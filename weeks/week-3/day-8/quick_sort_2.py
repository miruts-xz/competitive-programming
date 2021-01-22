# Enter your code here. Read input from STDIN. Print output to STDOUT


def partition(arr):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = []
    equal = []
    right = []
    for a in arr:
        if a < p:
            left.append(a)
        elif a > p:
            right.append(a)
        else:
            equal.append(a)
    left = partition(left)
    right = partition(right)
    result = left + equal + right
    print(' '.join(map(str, result)))
    return left + equal + right


if __name__ == '__main__':
    n = int(input())
    input_arr = list(map(int, input().rstrip().split()))
    partition(input_arr)
