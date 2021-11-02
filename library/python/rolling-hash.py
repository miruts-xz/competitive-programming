
# Function calculates rolling hash of a string of lowercase english letters
def get_hash(string: str)->int:
    MOD, p, p_power, value = 10**9+7, 31, 1, 0
    for c in string:
        value = (value + (ord(c)-ord('a')+1)*p_power)%MOD
        p_power *= p
    return value
if __name__ == "__main__":
    print(get_hash('ab'))