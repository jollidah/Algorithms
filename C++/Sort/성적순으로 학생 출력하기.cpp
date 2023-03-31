#include <iostream>
#include <queue>
#include <utility>      // pair를 이용하기 위한 라이브러리
#include <string>
using namespace std;

struct cmp          // functor를 응용하는 것이 더 빠르다
{                   // 컴파일러에서 functor는 호출하지 않기 때문이다.
    bool operator()(pair<string, int> p1, pair<string, int> p2)
    {
        return p1.second > p2.second;
    }
};

int main() {
    priority_queue<pair<string, int>, vector<pair<string, int>>, cmp> pq;
    int numCases, intTmp;
    string stringTmp;
    cin >> numCases;
    for(int i = 0; i < numCases; i++)
    {
        cin >> stringTmp;
        cin >> intTmp;
        pq.push(make_pair(stringTmp, intTmp));      // emplace는 괜찮지만 push는 먼저 make_pair로 쌍을 만든 후에 push를 해야함
    }
    while(!pq.empty())
    {
        stringTmp = pq.top().first;
        cout << stringTmp << " ";
        pq.pop();
    }
}
