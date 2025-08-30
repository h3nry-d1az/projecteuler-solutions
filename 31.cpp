#include <iostream>
#include <set>
#include <map>
#include <bitset>
using namespace std;

bitset<200> __memo_computed;
map<int, set<multiset<int>>> __memo_combinations;
set<multiset<int>> compute_combinations(int n)
{
    if (n == 0) return {{}};
    if (__memo_computed[n-1]) return __memo_combinations[n];

    set<multiset<int>> combinations;
    if (n == 200) combinations.insert({200});
    
    for (auto k : {1, 2, 5, 10, 20, 50, 100})
    {
        if (k > n) continue;
        set<multiset<int>> new_combinations = compute_combinations(n-k);
        for (auto e : new_combinations)
        {
            e.insert(k);
            combinations.insert(e);
        }
    }

    __memo_computed[n-1] = true;
    __memo_combinations[n] = combinations;
    return combinations;
}

int main()
{
    cout << compute_combinations(200).size() << endl;
    return 0;
}