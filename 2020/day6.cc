using namespace std;
#include<bits/stdc++.h> 

int main() {
	
  string line;
  int res = 0;
  ifstream myfile ("inp_day6.txt");
  unordered_map<char, int> mp;
  int cnt = 0;

  
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
	cnt++;
	for (auto x:line) {
		mp[x]++;
	}	

	if(line == "") {

		for (auto it:mp) {
			if(it.second + 1 == cnt) {
				res++;
			}
		}

		mp.clear();
		cnt = 0;

	}

    }
    myfile.close();
  }
   cout << res;

}
