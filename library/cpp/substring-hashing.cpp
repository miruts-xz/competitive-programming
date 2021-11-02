#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define MOD 1000000007
lli dp[1000001];
lli inv[1000001];

lli power(lli a, lli n){
    lli result = 1;
    while (n){
        if (n&1) result = (result*a)%MOD;
        n >>= 1;
        a = (a*a)%MOD;
    }
    return result;
}
void init(string input_string) {
    lli p = 31;
    lli p_power = 1;
    inv[0] = 1;
    dp[0] = (input_string[0]-'a'+1);
    for (int i = 1; i < input_string.size(); ++i) {
        char ch = input_string[i];
        p_power = (p_power*p)%MOD;
        inv[i] = power(p_power, MOD-2);
        dp[i] = (dp[i-1]+(ch-'a'+1)*p_power)%MOD;
    }
}
lli substring_hash(int l, int r) {
    int result = dp[r];
    if (l > 0) result -= dp[l-1];
    result = (result*inv[l])%MOD;
    return result;
}
int main() {
    init("miruts");
    cout << substring_hash(2,5) << endl;
}