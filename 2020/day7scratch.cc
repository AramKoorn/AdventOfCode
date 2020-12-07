#include <iostream>
#include <fstream>
#include <regex>
#include <map>
#include <set>
#include <queue>

using namespace std;

int main()
{
    regex rx1("(\\S+ \\S+) bags contain (.+)\\.");
    regex rx2("(\\d+) (\\S+ \\S+) bag[s]?[, ]?");
    smatch match1, match2;

    fstream file("input.txt");
    string line;

    map<string, vector<string>> contains;
    map<string, vector<pair<int, string>>> isContainedBy;

    while (getline(file, line)) {
        if (regex_search(line, match1, rx1)) {
            string container = match1[1];
            string contentsList = match1[2];
            while (regex_search(contentsList, match2, rx2)) {
                int num = atoi(string(match2[1]).data());
                string contained = match2[2];
                contains[contained].push_back(container);
                isContainedBy[container].push_back({num, contained});
                contentsList.erase(0, string(match2[0]).size());
            }
        }
    }

    ////////////
    // part 1 //
    ////////////

    queue<string> Q;
    set<string> examined;
    for (auto x : contains["shiny gold"]) {
        Q.push(x);
        examined.insert(x);
    }
    while (!Q.empty()) {
        for (auto x : contains[Q.front()]) {
            if (examined.insert(x).second) {
                Q.push(x);
            }
        }
        Q.pop();
    }
    cout << examined.size() << endl;

    ////////////
    // part 2 //
    ////////////

    int total = 0;
    queue<pair<int, string> > Q2;
    for (auto x : isContainedBy["shiny gold"]) {
        Q2.push(x);
    }
    while (!Q2.empty()) {
        for (auto x : isContainedBy[Q2.front().second]) {
            Q2.push({Q2.front().first * x.first, x.second});
        }
        total += Q2.front().first;
        Q2.pop();
    }
    cout << total << endl;

    return 0;
}
