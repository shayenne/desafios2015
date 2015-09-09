#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <queue>
#include <iomanip>   

using namespace std;
struct compare  
{  
  bool operator()(const int& l, const int& r)  
  {  
      return l > r;  
  }  
}; 


int main () {
  unsigned int n, i;
  unsigned int x;
  double med;
  priority_queue<unsigned int> pq;
  
  cin >> n;

  for (i = 0; i < n; i++) {
    cin >> x;

    pq.push(x);  
    if (pq.size() > (n/2)+1)
      pq.pop();

  }
    

  if (n % 2 != 0)
    med = pq.top();
  else {
    x = pq.top();
    pq.pop();
    med = (pq.top() + x)/2.0;
  }
  cout << setiosflags (ios::fixed) << setprecision(1) << med << endl;   

  return 0;
}
