MOD = 10**9+7
dp, inv = [0]*100001, [0]*1000001
# Function calculates modular inverse a number
def power(a: int, n: int)-> int:
    result = 1
    while n:
        if n&1: result = (result*a)%MOD
        n >>= 1
        a = (a*a)%MOD
    return result
def init(string: str):
    p, p_power = 31, 1
    dp[0] = ord(string[0])-ord('a')+1
    inv[0] = 1
    for i in range(1, len(string)):
        chr = string[i]
        p_power = (p_power*p)%MOD
        inv[i] = power(p_power, MOD-2)
        dp[i] = (dp[i-1]+(ord(chr)-ord('a')+1)*p_power)%MOD
def substring_hash(l: int, r: int)->int:
    result = dp[r]
    if l > 0: result -= dp[l-1]
    result = (result*inv[l])%MOD
    return result
if __name__ == "__main__":
    init('miruts')
    print(substring_hash(2, 5))

