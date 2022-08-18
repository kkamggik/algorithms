#include <iostream>
#include <queue>
using namespace std;
struct Node { 
	int x,y,idx;
};
bool operator<(Node t1, Node t2){
if (t1.idx > t2.idx) return true;
if (t1.idx < t2.idx) return false;
}
priority_queue<Node> t;
int main(){
	int n;
  	cin >> n;
  	int arr[n][n];
  	for(int i=0; i<n; i++){
    	for(int j=0; j<n; j++){
        	cin >> arr[i][j];
          	t.push({j,i,arr[i][j]});
        }
    }
  	int visited[n][n] = {0};
  	int dx[4] = {1,0,-1,0};
  	int dy[4] = {0,-1,0,1};
  	Node node;
  	int rst = 0, x, y;
  	while(!t.empty()){
    	node = t.top(); t.pop();
      	if(visited[node.y][node.x]!=0) continue;
      	rst = max(rst, node.idx);
      	visited[node.y][node.x] = 1;
      	for(int i=0; i<4; i++){
        	x = node.x + dx[i];
          	y = node.y + dy[i];
          	if(x<0 || x>=n || y<0 || y>=n) continue;
          	visited[y][x] = 1;
        }  	
    }
  	cout << rst << "초";
}