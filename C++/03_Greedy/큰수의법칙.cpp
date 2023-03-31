#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    int n, m, k, tmp = 0, res = 0;
    cin >> n >> m >> k;
    int * data = new int[n];
    for(int i = 0; i < n; i ++)
    {
        cin >> tmp;
        data[i] = tmp;
    }
    sort(data, data + n);           
    if (m < k)
    {
        res = m * data[n - 1];
    }
    else
    {
        while (m > 0)
        {
            if (m  >  k)
            {
                res += k * data[n - 1] + data[n - 2];
                m -= k + 1;
            }
            else
            {
                res += m * data[n - 1];
                break;
            }
        }
    }
    cout << res;
}

//  sort(arr, arr+n);
//  sort(v.begin(), v.end());sort(v.begin(), v.end(), compare);     사용자 정의 함수 사용
//  sort(v.begin(), v.end(), greater<자료형>());               내림차순 (Descending order)
//  sort(v.begin(), v.end(), less<자료형>                      오름차순 (default = Ascending order)
