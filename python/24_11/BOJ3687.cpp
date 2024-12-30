#include <bits/stdc++.h>
using namespace std;

int arr[1001][1001];
int psum[1001][1001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;


	//좌표 압축 
	vector<pair<int, int> > v;
	set<int> s_x;
	set<int> s_y;
	map<int, int> m_x;
	map<int, int> m_y;

	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		v.push_back({ x,y });
		s_x.insert(x);
		s_y.insert(y);
	}

	int idx = 1;

	for (auto i : s_x) {
		m_x[i] = idx++;
	}

	idx = 1;

	for (auto i : s_y) {
		m_y[i] = idx++;
	}


	for (int i = 0; i < n; i++) {
		arr[m_x[v[i].first]][m_y[v[i].second]] = 1;
	}



	//사분면 누적합 구하기 
	int ans = INT_MAX;


	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++) {
			psum[i + 1][j + 1] = psum[i + 1][j] + psum[i][j + 1] - psum[i][j] + arr[i+1][j+1];
		}
	}


	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++) {

			int a = psum[i][j];
			int b = psum[i][1000] - a;
			int c = psum[1000][j] - a;
			int d = psum[1000][1000] - a - b - c;

			ans = min(ans, max({ a, b, c, d }));
		}
	}
	cout << ans << '\n';

	return 0;
}