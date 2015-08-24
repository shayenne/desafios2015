#include<stdio.h>
#include<math.h>
#include<string.h>

int main() {
  int W, D;
  int x0, y0;
  int x1, y1;
  int px, py;
  char seq[1005];

  int i, j, idi, idj, k, n;
  float length;

  i = 0;
  j = 0;
  idi = 0;
  idj = 0;
  n = 0;
  length = 0;

  scanf("%d %d", &W, &D);
  scanf("%d %d", &x0, &y0);
  scanf("%d %d", &x1, &y1);
  
  fgets(seq, sizeof(seq), stdin);
  printf("%s", seq);
  if (strcmp(seq, "\n")) {
    for (n = 0; seq[n] != '\n'; n++);
    for (k = 0; k < n; k++) {
      printf("Achei %c\n", seq[k]);
      if (seq[k] == 'F' || seq[k] == 'B') {
	if (j == 0 && seq[k] == 'B')
	  idj = -1;
	j++;
      }
      else {
	if (i == 0 && seq[k] == 'R')
	  idi = -1;
	i++;
      }
	
    }
  }

  if (idi != 0)
    i *= idi;

  if (idj != 0)
    j *= idj;

  printf("%d %d\n", i, j);
  /*
  px = floor(i+1/2)*2*W+pow(-1, i)*x0;
  py = floor(j+1/2)*2*D+pow(-1, j)*y0;
  */
  if (i % 2 == 0)
    px = i*W+x0;
  else
    px = (i+1)*W-x0;

  if (j % 2 == 0)
    py = j*D+y0;
  else
    py = (j+1)*D-y0;
  
  printf("%d %d\n", px, py);

  length = sqrt((px - x1)*(px - x1)+ (py - y1)*(py - y1));

  printf("%.4f\n", length);
  
  return 0;
}
