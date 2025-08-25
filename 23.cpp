#include <iostream>
#include <vector>
#include <unordered_set>
#include <cstdint>
using namespace std;

#define ll long long

vector<int> __memo_sigma(INT16_MAX);
int sigma(int n)
{
    if (int m = __memo_sigma[n]; m) return m;
    if (n <= 1) return 0;

    int sum = 0;
    for (int i = 1; i < n; i++) if (n % i == 0) sum += i;
    __memo_sigma[n] = sum;
    return sum;
}

int main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    unordered_set<int> abundant;
    for (int n = 2; n <= 28123; n++) if (sigma(n) > n) abundant.insert(n);

    unordered_set<int> valid;
    ll sum = 0;
    for (int n = 1; n <= 28123; n++)
    {
        bool invalid = false;
        for (auto e = abundant.begin(); e != abundant.end(); e++)
        {
            if (abundant.find(n - *e) != abundant.end())
            {
                invalid = true;
                break;
            }
        }
        if (!invalid) {sum += n; valid.insert(n);}
    }

    cout << sum << endl;

    return 0;
}