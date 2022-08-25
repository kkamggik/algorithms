#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int n, k;
int dx[] = { 0,-1,0,1 };
int dy[] = { 1,0,-1,0 };
int arr[8][8];
int visited[8][8];
struct Node {
    int x, y, val;
};
queue<Node> q;
vector<Node> v;
int ans;
void dfs(int x, int y, int left) {
    ans = max(ans, visited[y][x]);
    int tx, ty;
    for (int i = 0; i < 4; i++) {
        tx = x + dx[i];
        ty = y + dy[i];
        if (tx < 0 || ty < 0 || tx >= n || ty >= n || visited[ty][tx]!=0) continue;
        if (arr[y][x] > arr[ty][tx]) {
            visited[ty][tx] = visited[y][x] + 1;
            dfs(tx, ty, left);
            visited[ty][tx] = 0;
        }
        if (arr[y][x] <= arr[ty][tx]) {
            if (left >= (arr[ty][tx] - arr[y][x] + 1)){      
                visited[ty][tx] = visited[y][x] + 1;
                int temp = arr[ty][tx];
                arr[ty][tx] = arr[y][x] - 1;
                dfs(tx, ty, 0);
                visited[ty][tx] = 0;
                arr[ty][tx] = temp;
            }
        }
    }
}
int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; t++) {
        cin >> n >> k;
        ans = 0;
        int m = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> arr[i][j];
                m = max(m, arr[i][j]);
                visited[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == m) {
                    visited[i][j] = 1;
                    dfs(j, i, k);
                    visited[i][j] = 0;
                }
            }
        }
        cout << "#" << t << " " << ans << endl;;
    }
}