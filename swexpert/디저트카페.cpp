#include <iostream>
using namespace std;
int n, sx, sy;
int arr[20][20];
int visited[20][20];
int dessert[101];
int dx[] = { 1,-1,-1,1 };
int dy[] = { 1,1,-1,-1 };
int ans;
 
void dfs(int x, int y, int d, int d1, int d2, int d3, int d4, int cnt) {
    if (x == sx && y == sy && d1==d3 && d2==d4 && cnt>=4) {
        if (cnt == 20) {
            int de = 1;
        }
        ans = max(ans, cnt);
        return;
    }
    int tx, ty, td;
    for (int i = 0; i < 2; i++) {
        td = (d + i) % 4;
        tx = x + dx[td];
        ty = y + dy[td];
        if (tx < 0 || ty < 0 || tx >= n || ty >= n || visited[ty][tx]!=0 || dessert[arr[ty][tx]]==1) continue;
        visited[ty][tx] = 1;
        dessert[arr[ty][tx]] = 1;
        if (td == 0) dfs(tx, ty, td, d1 + 1, d2, d3, d4, cnt + 1);
        else if (td == 1) dfs(tx, ty, td, d1, d2 + 1, d3, d4, cnt + 1);
        else if (td == 2 && d3+1 <= d1) dfs(tx, ty, td, d1, d2, d3 + 1, d4, cnt + 1);
        else if (td == 3 && d4+1 <= d2) dfs(tx, ty, td, d1, d2, d3, d4 + 1, cnt + 1);
        visited[ty][tx] = 0;
        dessert[arr[ty][tx]] = 0;
    }
}
int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; t++) {
        ans = 0;
        cin >> n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> arr[i][j];
                visited[i][j] = 0;
            }
        }
        for (int i = 0; i < 101; i++) dessert[i] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sx = j; sy = i; 
                dfs(j, i, 0, 0, 0, 0, 0, 0);
            }
        }
        if (ans == 0) ans = -1;
        cout << "#" << t <<  " " << ans << endl;
    }
}