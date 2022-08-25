#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
int arr[10][10];
int visited[10][10] = {0};
int n,m;
int parent[7];
struct Node{
    int x, y;
};
struct Dist{
    int d1, d2, d;
};
bool cmp(Dist dist1, Dist dist2){
    return dist1.d < dist2.d;
}
vector<Dist> v;
int dx[] = {0,-1,0,1};
int dy[] = {1,0,-1,0};
int find(int x){
    if(parent[x] == x) return x;
    parent[x] = find(parent[x]);
    return parent[x];
}
void Union(int x, int y){
    x = find(x);
    y = find(y);
    if(x>y) parent[x] = y;
    else parent[y] = x;
}
void dfs(int x, int y, int d, int curr){
    if(arr[y][x]!=curr && arr[y][x]!=0){
        if(visited[y][x]-2 >= 2) v.push_back({curr, arr[y][x],visited[y][x]-2});
        return;
    }
    int tx = x+dx[d], ty = y+dy[d];
    if(tx<0 || ty<0 || ty>=n || tx>=m || visited[ty][tx]!=0 || arr[ty][tx]==curr){
        // nothing happens
    }else{
        visited[ty][tx] = visited[y][x] + 1;
        dfs(tx,ty,d,curr);
        visited[ty][tx] = 0;
    }
}
void bfs(int x, int y, int idx){
    queue<Node> q;
    arr[y][x] = idx;
    visited[y][x] = 1;
    q.push({x,y});
    Node node;
    int tx, ty;
    while(!q.empty()){
        node = q.front(); q.pop();
        for(int i=0; i<4; i++){
            tx = node.x + dx[i];
            ty = node.y + dy[i];
            if(tx<0 || ty<0 || tx>=m || ty>=n || visited[ty][tx]!=0 || arr[ty][tx]!=1) continue;
            visited[ty][tx] = 1;
            arr[ty][tx] = idx;
            q.push({tx,ty});
        }
    }

}
int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> arr[i][j];
    int idx = 1;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(arr[i][j]==1 && visited[i][j]==0){
                bfs(j,i,idx);
                idx++;
            }
        }
    }
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) visited[i][j] = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(arr[i][j]!=0){
                visited[i][j] = 1;
                for(int d=0; d<4; d++) dfs(j,i,d,arr[i][j]);
                visited[i][j] = 0;
            }
        }
    }
    for(int i=1; i<=7; i++) parent[i] = i;
    sort(v.begin(), v.end(), cmp);
    int rst=0, a, b;
    for(int i=0; i<v.size(); i++){
        a = v[i].d1; b = v[i].d2;
        if(find(a)!=find(b)){
            Union(a,b);
            rst += v[i].d;
        }
    }
    int first = find(parent[1]);
    for(int i=2; i<idx; i++)
        if(find(parent[i])!=first) rst = -1;
    cout << rst;
}