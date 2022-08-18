#include <iostream>
using namespace std;
int n,m;
int arr[501][501];
int visited[501][501] = {0};
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int ans = 0;
void tetromino(int x, int y, int cnt, int score){
    if(cnt==4){
        ans = max(ans, score);
        return;
    }
    int nx, ny;
    for(int i=0; i<4; i++){
        nx = x + dx[i];
        ny = y + dy[i];
        if(nx<0 || ny<0 || nx>=m || ny>=n || visited[ny][nx]==1) continue;
        visited[ny][nx] = 1;
        tetromino(nx, ny, cnt+1, score+arr[ny][nx]);
        visited[ny][nx] = 0;
    }
}
int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) cin >> arr[i][j];
    int t;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            visited[i][j] = 1;
            tetromino(j,i,1,arr[i][j]);
            visited[i][j] = 0;
            if(j+2 < m){
                t = arr[i][j] + arr[i][j+1] + arr[i][j+2];
                if(i-1 >= 0) ans = max(ans, t+arr[i-1][j+1]);
                if(i+1 < n) ans = max(ans, t+arr[i+1][j+1]);
            }
            if(i+2<n){
                t = arr[i][j] + arr[i+1][j] + arr[i+2][j];
                if(j-1 >= 0) ans = max(ans, t+arr[i+1][j-1]);
                if(j+1 < m) ans = max(ans, t+arr[i+1][j+1]);
            }
        }
    }
    cout << ans;
}