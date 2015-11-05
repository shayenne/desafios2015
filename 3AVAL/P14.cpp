#include<iostream>
#include<sstream>
#include<vector>

using namespace std;

int main() {
  int T;
  int n, m;
  int tmp;
  vector < int > A(105), B(105); 

  cin >> T;
  
  for (int i = 0; i < T; i++) {
    cin >> n;
    for (int j = 0; j < n; j++) { 
      cin >> A[j];
    }
    

    cin >> m;
    for (int j = 0; j < m; j++) {
      cin >> B[j];
    
    }
  }
 
  return 0;
}
