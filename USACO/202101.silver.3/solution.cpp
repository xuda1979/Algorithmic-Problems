#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int largest = -1;
vector<vector<int>> a;


int beauty(int N, const vector<vector<int>> board, const vector<vector<int>> a){
    int total = 0; 
    for(int i = 0; i< N; i++)
        for(int j = 0; j < N; j++)
            total += board[i][j]*a[i][j];
    return total;
}


bool valid(int N, vector<vector<int>>& board, int i, int j, int value){
    if (value >1 or value<0)
        return false;
    if (i>0){
        if (j>0 and (value+board[i][j-1]+board[i-1][j-1]+board[i-1][j] !=2))
            return false;
        if (j<N-1 and (value+board[i-1][j]+board[i-1][j+1] >2))
            return false;
        
    }
    return true;
}




void find_largest(int N, vector<vector<int>>& board, int i, int j) {
    if (i>=N) {
        largest = max(largest, beauty(N, board,a));
        return;
    }
    if (valid(N, board, i, j, 1)){
        if (j<N-1){
            board[i][j] = 1;
            find_largest(N, board, i, j+1);
            board[i][j] = 0;
        }
        if (j == N-1){
            board[i][j] = 1;
            find_largest(N, board, i+1, 0);
            board[i][j] = 0;
        }
        
    }
    if (valid(N, board, i, j, 0)){
        if (j<N-1){
        
            find_largest(N, board, i, j+1);
        }
        if (j == N-1){
            find_largest(N, board, i+1, 0);
        }
    }
}

int main(){
    ifstream myfile ("input");
    string line;
    int value;
    int N;
    int line_n = 0;
    while(!myfile.eof()){
        getline(myfile, line);
        stringstream ss(line);
        if (line_n == 0)
            ss>>N;
        if (line_n >0){
            vector<int> v;
        
	while(!ss.eof()){
	    ss>>value;
            v.push_back(value);
	       
	}
            a.push_back(v);
        }


        line_n++;
	
    }
    vector<vector<int>> board(N, vector<int>(N,0));
    
    find_largest(N, board, 0, 0);
    cout<< largest<<'\n';
   
    return 0;
}
