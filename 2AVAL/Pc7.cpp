#include<stdio.h>
#include<iostream>
#include<string.h>
#include<sstream>

using namespace std;

int main() {
  int n;
  char * pch, *codigo;
  string word, cifer;
  
  cin >> n;
  cout << n << endl;

  for (int i = 0; i < n; i++) {
    cin >> word;
    cout << word << endl;
  }

  while (scanf("%s", codigo)) {
      pch = strtok (codigo," ");
      while (pch != NULL) {
	cout << pch;
	pch = strtok (NULL, " ");
      }
      cout << codigo << endl;
  }
  
  return 0;
}
