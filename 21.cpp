#include <iostream>
#include <vector>
using namespace std;

vector<int> __memo_sigma(10001);
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
    long sum = 0;
    for (int a = 2; a <= 10000; a++)
    {
        int b = sigma(a);
        if (b > 10000) continue;
        if (a != b && sigma(b) == a) sum += a;
    }
    cout << sum << endl;
    return 0;
}