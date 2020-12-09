#include <iostream>
#include <fstream>
#include <algorithm> 
#include <queue>
#define ll long long
#include <unordered_map>
using namespace std;

bool twoSum(ll target, vector<ll> data) {

	unordered_map<ll, ll> mp;

	for (auto x:data) {
		if(mp[x] )
		{
			return true;
		}
		else {
			ll missing = target - x;
			mp[missing] = target;
		}

	}
	return false;
}

int main()
{

    fstream file("day9inp.txt");
    string line;
    vector<ll> seq;

    // read in data 
    while ( getline(file, line)) {
	
	   seq.push_back(stol(line));
          }
        
    // problem 1
    for ( int i = seq.size() - 1; i >= 25; i--) {
	    ll target = seq[i];
	    
	    vector<ll> data;
	    for (int j = i - 1; j >= i - 25; j--) {
		    data.push_back(seq[j]);
	    }

	    if (!twoSum(seq[i], data)) {
		cout << target << endl;
		break;
		}	
	    data.clear();
    }

    // part 2
    ll target = 20874512; // copied from terminal
    for (int i = 0; i<seq.size(); i++) {
	    ll acc = 0;
	    vector<ll> tmp;
	    tmp.push_back(seq[i]);
	    acc += seq[i];
	    for ( int j = i + 1; j<seq.size(); j++) {
		    acc += seq[j];
		    tmp.push_back(seq[j]);

		    if ( acc == target) {
			    sort(tmp.begin(), tmp.end());
			    cout << tmp.front() + tmp.back();
			    break;

		    }
		    else if ( acc > target) {
			    tmp.clear();
			    break;
		    }
		    else
		    {
			    continue;
		    }

	    }
    }
}

