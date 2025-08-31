#include <iostream>
#include <bitset>
#include <vector>
#include <unordered_set>
#include <cmath>
using namespace std;

typedef long long ll;

vector<char> digits(ll n)
{
    vector<char> d;
    while (n != 0)
    {
        d.push_back(n % 10);
        n /= 10ll;
    }
    return d;
}

bitset<2147483648> __memo_computed;
bitset<2147483648> __memo_value; // Allocated 0.25 GB of space for memoization.
bool is_prime(int n)
{
    if (n <= 1) return false;
    if (n < 2147483648)
    {
        if (__memo_computed[n-1]) return __memo_value[n-1];
        __memo_computed[n-1] = true;
    }
    for (int i = 2; i <= (int)sqrt(n); i++)
    {
        if (n % i == 0)
        {
            if (n < 2147483648) __memo_value[n-1] = false;
            return false;
        }
    }
    if (n < 2147483648) __memo_value[n-1] = true;
    return true;
}

bool truncatable(ll n)
{
    vector<char> ds = digits(n);
    for (auto d : ds) if (d & 1 == 0) return false;
    ll nleft = n-((ll)(n/pow(10, ds.size()-1)))*pow(10, ds.size()-1);
    ll nright = n/10;
    while (nright > 0)
    {
        if (!is_prime(nright)) return false;
        nright /= 10;
    }
    while (nleft > 0)
    {
        if (!is_prime(nleft)) return false;
        nleft -= ((ll)(nleft/pow(10, (ll)log10(nleft))))*pow(10, (ll)log10(nleft));
    }
    return true;
}

int main()
{
    unordered_set<ll> nums;
    ll sum = 0ll;
    char count = 0;
    for (ll n = 11;;n++)
    {
        if (!is_prime(n)) continue;
        if (truncatable(n))
        {
            sum += n;
            nums.insert(n);
            count++;
            if (count == 11) break;
        }
    }

    cout << sum << endl;
    return 0;
}