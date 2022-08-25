#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int k, m, n;
int arr[15][12];
int ans;
int dx[] = { 0,-1,0,1 };
int dy[] = { 1,0,-1,0 };
struct Node {
    int x, y, val;
};
queue<Node> q;
void dfs(int cnt) {
    if (cnt <= k) {
        int c = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) if (arr[i][j] != 0) c++;
        ans = min(ans, c);
        if (cnt == k) return;
    }
    Node node;
    int x, y;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[j][i] != 0) {
                int temp[15][12];
                for (int a = 0; a < n; a++)
                    for (int b = 0; b < m; b++) temp[a][b] = arr[a][b];
                q.push({ i,j,arr[j][i]});
                arr[j][i] = 0;
                while (!q.empty()) {
                    node = q.front(); q.pop();
                    for (int a = 0; a < 4; a++) {
                        for (int b = 0; b < node.val; b++) {
                            x = node.x + dx[a] * b;
                            y = node.y + dy[a] * b;
                            if (x < 0 || y < 0 || x >= m || y >= n || arr[y][x] == 0) continue;
                            q.push({ x,y,arr[y][x]});
                            arr[y][x] = 0;
                        }
                    }
                }
                vector<int> v;
                for (int a = 0; a < m; a++) {
                    for (int b = 0; b < n; b++)
                        if (arr[b][a] != 0) v.push_back(arr[b][a]);
                    for (int b = n - 1; b >= 0; b--) {
                        if (v.empty()) arr[b][a] = 0;
                        else {
                            arr[b][a] = v.back();
                            v.pop_back();
                        }
                    }
                }
                dfs(cnt + 1);
                for (int a = 0; a < n; a++)
                    for (int b = 0; b < m; b++) arr[a][b] = temp[a][b];
                break;
            }
        }
    }
}
int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; t++) {
        ans = 2e9;
        cin >> k >> m >> n;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) cin >> arr[i][j];
        dfs(0);
        cout << "#" << t << " " << ans << endl;
    }
}