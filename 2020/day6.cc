using namespace std;
#include<bits/stdc++.h> 

int findRow(double low, double high, string seq) {

  double mid;

  for ( auto i:seq) {

    /* cout << mid << endl; */
    /* cout << "low: " << low << " high: " << high << endl; */ 

    // lower half
    if (i == 'F' || i == 'L') {
       mid = floor((high + low) / 2);
       high = mid;
    }
    else {
      mid = ceil((high + low) / 2);
      low = mid;
  }
 }
  return mid;
}

int main() {

  string line;
  ifstream myfile ("inp_day.txt");
  vector<string> inp;

  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      
      inp.push_back(line);

    }
    myfile.close();
  }

  string test3 = "FBFBBFFRLR";

  cout << test3.substr(7, 3) << endl;

  string hoi = "BFFFBBFRRR"; 
  string test = "FFFBBBFRRR";
  string test2 = "BBFFBBFRLL";
  cout << "row: " << findRow(0, 127, test3) << "column: " << findRow(0, 7, test3.substr(7, 4 )) << endl;
  cout << "row: " << findRow(0, 127, hoi) << "column: " << findRow(0, 7, hoi.substr(7, 4 )) << endl;
  cout << "row: " << findRow(0, 127, test) << "column: " << findRow(0, 7, test.substr(7, 3 )) << endl;
  cout << "row: " << findRow(0, 127, test2) << "column: " << findRow(0, 7, test2.substr(7, 3 )) << endl;

  int mx = 0;
  vector<int> id;
  for (auto x:inp){
    int tmp = findRow(0, 127, x) * 8 + findRow(0, 7, x.substr(7, 3 ));
    id.push_back(tmp);
    mx = max(tmp, mx);

  }
  sort(id.begin(), id.end());  
  for (int i = 0; i<id.size() -1 ; i++) {
    if ( id[i+1] != id[i] + 1){

    cout << id[i] + 1 << endl;
    }
}
}
