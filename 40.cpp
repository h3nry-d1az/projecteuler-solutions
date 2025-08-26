#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define ll long long

vector<ll> __memo_c(20);
ll c(int n)
{
    if (ll m = __memo_c[n]; m) return m;
    if (n == 0) return 0;
    if (n == 1) return 9;
    ll r = 10*c(n-1) + pow(10, n) - 1;
    __memo_c[n] = r;
    return r;
}

vector<int> digits(ll n)
{
    vector<int> ds;
    ll k = n;
    while (k != 0)
    {
        int d = k % 10;
        ds.push_back(d);
        k = (k - d) / 10;
    }
    return ds;
}

int d(ll n)
{
    int m = 1;
    while (c(m) < n) m++;
    n = n - c(m - 1);
    int j = n/m - 1;
    int k = j + pow(10, m-1);
    return digits(k+1)[(m-1)-(n-m*(j+1)-1)];
}

int main()
{
    cout << 1 * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000) << endl;
    return 0;
}