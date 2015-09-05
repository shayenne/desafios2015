#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <stack>

using namespace std;

struct node {
  char data;
  node *child[26];
  node() {
    for (int i = 0; i < 26; i++)
      child[i] = NULL;
  }
};

class trie {
private:
  node *root;
public:
  trie() {
    root = new_node(0);
  }

  node *new_node(int data) {
    node *X = new node;
    X->data = data;
    return X;
  }

  bool add(string S) {
    bool new = FALSE;
    node *cur = root;
    for (int i = 0; i < S.length(); i++) {
      if (!cur->child[S[i]-'a']) {
        cur->child[S[i]-'a'] = new_node(S[i]);
        if (i == S.length()-1)
          new = TRUE
      }
      cur = cur->child[S[i]-'a'];
    }
    return new;
  }

  int check(node *cur, string S, int i) {
    if (cur) {
      cout << cur->data;
      if (i < S.length())
	return check(cur->child[S[i]-'a'], S, i+1);
    }
    return i-1;
  }

  int checkroot(string S) {
    if (root && S.length() > 0 && S[0] >= 'a')
      return check(root->child[S[0]-'a'], S, 1);
    else
      cout << "\nEmpty root\n";
  }
};
  
static const long int MAX = 75000;

int main() {
	trie t;
	string cipher;
	int cnt;

	getline(cin, cipher);

	cout << cipher << endl;

	cnt = 0;
	for (int i = 0; i < cipher.length(); i++) {
		for (int j = 0; j < cipher.length()+1; j++) {
			cout << cipher.substr(i, j) << endl;
			if (t.add(cipher.substr(i, j)))
				cnt++;
		}
	}

	cout << cnt << endl;
  return 0;
}
