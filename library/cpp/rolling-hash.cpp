#include <bits/stdc++.h>
using namespace std;

long long int get_hash(string);
int main() {
    // Test code
    cout << get_hash("ruts") << endl;
}
/*
    Function calculates polynomial hash of a string of lowercase english letters
*/
long long int get_hash(string str) {
    int p = 31;
    int p_power = 1;
    long long int value = 0;
    for (char c : str) {
        value += (c-'a'+1)*p_power;
        p_power *= p;
    }
    return value;
}

