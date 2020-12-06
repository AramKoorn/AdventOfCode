using namespace std;
#include<bits/stdc++.h> 

int findTree(vector<vector<char>> mat, int right, int down) {

  int idx = -1;
  int res = 0;
  int start = down;

  for (int i = start; i<mat.size(); i+=down ) {

    idx += right;

      if ( idx > mat[i].size() -1 ) {
        idx -= mat[i].size();
      }
    int toCheck;
    if (idx == mat[i].size() - 1) {
      toCheck = 0;
    }
    else
    {
      toCheck = idx + 1;
    }

    if (mat[i][toCheck] == '#') {
      res++;
    }

  }
  return res;
}

int main() {


  string line;
  ifstream myfile ("inp_day3.txt");
  vector<vector<char>> mat;

  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      /* cout << line << '\n'; */
      vector<char> tmp;
      for (auto x:line) {
        tmp.push_back(x);
      }

      mat.push_back(tmp);
    }
    myfile.close();
  }


  // test if reading the data worked 
  for (int i = 0; i<mat.size(); i++) {
    for (int j = 0; j<mat[i].size(); j++) {
      cout << mat[i][j];
    }
    cout << endl;
  }

  // actually do the puzzle
  int idx = -1;
  int res = 0;

  for (int i = 1; i<mat.size(); i++ ) {

    idx += 3;

      if ( idx > mat[i].size() -1 ) {
        idx -= mat[i].size();
      }
    int toCheck;
    if (idx == mat[i].size() - 1) {
      toCheck = 0;
    }
    else
    {
      toCheck = idx + 1;
    }

    if (mat[i][toCheck] == '#') {
      res++;
    }

  }

  cout << "The answer  is: " << res;  
  int test = findTree(mat, 3, 1);
  cout << "The answer  is: " << findTree(mat, 1, 1) * findTree(mat, 3, 1) * findTree(mat, 5, 1) * findTree(mat, 7, 1) * findTree(mat, 1, 2);  
  


}

