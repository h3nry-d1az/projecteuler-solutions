#include <iostream>
#include <unordered_set>
#include <cmath>
using namespace std;

unordered_set<int>
digit_permutations(unordered_set<int> digits)
{
  if (digits.size() == 1) return digits;
  unordered_set<int> ps;
  for (auto d : digits)
  {
    unordered_set<int> new_digits = {};
    for (auto e : digits)
    {
      if (e == d) continue;
      new_digits.insert(e);
    }
    int D = d*pow(10, new_digits.size());
    unordered_set<int> new_ps = digit_permutations(new_digits);
    for (auto p : new_ps) ps.insert(D+p);
  }
  return ps;
}

unordered_set<int> pandigitals(char d)
{
  unordered_set<int> digits;
  for (char i = 1; i <= d; i++) digits.insert(i);
  return digit_permutations(digits);
}

bool is_prime(int n)
{
  if ((n & 1) == 0) return false;
  for (int k = 3; k <= (int)sqrt(n); k++) if (n % k == 0) return false;
  return true;
}

int main()
{
  int largest_pandigital_prime = 0;
  for (char n = 3; n <= 9; n++)
  {
    unordered_set<int> ps = pandigitals(n);
    for (auto p : ps)
    {
      if (is_prime(p))
        largest_pandigital_prime = max(largest_pandigital_prime, p);
    }
  }
  cout << largest_pandigital_prime << endl;
  return 0;
}
