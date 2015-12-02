#include<bits/stdc++.h>

using namespace std;

int main() {
  int n, x, y, v;
  vector<int> a (200005, 0), states (200005, 0);
  bool cycle;
  
  cin >> n;

  for (int i = 2; i <= n; i++) {
    cin >> a[i];
  }


  for (int i = 1; i < n; i++) {
    cycle = false;

    for (int j = 0; j < n; j++)
      states[j] = 0;
    
    states[0] = 1;
    states[1] = i + 1;

    x = i + 1;
    y = i;

    a[1] = x;

    for (int j = 1; j < n; j++) {
      v = a[x];

      if (j % 2 != 0)
	x -= v;
      else
	x += v;

      y += v;

      if (x <= 0 || x > n)
	break;

      for (int k = 0; k < n; k++) {
	if (states[k] == x) {
	  cout << -1 << endl;
	  cycle = true;
	  break;
	}

	if (k == n-1)
	  for (int l = 0; l < n; l++)
	    if (states[l] == 0) {
	      states[l] = x;
	      break;
	    }
      }
      if (cycle)
	break;
    }
    if (!cycle)
      cout << y << endl; 
    
  }
  
  return 0;
}
