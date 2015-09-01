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

  void add(string S) {
    node *cur = root;
    for (int i = 0; i < S.length(); i++) {
      if (!cur->child[S[i]-'a'])
	cur->child[S[i]-'a'] = new_node(S[i]);
      cur = cur->child[S[i]-'a'];
    }
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
  string vista, ultima;
  int x = 0;
  int count = 0;

  getline(cin, vista);
  getline(cin, ultima);

  cout << vista << endl;
  cout << ultima << endl;
  
  t.add(vista);
  x = t.checkroot(ultima);
  
  while (x > 0 && ultima.length() > 0) {
    count++;
    pos = ultima.find(vista[0]);
    subs = ultima.substr(pos, ultima.length());
    y = t.checkroot(sub);
    if (y <= 1 && ultima.length() == 1)
      ultima = subs;
  }


  cout << x;
  return 0;
}
