#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

bool repeated_snap(const vector<vector<int>>& results, int start_minute, int end_minute){
    auto start = results[start_minute];
    auto end = results[end_minute];

    return equal(start.begin(), start.end(), end.begin());
}

bool repeated(int Q, const vector<vector<int>>& results){
    int size = results.size();
    for(int i=size-2; i>= 0; i--) {
        if ((size-1-i) % Q==0 and repeated_snap(results, i, size-1))
            return true;
    }
    return false;
}


void simulate_one_minute(int Q, const vector<vector<int>>& swaps, vector<vector<int>>& results){
    
    int size = results.size();
    int step = (size-1)%Q;
    vector<int> last = results[size-1];
 
    swap(last[swaps[step][0]], last[swaps[step][1]]);
    results.push_back(last);
}


void simulate(int Q, const vector<vector<int>>& swaps, vector<vector<int>>& results){
          
    while(!repeated(Q, results))
        simulate_one_minute(Q, swaps, results);

}




int main(){

    ifstream myfile("input");
    string str;
    int line_n = 0;
    int N, Q;
    string line;
    vector<vector<int>> swaps;
    while(!myfile.eof()){
        getline(myfile,line);
        stringstream ss(line);
        
        if(line_n==0){
            ss>>N>>Q;

        }
        if(line_n>0 and line_n  <=Q){
            vector<int> v;
            int a,b;
            ss>>a>>b;
            v.push_back(a-1);
            v.push_back(b-1);
            swaps.push_back(v);
        }   
        line_n++; 
    }
   
    vector<int> v;
    for (int i=0; i<N; i++)
        v.push_back(i);
    vector<vector<int>> results;
    results.push_back(v);

    
    simulate(Q, swaps, results);
       
    for (int i =0; i<N; i++){
        set<int> loop;
        for(auto e:results)
            loop.insert(find(e.begin(), e.end(),i)-e.begin());
        cout<<loop.size()<<'\n';   

    }
    
    return 0;
}
