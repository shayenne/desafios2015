#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <queue>
#include <iomanip>   
#include <algorithm>
#include <vector>


int main () {
  unsigned int n, i;
  unsigned int x;
  double med;

  int v[250000/2+3];

  i = 0;

  cin >> n;
   for(; i < n/2+1; ++i) cin >> v[i];
   make_heap(v,v+n/2+1);
   for(; i < n; ++i){
     cin >> v[n/2+1];
     push_heap(v,v+n/2+2);
     pop_heap(v,v+n/2+2);
   }
    

  if (n % 2 != 0)
    med = v.back();
  else {
    x = v.back();
    v.pop_back();
    med = (v.back()*0.5 + x*0.5);
  }
  cout << setiosflags (ios::fixed) << setprecision(1) << med << endl;   

  return 0;
}
