#include<bits/stdc++.h>

using namespace std;


int main() {
  int n;
  set<pair<float, float> > pts;
  
  cin >> n;
  
  for (int i = 0; i < n; i++) {
    pair<float,float> p;
    cin >> p.first >> p.second;
    pts.insert( p);
  }

  int grps = 0;
  for (set<pair<float, float> >::iterator p1 = pts.begin(); p1 != pts.end(); p1++) {
    set<pair<float,float>  >::iterator p2 = p1;
    for (p2++; p2 != pts.end(); p2++) {

      if (pts.find( make_pair( (p1->first + p2->first) / 2, (p1->second + p2->second) / 2)) != pts.end()) 
	grps++;	
      
      
    }
  }
  cout << grps << endl;
    
  return 0;
}
