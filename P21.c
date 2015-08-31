/* Shayenne Moura*/
#include<stdio.h>
#include<math.h>
#include<string.h>

int main() {
  int W, D;
  int x0, y0;
  int x1, y1;
  long long px, py;
  char seq[1005], x, buffer[20];

  int i, j, idi, idj, k, n;
  double length;

  i = 0;
  j = 0;
  idi = 0;
  idj = 0;
  n = 0;
  length = 0;
  seq[0] = '\0';

  /*
  fgets(buffer, sizeof(buffer), stdin);
  sscanf(buffer, "%d %d", &W, &D);
  fgets(buffer, sizeof(buffer), stdin);
  sscanf(buffer, "%d %d", &x0, &y0);
  fgets(buffer, sizeof(buffer), stdin);
  sscanf(buffer, "%d %d", &x1, &y1);
  fgets(seq, sizeof(seq), stdin);
  
  */
  scanf("%d %d", &W, &D);
  scanf("%d %d", &x0, &y0);
  scanf("%d %d", &x1, &y1);
  scanf("%s", seq);
  


  if (strcmp(seq, "\0")) {
    for (n = 0; n < 1000 && seq[n] != '\0'; n++);
    for (k = 0; k < n; k++) {
<<<<<<< HEAD
      if (seq[k] == 'F' || seq[k] == 'B') {
	if (j == 0 && seq[k] == 'B')
	  idj = -1;
	j++;
      }
      else {
      	if (seq[k] == 'L' || seq[k] == 'R') {
	  if (i == 0 && seq[k] == 'R')
	    idi = -1;
	  i++;
	}
=======
      
      if (seq[k] == 'F' || seq[k] == 'B') {
	if (seq[k] == 'F')
	  idj = -1;
	else
	  idj = 1;
	j++;
      }
      else {
      	if (seq[k] == 'L' || seq[k] == 'R')
	  if (seq[k] == 'L')
	    idi = -1;
	  else
	    idi = 1;
	i++;
>>>>>>> 9f427832df8a610cb5708da03b3334bb8a418ddd
      }
      
    }
  }
  

  if (idi != 0)
    i *= idi;

  if (idj != 0)
    j *= idj;

  if (i % 2 == 0)
    px = i*W+x0;
  else
    px = (i+1)*W-x0;

  if (j % 2 == 0)
    py = j*D+y0;
  else
    py = (j+1)*D-y0;
  
  length = sqrt((long long)(px - x1)*(px - x1)+(long long)(py - y1)*(py - y1));

  printf("%.4f\n", length);
  
  return 0;
}
