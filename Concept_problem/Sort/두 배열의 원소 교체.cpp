#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;


int main() {
    int length, switchCnt, tmp;
    cin >> length;
    cin >> switchCnt;
    int * l1 = new int [length];
    int * l2 = new int [length];
    for (int i = 0; i < length; i++)
    {
        cin >> tmp;
        l1[i] = tmp;
    }
    for (int i = 0; i < length; i++)
    {
        cin >> tmp;
        l2[i] = tmp;
    }
    sort(l2, l2 + length, greater<int>());  // 내림차순
    sort(l1, l1 + length, less<int>());     // 오름차순(default)

    for (int p = 0; p < length; p++)
    {
        if (l2[p] > l1[p] && switchCnt > 0)
        {
            swap(l2[p], l1[p]);
            switchCnt --;
        }
        else
        {
            break;
        }
    }
    cout << accumulate(l1, l1 + length, 0);     //리스트 합계 std::accumulate 와 부분합 std::partial_sum 기억
}
