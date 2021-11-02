def get_winner(red, blue)->str:
    rc, bc = 0, 0
    for r, b in zip(red, blue):
        if int(r) > int(b):
            rc += 1
        elif int(r) < int(b):
            bc += 1
    return 'RED' if rc > bc else 'BLUE' if bc > rc else 'EQUAL'

if __name__ == "__main__":
    tests = []
    for _ in range(int(input())):
        input()
        red = input()
        blue = input()
        print(get_winner(red, blue))

