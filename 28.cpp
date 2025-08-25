#include <iostream>
using namespace std;

#define ll long long

int main()
{
    ll sum = 1;
    for (int i = 1; i <= (1001-1)/2; i++)
    {
        int l = 2*i;
        int s = (l+1)*(l+1);
        sum += s + (s-l) + (s-2*l) + (s-3*l); 
    }

    cout << sum << endl;
    return 0;
}