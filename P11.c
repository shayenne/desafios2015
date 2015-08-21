/* Shayenne Moura */
#include<stdio.h>
#include<stdlib.h>

int main() {
  long **A, *s;
  int n, f;
  int i, j, k;
  long sum, val;
  long  x;
  
  scanf("%d", &n);

  s = (long *) malloc(n*sizeof(long));
  
  k = 0;

  while (k < n) {
    scanf("%d", &f);
    
    sum = 0;

    for (i = 0; i < f; i++) {
      for (j = 0, val = 1; j < 3; j++) {
	scanf("%d", &x);
	if (j != 1)
	  val *= x;
      }
      sum += val;
    }
    
    s[k] = sum;
    k++;
  }

  for (i = 0; i < n; i++){
    printf("%li\n", s[i]);
  }
  free(s);
  
  return 0;
}
