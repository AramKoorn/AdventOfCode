using namespace std;
#include<bits/stdc++.h> 

int main() {

  string line;
  ifstream myfile ("inp_passport.txt");
  string full = "";
  char delim = ' ';
  unordered_map<string, string> mp;
  int res =  0;

  vector<string> req = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {

      stringstream ss(line);
      string token;
     
      while (getline(ss, token, delim)) {

        string k = "";
        string v = "";
        bool key = true;

        for (auto x:token) {

          if (x == ':') {
            key = false;
            continue;
          }
         
          if (key){
            k += x;
          }
          else
          {
            v += x;
          }
        }

        mp[k] = v;
      }
    
    // new person
    if (line == "") {

      cout << mp["hcl"] << endl;

      bool ok = true;
      
      // Check if all the required fields are available
      for (auto x: req) {
        if (mp.find(x) == mp.end()) {
          ok = false;
          break;
          }
      }

      // byr
      if (ok) {
      int byr = stoi(mp["byr"]);
      if (byr < 1920 || byr > 2002) {
        ok = false;
      } 

      //issue year
      int iyr = stoi(mp["iyr"]);
      if (iyr < 2010 || iyr > 2020) {
        ok = false;
        } 


      // expiration date
      int eyr = stoi(mp["eyr"]);
      if (eyr < 2020 || eyr > 2030) {
        ok = false;
        }

      //height
      string unit = "";
      bool cm = true;
      bool check = true;
      int hgt;
      for (auto x:mp["hgt"]) {
        if(x == 'c'){
          hgt = stoi(unit);
          check = false;
          break;
        }

        if(x == 'i'){
          hgt = stoi(unit);
          check = false;
          cm = false;
          break;
        }
        unit += x;
      }

      if (check) {
        ok = false;
      }

      if (cm) {
        if(hgt < 150 || hgt > 193) {
          ok = false;
        }
      }
      else {
        if (hgt <59 || hgt > 76) {
          ok = false;
        }
      }

      // hair color
      if ( mp["hcl"][0] != '#' || mp["hcl"].size() != 7) {
        ok = false;
      }

      // eye color
      vector<string> color = { "amb","blu", "brn", "gry", "grn", "hzl", "oth" }; 
      if (find(color.begin(), color.end(), mp["ecl"] ) == color.end()) {
        ok = false;
      }

      // pid
      if (mp["pid"].size() != 9 ) {
        ok = false;

      }
      else {
        for (auto x: mp["pid"]) {
          if (!isdigit(x)) {
            ok = false;
            break;
          }

        }
      }

      }


      
      if (ok) {
      res++;
      mp.clear();
      }
      else
      {
        mp.clear();
      }
    }
  }
    myfile.close();
    }
  cout << "\n";
  cout << "The answer is: " << res;
}
