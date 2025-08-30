#include <iostream>
#include <bitset>
#include <tuple>
#include <cmath>
using namespace std;

bitset<2001000> __memo_computed;
bitset<2001000> __memo_value;
bool is_prime(int n)
{
    if (n <= 1) return false;
    if (__memo_computed[n-1]) return __memo_value[n-1];
    __memo_computed[n-1] = true;
    for (int i = 2; i <= (int)sqrt(n); i++)
    {
        if (n % i == 0)
        {
            __memo_value[n-1] = false;
            return false;
        }
    }
    __memo_value[n-1] = true;
    return true;
}

int main()
{
    tuple<int, int> maximum = {0, 0};
    for (int b = 2; b <= 1000; b++)
    {
        if (!is_prime(b)) continue;
        for (int a = -999; a < 1000; a++)
        {
            int n = 1;
            while (is_prime(n*n + a*n + b)) n++;
            if (n > get<0>(maximum)) maximum = {n, a*b};
        }
    }

    cout << get<1>(maximum) << endl;
    return 0;
}