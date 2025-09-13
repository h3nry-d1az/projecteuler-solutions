#include <cassert>
#include <iostream>
#include <set>
#include <cmath>
using namespace std;

int main()
{
  set<set<int>> solutions = {};
  size_t max_solutions = 0;
  int max_p = 0;

  for (int p = 12; p <= 1000; p += 2)
  {
    if (solutions.size() >= max_solutions)
    {
      max_solutions = solutions.size();
      max_p = p-2;
    }
    solutions = {};
    for (int a = 1; a <= p/2; a++)
    {
      if ( (2*a*p - p*p) % (2*a - 2*p) != 0 ) continue;
      int b = (2*a*p - p*p) / (2*a - 2*p);
      double c = sqrt(a*a+b*b);
      if (!(c - (int)c < 1e-6)) continue;
      solutions.insert({a, b, (int)c});
    }
    continue;
  }

  cout << max_p << endl;
  return 0;
}
