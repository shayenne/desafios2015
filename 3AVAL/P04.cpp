#include<iostream>
#include<vector>

typedef struct operacao{
  int op;
  int l;
  int r;
  int v;
} operacao;

using namespace std;

int main() {
  int n, m;
  vector<operacao> op(5005);
  vector<long> array(5005, 1e9), diff(5005, 0);
  int right;
  operacao novo;
  
  cin >> n >> m;

  for (int i = 0; i < m; i++) {
    cin >> novo.op >> novo.l >> novo.r >> novo.v;
    op[i] = novo;

    if (novo.op == 1) 
      for (int j = (novo.l)-1; j < novo.r; j++) 
	diff[j] += novo.v;
    else {
      right = 0;
      for (int j = (novo.l)-1; j < novo.r; j++)
	if (array[j] >= novo.v - diff[j]) {
	  array[j] = novo.v - diff[j];
	  right = 1;
	}
      if (!right) {
	cout << "NO" << endl;
	return 0;
      }
    }
  }

  vector<long> test(array);

  for (int i = 0; i < m; i++) {
    if (op[i].op == 1) {
      for (int j = (op[i].l)-1; j < op[i].r; j++)
	test[j] += op[i].v;
    }
    else {
      right = 0;
      for (int j = (op[i].l)-1; j < op[i].r; j++) {
	if (test[j] > op[i].v) {
	  cout << "NO" << endl;
	  return 0;
	}
	else if (test[j] == op[i].v)
	  right = 1;
      }
      if (!right) {
	cout << "NO" << endl;
	return 0;
      }
	
    }
  }
  
  cout << "YES" << endl;
  for (int i = 0; i < n; i++)
    cout << array[i] << " ";
  
  return 0;
}
