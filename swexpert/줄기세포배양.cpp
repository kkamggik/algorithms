#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int n, m, k;
int arr[1000][1000];
int dx[] = { 0,1,0,-1 };
int dy[] = { 1,0,-1,0 };
struct Node {
	int x, y, time, life;
};
struct cmp {
    bool operator()(Node n1, Node n2){
        return arr[n1.y][n1.x] < arr[n2.y][n2.x];
    }
};
int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> n >> m >> k;
		for (int i = 0; i < 1000; i++) {
			for (int j = 0; j < 1000; j++) {
				arr[i][j] = 0;
			}
		}
        vector<Node> v;
		for (int i = 500; i < 500 + n; i++) {
			for (int j = 500; j < 500 + m; j++) {
				cin >> arr[i][j];
				if (arr[i][j] != 0) {
					v.push_back({ j,i,arr[i][j],arr[i][j]});
				}
			}
		}
        Node node;
        int x, y,cnt=0;
        priority_queue<Node, vector<Node>, cmp> q;
		while (k > 0) {
            k--;
            for(int i=0; i < v.size(); i++){
                v[i].time--;
                if(v[i].time == -1) q.push({v[i]});
                if(v[i].time == -v[i].life ) arr[v[i].y][v[i].x] = -1;
            }
            while(!q.empty()){
                node = q.top(); q.pop();
                for (int i = 0; i < 4; i++) {
					x = node.x + dx[i];
					y = node.y + dy[i];
					if (x < 0 || y < 0 || x >= 1000 || y >= 1000 || arr[y][x] != 0) continue;
                    arr[y][x] = node.life;
                    v.push_back({x, y, arr[y][x], arr[y][x]});
				}
            }
		}
        for (int i = 0; i < 1000; i++) 
			for (int j = 0; j < 1000; j++) 
				if(arr[i][j]>0) cnt++;
		cout << "#" << t  << " " <<  cnt << endl;
	}
}