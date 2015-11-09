#include<iostream>
#include<utility>
#include<stdio.h>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int n;
  int x, y;
  pair <int, int> p, ymenor;
  vector <pair <float, pair <int, int> > > q (10000);
    
  cin >> n;

  ymenor = make_pair (0,0);

  for (int i = 0; i < n; i++) {
    cin >> x >> y;
    p = make_pair (x, y);
    q[i] = make_pair (0, p);
    if (y < ymenor.second)
      ymenor = make_pair (x, y);
  }

  /* Ordenar os pontos de acordo com o angulo do menor*/

  for (int i = 0; i < n/2; i++) {
    cout << q[i].first << " " << q[i].second.first << endl;
  }
  
  return 0;
}
