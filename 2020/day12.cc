#include<fstream>
#include<iostream>
#include<vector>
using namespace std;


int main()
{


  fstream file("inp12.txt");
  string line;
  vector<pair<char, int>> dir;

  // read in data 
  while ( getline(file, line)) 
  {
    
    pair<char, int> foo;
    foo = make_pair(line[0], stoi(line.substr(1)));
    dir.push_back(foo);
    
  }

  cout << "first: " << dir[0].first;
}
