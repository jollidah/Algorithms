#include <iostream>

using namespace std;
int main() {
    int n, m, tmp = 0, res = 0;
    cin >> n >> m;
    for(int i = 0; i < n; i++)
    {
        int minValue = 1e9;     // declare minValue
        for (int j = 0; j < m; j++)
        {
         cin >> tmp;
        if (tmp < minValue)     // compare input with recent minValue
        {
            minValue = tmp;
        }
        }
        if (minValue > res)
        {
            res = minValue;
        }
    }
    cout << res;
}
