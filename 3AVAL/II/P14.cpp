#include<bits/stdc++.h>


using namespace std;

void printGraph(map<pair<char, int>, list<pair<char, int> > >& graph) {
  for (auto i: graph) {
    //list<pair<char, int> >::iterator it = graph[i].begin();

    //if (it != graph[i].end()) { 
    //cout << i.second << " :" << endl;
      
      for (auto j: i) 
      	cout << ' ' << j.second;
      
      cout << '\n';
    }
  }
}

int main() {
  int t, n, m;
  vector<int> A (101), B (101);
  map<pair<char, int>, list<pair<char, int> > > graph; 
  
  cin >> t;

  for (int i = 0; i < t; i++) {
    cin >> n;

    for (int j = 1; j <= n; j++) {
      cin >> A[j]; 
    }

    cin >> m;

    for (int j = 1; j <= m; j++) {
      cin >> B[j]; 
    }

    for (int j = 1; j <= n; j++) {
      for (int k = 1; k <= m; k++) {
	if (B[k] % A[j] == 0) {
	  graph[make_pair('A', A[j])].push_back(make_pair('B', B[k]));
	  graph[make_pair('B', B[k])].push_back(make_pair('A', A[j]));
	}
      }
    }
    //printGraph(graph);
  }
  
  return 0;
}
