#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <sys/types.h>
#include <vector>
using namespace std;

set<vector<uint8_t>> permutations(vector<uint8_t> a)
{
    if (a.size() == 1)
        return {a};
    set<vector<uint8_t>> ps;
    for (auto ai : a)
    {
        if (a.size() == 10 && ai == 0)
            continue;
        vector<uint8_t> ap = a;
        ap.erase(find(ap.begin(), ap.end(), ai));
        for (auto p : permutations(ap))
        {
            p.insert(p.begin(), ai);
            ps.insert(p);
        }
    }
    return ps;
}

uint32_t construct(vector<uint8_t> n)
{
    uint32_t num = 0;
    uint32_t l = n.size();
    for (uint32_t i = 1; i <= l; i++)
        num += n[i - 1] * pow(10, l - i);
    return num;
}

int main()
{
    set<uint32_t> solutions;
    uint64_t sum = 0ll;
    for (auto p : permutations({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}))
    {
        if ((construct({p[1], p[2], p[3]}) % 2 == 0) && (construct({p[2], p[3], p[4]}) % 3 == 0) &&
            (construct({p[3], p[4], p[5]}) % 5 == 0) && (construct({p[4], p[5], p[6]}) % 7 == 0) &&
            (construct({p[5], p[6], p[7]}) % 11 == 0) && (construct({p[6], p[7], p[8]}) % 13 == 0) &&
            (construct({p[7], p[8], p[9]}) % 17 == 0))
        {
            solutions.insert(construct({p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]}));
        }
    }
    for (auto s : solutions)
    {
        sum += s;
    }
    cout << sum << endl;
    return 0;
}
