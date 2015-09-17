#include<iostream>

using namespace std;

void imprimeSolucao(int n, int tab[9][9]) {
  for (int i = 0; i < n*n; i++) {
    for (int j = 0; j < n*n; j++)
      cout << tab[i][j] << " ";
    cout << endl;
  }
}

int value(int n, int i, int j, int tab[9][9]) {
  int numbers[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int k, l;
  for (k = 0; k < n; k++) {
    for (l = 1; l < n; l++)
      if (!tab[k][l]){
	i = k;
	j = l;
	break;
      }
    if (i == k && j == l)
      break;
  }
  
  for (int k = 0; k < n*n; k++) {
    numbers[tab[i][k]] += 1;
    numbers[tab[k][j]] += 1;
  }
  for (int k = 1; k < n; k++) 
    for (int l = 1; l < n; l++)
    numbers[tab[k][l]] += 1;

  for (int k = 0; k < n*n; k++)
    if (!numbers[k]){
      tab[i][j] = k;
      if (value(n, 0, 0, tab))
	return 1;	
    }
  return 0;
}

int main() {
  int n;
  int sudoku[9][9];

  cin >> n;

  for (int i = 0; i < n*n; i++)
    for (int j = 0; j < n*n; j++)
      cin >> sudoku[i][j];

  
  if (value(n, 0, 0, sudoku))
     imprimeSolucao(n, sudoku);
  else
    cout << "NO SOLUTION" << endl;	
  
  return 0;
}
