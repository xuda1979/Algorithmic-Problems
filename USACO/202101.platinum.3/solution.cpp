#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;


bool connected_neighbour(const vector<vector<char>>& a, const int& m, const int& n,  int i, int j, int i1, int j1){
    if (i1<0 or i1>=m)
        return false;
    if (j1<0 or j1>=n)
        return false;
    if (a[i][j] != a[i1][j1])
        return false;
    return true;

}

void get_component(const vector<vector<char>>& a, const int& m, const int& n,  const vector<int>& corners, int i, int j, set<pair<int, int>>& traveled){
    if (i<corners[0] or i >corners[2])
        return;
    if (j<corners[1] or j> corners[3])
        return;
    pair<int, int> point = make_pair(i,j);
    if (traveled.find(point) == traveled.end()) {
        traveled.insert(point);
        if(connected_neighbour(a,m,n,i,j,i+1,j))
            get_component(a,m,n,corners, i+1,j, traveled);
        if(connected_neighbour(a,m,n,i,j,i-1,j))
            get_component(a,m,n,corners, i-1,j, traveled);
        if(connected_neighbour(a,m,n,i,j,i,j+1))
            get_component(a,m,n,corners, i,j+1, traveled);
        if(connected_neighbour(a,m,n,i,j,i,j-1))
            get_component(a,m,n,corners, i,j-1, traveled);
       
    } 

} 


int total_component_n(const vector<vector<char>>& a, const int m, const int n, const vector<int>& corners){
    int  total = 0;
    set<pair<int,int>> traveled;
    for(int i=corners[0];i<=corners[2];i++)
        for(int j=corners[1];j<=corners[3];j++) {
            pair<int, int> point = make_pair(i,j);
            if (traveled.find(point) == traveled.end()){
                set<pair<int, int>> sub_traveled;
                get_component(a,m,n,corners,i,j, sub_traveled);
                traveled.insert(sub_traveled.begin(), sub_traveled.end());
                total++;
            }
        }



    return total;   

}

int main(){

    ifstream myfile("input");
    int line_n = 0;
    string line;
    int m,n,q;
    char c;
    int value;
    vector<vector<char>> a;
    vector<vector<int>> positions;
    while(!myfile.eof()){
        getline(myfile, line);
        stringstream ss(line);
        
        if (line_n==0)
            ss>>m>>n>>q;
        if(line_n >0 and line_n <= m){
            vector<char> v;
            while(!ss.eof()){
                ss>>c;
                v.push_back(c);
                
            }
            a.push_back(v);
        }
        if(line_n > m and line_n<=m+q){
            vector<int> v;
            while(!ss.eof()){
                ss>>value;
                v.push_back(value-1);
            }
            positions.push_back(v);
        }
        line_n++;
    }
    for(auto e:positions) {
        int total = total_component_n(a,m,n,e);
        cout<<total<<'\n';
    }
    
    return 0;
}
