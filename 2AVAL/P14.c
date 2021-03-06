#include<stdio.h>

/* Vértices de digrafos são representados por objetos do tipo Vertex. */

#define Vertex int

/* REPRESENTAÇÃO POR LISTAS DE ADJACÊNCIA: A estrutura digraph representa um digrafo. O campo adj é um ponteiro para o vetor de listas de adjacência, o campo V contém o número de vértices e o campo A contém o número de arcos. */

struct digraph {
   int V; 
   int A; 
   link *adj; 
};
/* Um objeto do tipo Digraph contém o endereço de um digraph. */

typedef struct digraph *Digraph;
/* A lista de adjacência de um vértice v é composta por nós do tipo node. Cada nó da lista corresponde a um arco e contém um vizinho w de v e o endereço do nó seguinte da lista. Um link é um ponteiro para um node. */

typedef struct node *link;
struct node { 
   Vertex w; 
   link next; 
};
/* A função NEWnode recebe um vértice w e o endereço next de um nó e devolve o endereço a de um novo nó tal que a->w == w e a->next == next. */

link NEWnode( Vertex w, link next) { 
   link a = malloc( sizeof (struct node));
   a->w = w; 
   a->next = next;     
   return a;                         
}

/* REPRESENTAÇÃO POR LISTAS DE ADJACÊNCIA: A função DIGRAPHinit devolve (o endereço de) um novo digrafo com vértices 0 1 ... V-1 e nenhum arco. */

Digraph DIGRAPHinit( int V) { 
   Vertex v;
   Digraph G = malloc( sizeof *G);
   G->V = V; 
   G->A = 0;
   G->adj = malloc( V * sizeof (link));
   for (v = 0; v < V; v++) 
      G->adj[v] = NULL;
   return G;
}
/* REPRESENTAÇÃO POR LISTAS DE ADJACÊNCIA: A função DIGRAPHinsetA insere um arco v-w no digrafo G.  A função supõe que v e w são distintos, positivos, e menores que G->V. Se o digrafo já tem arco v-w, a função não faz nada. */

void DIGRAPHinsertA( Digraph G, Vertex v, Vertex w) { 
   link a;
   for (a = G->adj[v]; a != NULL; a = a->next) 
      if (a->w == w) return;
   G->adj[v] = NEWnode( w, G->adj[v]);
   G->A++;
}

/* A função UFfind devolve o chefe de v (ou seja, o chefe da árvore que contém v na floresta geradora mst[0..k-1]).  A função UFunion recebe dois chefes distintos x e y e faz a união das correspondentes árvores. */

static Vertex ch[maxV];
static int sz[maxV];

void UFinit( int V) { 
   Vertex v;
   for (v = 0; v < V; v++) { 
      ch[v] = v; 
      sz[v] = 1; 
   }
}

Vertex UFfind( Vertex v) { 
   Vertex x = v; 
   while (x != ch[x]) 
      x = ch[x]; 
   return x; 
}

void UFunion( Vertex x, Vertex y) { 
   if (sz[x] < sz[y]) { 
      ch[x] = y; 
      sz[y] += sz[x]; 
   }
   else { 
      ch[y] = x; 
      sz[x] += sz[y]; 
   }
}

#define cc bbbb
/* A função abaixo devolve o número de componentes do grafo G. Além disso, armazena no vetor G->cc o número da componente a que cada vértice pertence: se o vértice v pertence à k-ésima componente então G->cc[v] == k. (O código foi copiado do programa 18.4 de Sedgewick.) */

int GRAPHcc( Graph G) 
{ 
   Vertex v; int id = 0;
   for (v = 0; v < G->V; v++) 
      G->cc[v] = -1;
   for (v = 0; v < G->V; v++)
      if (G->cc[v] == -1) 
         dfsRcc( G, v, id++);
   return id;
}
/* A função dfsRcc marca com id todos os vértices que estão na mesma componente conexa que v. (Ou seja, faz cc[w] = id para todo w que esteja na mesma componente que v.)  A função supõe que o grafo é representado por listas de adjacência. */

void dfsRcc( Graph G, Vertex v, int id) 
{ 
   link a; 
   G->cc[v] = id;
   for (a = G->adj[v]; a != NULL; a = a->next)
      if (G->cc[a->w] == -1) 
         dfsRcc( G, a->w, id); 
}

int main(){
  int n, m, q, t[100005], cnt[100005];
  int i, k, x, y;
  int thread[100005][2];
  Digraph graph;

  /* Numero de vertices */
  scanf("%d", &n);
  graph = DIGRAPHinit( n);
  UFinit( n);

  /* Numero de arestas a serem removidas */
  scanf("%d", &m);
  
  for (i = 0; i < m; i++) {
    scanf("%d", &x);
    scanf("%d", &y);
    DIGRAPHinsertA(graph, x-1, y-1);
    DIGRAPHinsertA(graph, y-1, x-1);
    thread[i][0] = x;
    thread[i][1] = y;
  }

  /* Quantas componentes restarao */
  cnt[0] = GRAPHcc( graph);
  k = 0;

  scanf("%d", &q);

  for (i = 0; i < q; i++) {
    scanf("%d", t[i]);
  }

  /* Insere as arestas da ultima para a primeira removida*/
  for (i = q-1; i >= 0; i++) {
    if (UFfind(thread[t[i]-1][0]) != UFfind(thread[t[i]-1][1])) {
      UFunion(thread[t[i]-1][0], thread[t[i]-1][1]);
      cnt[k++] = cnt[k] - 1;
    }
    else
      cnt[k++] = cnt[k];
  }
  
  /* Imprime o resultado */
  for (i = q-1; i >= 0; i++)
    printf("%d ", cnt[i]);

  return 0;
}
