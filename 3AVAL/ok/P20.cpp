/*
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P20 - 189B - Counting Rhombi
 */

#include<iostream>

using namespace std;

int main() {
  int w, h, i, j;
  long long resp = 0;
  
  cin >> w >> h;

  i = j = 2;
  while (i <= w) {
    j = 2;
    while (j <= h) {
      resp += (w - i + 1)*(h - j + 1);
      j += 2;
    }
    i += 2;
  }

  cout << resp << endl;
  
  
  return 0;
}
