#include <iostream>
#include <queue>
#include <vector>
using namespace std;
struct Node{
    int x,y;
};
vector<Node> virus;
int arr[8][8];
int used[8][8] = {0};
int n,m;
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};
int answer = 0;
void count(){
    queue<Node> q;
    int cnt[8][8];
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) cnt[i][j] = used[i][j];
    int x,y;
    for(int i=0; i<virus.size(); i++){
        x = virus[i].x;
        y = virus[i].y;
        q.push({x,y});
        cnt[y][x] = 1;
    }
    Node node;
    while(!q.empty()){
        node = q.front(); q.pop();
        for(int i=0; i<4; i++){
            x = node.x + dx[i];
            y = node.y + dy[i];
            if(x<0 || y<0 || x>=m || y>=n) continue;
            if(arr[y][x]==0 && cnt[y][x]==0 && used[y][x]!=1){
                cnt[y][x] = 1;
                q.push({x,y});
            }
        }
    }
    int c = 0;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(cnt[i][j]==0 && arr[i][j]!=1 && used[i][j]!=1)  c++;
    answer = max(answer, c);
}
void wall(int cnt){
    if(cnt == 3){
        count();
        return;
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(arr[i][j] == 0 && used[i][j]==0){
                used[i][j] = 1;
                wall(cnt+1);
                used[i][j] = 0;
            }
        }
    }
}
int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 2) virus.push_back({j,i});
        }
    }
    wall(0);
    cout << answer;
}