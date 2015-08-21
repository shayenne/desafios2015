/* Shayenne Moura */
#include<stdio.h>
#include<stdlib.h>

int main() {
  int *A;
  int i, min, max;
  int n, x;

  x = 0;
  min = 1000;
  max = 0;
  
  scanf("%d", &n);
   
  A = (int *) malloc (n * sizeof(int));
  
  for (i = 0; i < n; i++)
    scanf("%d", &A[i]);

  for (i = 0; i < n-1; i++){
    x = A[i+1]-A[i];
    if (x > max)
      max = x;

    if (i < n-2){
      x = A[i+2]-A[i];
      if (x < min){
	min = x;
      }
    }
  }
  
  if (min < max)
    min = max;

  printf("%d", min);

  free(A);

  return 0;
}
