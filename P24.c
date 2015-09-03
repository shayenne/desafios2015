#include<stdio.h>
#include<stdlib.h>

#define maxV 1000000
#define Vertex long long

/* REPRESENTAÇÃO POR LISTAS DE ADJACÊNCIA: A estrutura digraph representa um digrafo. O campo adj é um ponteiro para o vetor de listas de adjacência, o campo V contém o número de vértices e o campo A contém o número de arcos. */

typedef struct node *link;
struct node { 
   Vertex w; 
   link next; 
};

struct digraph {
   int V; 
   int A; 
   link *adj; 
};

/* Um objeto do tipo Digraph contém o endereço de um digraph. */

typedef struct digraph *Digraph;

/* A lista de adjacência de um vértice v é composta por nós do tipo node. Cada nó da lista corresponde a um arco e contém um vizinho w de v e o endereço do nó seguinte da lista. Um link é um ponteiro para um node. */


/* A função NEWnode recebe um vértice w e o endereço next de um nó e devolve o endereço a de um novo nó tal que a->w == w e a->next == next. */

link NEWnode( Vertex w, link next) { 
   link a = malloc( sizeof (struct node));
   a->w = w; 
   a->next = next;     
   return a;                         
}

/* REPRESENTAÇÃO POR LISTAS DE ADJACÊNCIA: A função DIGRAPHinit devolve (o endereço de) um novo digrafo com vértices 0 1 ... V-1 e nenhum arco. */

Digraph DIGRAPHinit( long long V) { 
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

/* Vamos supor que nossos digrafos têm no máximo maxV vértices. */

static long long conta, pre[maxV], pos[maxV];

/* A função devolve 1 se o digrafo G tem um ciclo e devolve 0 em caso contrário. */

int DIGRAPHcycle( Digraph G) 
{ 
   Vertex v;
   conta = 0;
   for (v = 0; v < G->V; v++)
      pre[v] = pos[v] = -1;
   for (v = 0; v < G->V; v++)
      if (pre[v] == -1) 
         if (cycleR( G, v) == 1) return 1;
   return 0;
}

/* A função cycleR devolve 1 quando encontra um ciclo ao percorrer G a partir do vértice v e devolve 0 em caso contrário. */

int cycleR( Digraph G, Vertex v) 
{ 
   link a;
   pre[v] = conta++;
   for (a = G->adj[v]; a != NULL; a = a->next) {
      Vertex w = a->w;
      if (pre[w] == -1) {
         if (cycleR( G, w) == 1) return 1;
      } else if (pos[w] == -1) return 1; /* v-w é arco de retorno */
   }
   pos[v] = conta++;
   return 0;
}

static long long tsi[maxV];
#define Dag Digraph

/* Recebe um DAG G e armazena em tsi[0..V-1] uma ordenação topológica de G:  para cada arco v-w teremos tsi[v] < tsi[w].  (O código é cópia do Programa 19.6 de Sedgewick.) */
void TSdfsR( Dag G, Vertex v) 
{ 
   link a; 
   pre[v] = 0; 
   for (a = G->adj[v]; a != NULL; a = a->next)
      if (pre[a->w] == -1) 
         TSdfsR( G, a->w); 
   tsi[v] = conta--;
}

void DAGts( Dag G) 
{ 
   Vertex v; 
   conta = G->V - 1;
   for (v = 0; v < G->V; v++)  
      pre[v] = -1; 
   for (v = 0; v < G->V; v++)
      if (pre[v] == -1) 
         TSdfsR( G, v);
}
/********
 * MAIN *
 ********/

int main() {
  long long i, x, y;
  Digraph d;
  long long n, k;

  scanf("%d %d", &n, &k);

  while (n != 0) {
    d = DIGRAPHinit( n);
    
    /* Construção do digrafo*/
    for (i = 0; i < k; i++) {
      scanf("%d %d", &x, &y);
      DIGRAPHinsertA( d, x-1, y-1);
    }

    if (!DIGRAPHcycle(d)) {
      DAGts( d);
      for (i = 0; i < n; i++)
	printf("%d\n", tsi[i]+1);
    }
    else
      printf("IMPOSSIBLE\n");
    
    scanf("%d %d", &n, &k);
  }
  return 0;
}
