#include<iostream>

using namespace std;

int value(n, i, j, tab) {
  int numbers[10] = {0}*10;
  
  for (int k = 0; k < n*n; k++) {
    numbers[tab[i][k]] += 1;
    numbers[tab[k][j]] += 1;
  }
  for (int k = 1; k < n; k++) 
    for (int l = 1; l < n; l++)
    numbers[tab[k][l]] += 1;

  for (int k = 0; k < n; k++)
    if (!numbers[k])
      return k;
  return 0;
}

int main() {
  int n;
  int sudoku[9][9];

  cin >> n;

  for (int i = 0; i < n*n; i++)
    for (int j = 0; j < n*n; j++)
      cin >> sudoku[i][j];

  for (int i = 0; i < n*n; i++) {
    for (int j = 0; j < n*n; j++)
      if (!sudoku[i][j])
	if value(n, i, j, sudoku)
      cout << sudoku[i][j] << " ";
    cout << endl;
  }

  for (int i = 0; i < n*n; i++) {
    for (int j = 0; j < n*n; j++)
      cout << sudoku[i][j] << " ";
    cout << endl;
  }
  
  cout << n << endl;
  
  return 0;
}
