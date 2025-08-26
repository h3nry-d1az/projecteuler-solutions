#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define ll long long

vector<int> digits(int n)
{
    vector<int> ds;
    int k = n;
    while (k != 0)
    {
        int d = k % 10;
        ds.push_back(d);
        k = (k - d) / 10;
    }
    return ds;
}

int main()
{
    ll sum = 0ll;
    for (int i = 10; i < 1e7; i++)
    {
        int s = 0;
        for (auto d : digits(i)) s += pow(d, 5);
        if (s == i) sum += i;
    }

    cout << sum << endl;

    return 0;
}