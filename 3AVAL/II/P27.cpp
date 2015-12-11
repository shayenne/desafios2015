/*
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P27 - 14D. Two Paths
 */
#include<bits/stdc++.h>

using namespace std;

#define MAXN 201

int lvr[MAXN];
int qtd[MAXN];
int grafo[MAXN][MAXN];

int dfsBigPath(vector<list<int> >& graph, int v, int ini) {
    int maxv = -1;

    if (v != ini && qtd[v] <= 1)
        return 0;

    lvr[v] = 1;

    for (auto w : graph[v])
        if (lvr[w] == 0 && grafo[v][w] == 1) {
            int maxw = dfsBigPath(graph, w, ini);
            if (maxw != -1 && maxv < 1 + maxw)
                maxv = 1 + maxw;
        }

    lvr[v] = 0;
    return maxv;
}

void verticesLivres(vector<list<int> >& graph, int v, int ini, list<int>& livres) {
    if (v != ini && qtd[v] <= 1) {
        livres.push_back(v);
        return;
    }
    lvr[v] = 1;
    for (auto w : graph[v])
        if (lvr[w] == 0 && grafo[v][w] == 1)
            verticesLivres(graph, w, ini, livres);

    lvr[v] = 0;
}

int bigPath(vector<list<int> >& graph, int v) {
    memset( lvr, 0, graph.size() * sizeof (int));
    int big = 0;
    list<int> livres;
    verticesLivres(graph, v, v, livres);
    for (auto l : livres) {
        memset( lvr, 0, graph.size() * sizeof (int));
        int path = dfsBigPath(graph, l, l);
        if (path > big)
            big = path;
    }
    return big;
}

int main() {
    int n;
    cin >> n;
    memset(lvr, 0, (n+1) * sizeof (int));
    memset(qtd, 0, (n+1) * sizeof (int));
    vector<list<int> > graph(n+1, list<int>());
    int arestas[MAXN][MAXN];
    for (int i = 0; i < n+1; i++) {
        memset(grafo[i], 0, (n+1) * sizeof (int));
        memset(grafo[i], 0, (n+1) * sizeof (int));
    }
    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
        grafo[a][b] = 1;
        grafo[b][a] = 1;
        qtd[a]++;
        qtd[b]++;
    }
    int maior = 0;
    for (int v = 1; v <= n; v++) {
        for (auto w : graph[v]) {
            if (arestas[v][w] != 1) {
                arestas[v][w] = 1;
                arestas[w][v] = 1;
                qtd[v]--;
                qtd[w]--;
                grafo[v][w] = 0;
                grafo[w][v] = 0;
                int v1 = bigPath(graph, v);
                int v2 = bigPath(graph, w);
                v1 *= v2;
                if (v1 > maior)
                    maior = v1;
                qtd[v]++;
                qtd[w]++;
                grafo[v][w] = 1;
                grafo[w][v] = 1;
            }
        }
    }
    cout << maior << endl;
    return 0;
}
