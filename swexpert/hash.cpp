#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using  namespace std;
unordered_map<int, vector<string>> candidates;
unordered_map<string, vector<int>> whois;

int main(){
    int n;
    cin >> n;
    int id;
    string state, name;
    for(int i=0; i<n; i++){
        cin >> state;
        if(state == "recommand"){
            cin >> id >> name;
            if(candidates.find(id)==candidates.end()) candidates[id] = vector<string>();
            candidates[id].push_back(name);
            if(whois.find(name)==whois.end()) whois[name] = vector<int>();
            whois[name].push_back(id);
            cout << candidates[id].size() << endl;
        }else if(state == "print"){
            cin >> id;
            if(candidates.find(id)==candidates.end()) cout << "none" << endl;
            else{
                for(int i=0; i < candidates[id].size(); i++){
                    cout << candidates[id][i] << " ";
                }
                cout <<  endl;
            }
        }else if(state == "whois"){
            cin >> name;
            if(whois.find(name)==whois.end()) cout << "none" << endl;else{
                vector<int> v;
                for(int i=0; i < whois[name].size(); i++){
                    v.push_back(whois[name][i]);
                }
                sort(v.begin(), v.end());
                for(int i=0 ;i<v.size(); i++) cout << v[i] << " ";
                cout << endl;
            }
        
        }
    }
}