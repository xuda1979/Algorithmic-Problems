#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int n_strokes(string s, int start, int end){
    if (start > end)
        return 0;
    if (start == end)
        return 1;
    for(int i = end-1; i>=start; i--){
        if (s[i] == s[end])
            return n_strokes(s, start, end-1);
        if (s[i]<s[end])
            return 1+n_strokes(s, start, end-1);
        
    }

    return n_strokes(s, start, end-1) + 1;
    
}

int main(){
    string line;
    int line_n = 0;
    int N, Q, lb,ub;
    string str;
    vector<vector<int>> a;
    ifstream myfile("input");
    while(!myfile.eof()){
        getline(myfile, line);
        stringstream ss(line);

        if (line_n ==0){
            ss>>N>>Q;
        } else{
            if (line_n == 1)
                ss>>str;
            if (line_n >1 and line_n<=1+Q){
                vector<int> v;
                while(!ss.eof()){
                    ss>>lb>>ub;
                    v.push_back(lb);
                    v.push_back(ub);
                    a.push_back(v);
                }
            }

        }
        

        line_n++;

    }
    
    for(auto e:a)
        cout<<n_strokes(str,0, e[0]-1-1)+n_strokes(str, e[1], str.size()-1)<<'\n';
    return 0;
}

