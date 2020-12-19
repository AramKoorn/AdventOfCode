#include<fstream>
#include <unistd.h>
#include<array>
#include<tuple>
#include<vector>
#include<iostream>
using namespace std;

int countOcc(int i, int j, vector<vector<char>> mat) 
{

  int cnt = 0;
  int row = i;
  int col = j;

  // left direction
  row = i;
  col = j -1;
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      col--;
    }
  }

  row = i;
  col = j + 1;
  // right direction
  while (mat[row][col] != 'O') {
    //cout << "row: " << row << " col: " << col << endl;
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      col++;
    }
  }
  
  row = i + 1;
  col = j;
  // top direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row++;
    }
  }
  
  row = i - 1;
  col = j;
  // down direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row--;
    }
  }
  
  row = i + 1;
  col = j + 1;
  // diagonal up direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row++;
      col++;
    }
  }
  
  row = i - 1;
  col = j - 1;
  // diagonal down direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row--;
      col--;
    }
  }
  
  row = i - 1;
  col = j + 1;
  // left up direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row--;
      col++;
    }
  }
  
  row = i + 1;
  col = j - 1;
  // right down direction
  while (mat[row][col] != 'O') {
    if (mat[row][col] == '#') {
      cnt++;
      break;
    }
    else if ( mat[row][col] == 'L')
    {
      break;
    }
    else 
    { 
      row++;
      col--;
    }
  }
  return cnt;
}

void update(vector<vector<char>> &mat)
{

  vector<pair<int, int>> updL;
  vector<pair<int, int>> updSeat;
  int cnt;

  for (int i = 0; i<mat.size(); i++) {
    for (int j =0; j<mat[0].size(); j++) {

      // we know its outer ring
      if (mat[i][j] == 'O' || mat[i][j] == '.'){
        continue;
      }

      // its an empty seat
      else if ( mat[i][j] == 'L' )
      {
        cnt = countOcc(i, j, mat);
        if (cnt == 0)
        {
          pair<int, int> foo;
          foo = make_pair(i, j);
          updL.push_back(foo);
        }
      }

      // it is an occupied seat
      else
        {
          
          cnt = countOcc(i, j, mat);
          //cout << cnt << endl;
          if (cnt >= 5)
          {
          pair<int, int> foo;
          foo = make_pair(i, j);
          updSeat.push_back(foo);
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
  
  //// create last layer
  vector<char> tmp (mat.size() + 2, 'O');
  mat.push_back(tmp);

  //for (int i = 0; i< 5; i++) {
    //update(mat);

  //for (int i = 0; i<mat.size(); i++) {
    //for (int j = 0; j<mat[0].size(); j++) {
      //cout << mat[i][j];
    //}
    //cout << endl;
  //}
  //}

  // print
  bool ok = true;
  while (ok) 
  {
  
  //print
  for (int i = 0; i<mat.size(); i++) {
    for (int j = 0; j<mat[0].size(); j++) {
      cout << mat[i][j];
    }
    cout << endl;
  }

  vector<vector<char>> old = mat;
  update(mat);


  if (old == mat) {
    ok = false;
  }

}
  int cnt = 0; 
  // get answer
  for (int i = 0; i<mat.size(); i++) {
    for (int j = 0; j<mat[0].size(); j++) {
      if (mat[i][j] == '#') {
        cnt++;
      }
    }
  }
    cout << "N seats: " << cnt <<  endl;
}
