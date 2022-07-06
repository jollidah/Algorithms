#include <iostream>
#include <queue>

using namespace std;
int main() {
    priority_queue<int> pq;
    int numCases, tmp;
    cin >> numCases;
    for(int i = 0; i < numCases; i++)
    {
        cin >> tmp;
        pq.push(tmp);
    }
    while(!pq.empty())
    {
        cout << pq.top() << " ";
        pq.pop();
    }
}

# 우선순위큐를 이용해 쉽게 해결할 수 있다.
