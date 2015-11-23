/*
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P2 - 1647. Divide an Island!
 */
#include<iostream>
#include<math.h>
#include<stdio.h>

using namespace std;

int main() {
  double x1, y1, x2, y2, x3, y3;
  double A, B, C, tmp;
  double P, soma, prod, area, delta;
  int resp = 0;
  double r1, r2, s1, s2, p, q, k, l;
  
  cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

  A = sqrt ((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
  B = sqrt ((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
  C = sqrt ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));

  P = A + B + C;

  soma = P/2;

  //area = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y2))/2;
  area = sqrt (soma*(soma-A)*(soma-B)*(soma-C));
  
  for (int i = 0; i < 3 && resp == 0; i++) {
    
    prod = A * B / 2;
    
    delta = soma*soma - 4*prod;
    if (fabs(delta) <= 1e-10)
      delta = 0;
    
    if (delta >= 0) {
      r1 = (soma + sqrt(delta))/2;
      r2 = (soma - sqrt(delta))/2;

      s1 = soma - r1;
      s2 = soma - r2;
      
      if (r1 <= B+1e-10 && s1 <= A+1e-10) {
	p = x3 + (r1/B) * (x1-x3);
	q = y3 + (r1/B) * (y1-y3);
	k = x3 + (s1/A) * (x2-x3);
	l = y3 + (s1/A) * (y2-y3);
	resp = 1;
      }
      else if (r2 <= B+1e-10 && s2 <= A+1e-10) {
	p = x3 + (r2/B) * (x1-x3);
	q = y3 + (r2/B) * (y1-y3);
	k = x3 + (s2/A) * (x2-x3);
	l = y3 + (s2/A) * (y2-y3);
	resp = 1;
      }
      
    }
    tmp = A;
    A = B;
    B = C;
    C = tmp;
    tmp = x1;
    x1 = x2;
    x2 = x3;
    x3 = tmp;
    tmp = y1;
    y1 = y2;
    y2 = y3;
    y3 = tmp;
  }

  if (! resp) {
    cout << "NO";
    return 0;
  }

  printf("YES\n%.15lf %.15lf\n%.15lf %.15lf\n", p, q, k, l);

  return 0;
}
