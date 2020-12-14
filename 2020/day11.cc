#include<fstream>
#include <unistd.h>
#include<array>
#include<tuple>
#include<vector>
#include<iostream>
using namespace std;

void update(vector<vector<char>> &mat)
{

  vector<pair<int, int>> updL;
  vector<pair<int, int>> updSeat;
  vector<pair<int, int>> offset { 
  { 0,  1}, { 0, -1}, { 1,  0}, {-1,  0}, { 1,  1}, {-1, -1}, { 1, -1}, {-1,  1}
  };

  for (int i = 0; i<mat.size(); i++) {
    for (int j =0; j<mat[0].size(); j++) {

      // we know its outer ring
      if (mat[i][j] == 'O' || mat[i][j] == '.'){
        continue;
      }

      // its an empty or occupied seat
      else if ( mat[i][j] == 'L' )
      {
        bool ok = true;
          for (auto x:offset) 
          {
            if ( mat[x.first + i][x.second + j] == '#' )
            {
              ok =false;
              break;
            }
          }
          if (ok) {
            pair<int, int> foo;
            foo = make_pair(i, j);
            updL.push_back(foo);
          }

          }
        else
        {
          int cnt = 0;
          for (auto x:offset) 
          {
            if ( mat[x.first + i][x.second + j] == '#' )
            {
              cnt++;
              if ( cnt >= 4) 
              {
                pair<int, int> foo;
                cnt = 0;
                foo = make_pair(i, j);
                updSeat.push_back(foo);
                break;
              }
            }
          }
        }
      }
    }
  
  // update the matrix
  for (auto x: updL) 
  {
    mat[x.first][x.second] = '#';
  }

  for (auto x: updSeat) 
  {
    mat[x.first][x.second] = 'L';
  }
  cout << endl;

}





int main()
{

  // read
  fstream file("inp11.txt");
  string line;
  vector<vector<char>> mat;
  int i = 0;

  // read in data 
  while ( getline(file, line)) 
  {
      vector<char> tmp (line.size() + 2, 'O');

      if (i == 0) 
      {
        mat.push_back(tmp);
        i++;
      }

      for (int i = 0; i<line.size(); i++) 
      {
        tmp[i + 1] = line[i];
      }
      mat.push_back(tmp);
  }
  
  // create last layer
  vector<char> tmp (mat.size() + 2, 'O');
  mat.push_back(tmp);

  // print
  for (int i = 0; i<mat.size(); i++) {
    for (int j =0; j<mat[0].size(); j++) {
      cout << mat[i][j];
    }
    cout << endl;
  }
 
  //for(int i = 0; i<50; i++) {
  //update(mat);

   //print
  //for (int i = 0; i<mat.size(); i++) {
    //for (int j =0; j<mat[0].size(); j++) {
      //cout << mat[i][j];
    //}
    //cout << endl;
  //}
  //}

  // print
  bool ok = true;
  int cnt = 0;
  while (ok) {
  vector<vector<char>> old = mat;
  update(mat);

  if (old == mat) {
    ok = false;

  }

  
  // print
  for (int i = 0; i<mat.size(); i++) {
    for (int j =0; j<mat[0].size(); j++) {
      cout << mat[i][j];
    }
    cout << endl;
  }
  }
  
  for (int i = 0; i<mat.size(); i++) {
    for (int j =0; j<mat[0].size(); j++) {
      if ( mat[i][j] == '#'){
        cnt++;
      }
    }
    cout << endl;
  }
  cout << cnt;


  // print
}
