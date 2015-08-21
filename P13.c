/* Shayenne Moura */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void acrescenta(char soma[], int dig, int j){
  char c = '0';
  int new;
 
  if (dig < 10) {
    c += dig;
    soma[j] = c;
  }
  else {
    c += dig % 10;
    soma[j] = c;
    new = 1 + soma[j-1] - '0';
    c = '0';
    while (new > 9) {
      soma[j-1] = c + (new % 10);
      j--;
      new = 1 + soma[j-1] - '0';
      c = '0';
    }
    soma[j-1] += 1;
  }
    
}

int main() {
  int i, j, qtd, dig, cnt;
  char soma[102];
  char x[105];

  for (i = 0; i < 102; i++)
    soma[i] = '0';

  fgets(x, sizeof(x), stdin);
  while (strcmp(x, "0\n")) {
    for (i = strlen(x)-2, j = 101; i >= 0; i--, j--) {
      dig = x[i] + soma[j] - '0' - '0';
      acrescenta(soma, dig, j);
    }
    fgets(x, sizeof(x), stdin);
  }

  cnt = 0;
  while (cnt < 102 && soma[cnt] == '0')
    cnt++;
  for (i = cnt; i < 102; i++)
    printf("%c", soma[i]);
  printf("\n");
  
  return(0);
}


