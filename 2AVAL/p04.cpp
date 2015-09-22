/*

Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P3 - 989. Su Doku

*/
#include<iostream>
#include<string>
#include<sstream>

using namespace std;

void imprimeSolucao(int n, int tab[][9]) {
  for (int i = 0; i < n*n; i++) {
    for (int j = 0; j < n*n-1; j++)
      cout << tab[i][j] << " ";
    cout << tab[i][n*n-1];
    cout << endl;
  }
}

int value(int n, int i, int j, int tab[][9], int qtd) {
  int numbers[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int k, l, r, s;
  r = -1;
  s = -1;
  k = i;
  l = j;
  while (k < n*n) {
    while (l < n*n) {
      if (!tab[k][l]){
	r = k;
	s = l;
	break;
      }
      l++;
    }
    if (r == k && s == l)
      break;
    l = 0;
    k++;
  }
  
  for (int k = 0; k < n*n; k++) {
    numbers[tab[r][k]] += 1;
    numbers[tab[k][s]] += 1;
  }
  
  for (int k = (r/n)*n; k < ((r/n)*n)+n; k++) 
    for (int l = (s/n)*n; l < ((s/n)*n)+n; l++)
      numbers[tab[k][l]] += 1;


  for (int k = 1; k < n*n+1; k++)
    if (!numbers[k]){
      tab[r][s] = k;
      qtd += 1;
      
      if (qtd == n*n*n*n)
	return 1;
      if (value(n, r, s, tab, qtd))
	return 1;
      else
	tab[r][s] = 0;
	qtd -= 1;
    }

  return 0;
}

int main() {
  string entry;
  int n;
  int sudoku[9][9];
  int qtd;

  cin >> n;
  qtd = 0;
  
  for (int i = 0; i < n*n; i++)
    for (int j = 0; j < n*n; j++) {
      cin >> sudoku[i][j];
      if (sudoku[i][j])
	qtd +=1 ;
    }
  
  if (qtd == n*n*n*n)
    imprimeSolucao(n, sudoku);
  else {
    if (value(n, 0, 0, sudoku, qtd))
      imprimeSolucao(n, sudoku);
    else
      cout << "NO SOLUTION" << endl;
  }
  
  while (cin >> n) {
    qtd = 0;
    
    for (int i = 0; i < n*n; i++)
      for (int j = 0; j < n*n; j++) {
	cin >> sudoku[i][j];
	if (sudoku[i][j])
	  qtd +=1 ;
      }
    cout << endl;
    if (qtd == n*n*n*n)
      imprimeSolucao(n, sudoku);
    else {
      if (value(n, 0, 0, sudoku, qtd))
	imprimeSolucao(n, sudoku);
      else
	cout << "NO SOLUTION" << endl;
    }
    
  }
  return 0;
}
