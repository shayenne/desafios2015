/*
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P37 - 284D. Cow Program
 */

#include<bits/stdc++.h>

using namespace std;

static const long long int MAXX = 2e5 + 1;

typedef long long int vertex;

#define MAIS true
#define MENOS false

typedef struct node {
	vertex v;
	long long int cost;
	bool vis;
} node;

class iGraph {
public:
	long long int n;
	list<node> adj[MAXX][2];
	iGraph( long long int n) : n{ n } {};

	vector<long long int> bfs();
};

vector<long long int> iGraph::bfs() {
	vector<long long int> soma( n + 1, -1);
	vertex v = 0;
	queue<pair<vertex, list<node>::iterator> > qu[2];
	for (list<node>::iterator it = adj[v][MENOS].begin(); it != adj[v][MENOS].end(); it++) {
		if (!it->vis) {
			qu[MENOS].push( make_pair( v, it));
		}
	}
	for (list<node>::iterator it = adj[v][MAIS].begin(); it != adj[v][MAIS].end(); it++) {
		if (!it->vis) {
			qu[MAIS].push( make_pair( v, it));
		}
	}

	bool isPlus = MENOS;
	while (!qu[isPlus].empty() || !qu[!isPlus].empty()) {
		if (qu[isPlus].empty()) {
			isPlus = !isPlus;
		}
		v = qu[isPlus].front().first;
		list<node>::iterator itw = qu[isPlus].front().second;
		qu[isPlus].pop();
		itw->vis = true;
		for (list<node>::iterator it = adj[itw->v][!isPlus].begin(); it != adj[itw->v][!isPlus].end(); it++) {
			if (!it->vis) {
				it->cost += itw->cost;
				if (it->v == 1) {
					soma[itw->v] = it->cost;
				}
				else {
					qu[!isPlus].push( make_pair( itw->v, it));
				}
			}
		}
		isPlus = !isPlus;
	}
	return soma;
}


int main()
{
	long long int n;
	cin >> n;
	iGraph grafo( n);

	for (long long int i = 2; i <= n; i++) {
		long long int a, c;
		cin >> a;
		node v = { 1, i - 1, false };
		grafo.adj[i][MAIS].push_back( v);
		v = { i, a, 0 };
		c = i + a;
		if (c > n) {
			grafo.adj[0][MAIS].push_back( v);
		}
		else {
			grafo.adj[c][MAIS].push_back( v);
		}
		c = i - a;
		if (c <= 0) {
			grafo.adj[0][MENOS].push_back( v);
		}
		else {
			grafo.adj[c][MENOS].push_back( v);
		}
	}

	vector<long long int> soma = grafo.bfs();
	for (long long int i = 2; i <= n; i++) {
		cout << soma[i] << endl;
	}

	return 0;
}

