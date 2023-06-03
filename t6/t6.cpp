#include "shortest_path.hpp"

using namespace std;

// int main() {
//     Grafo g(4);

//     g.adicionaArco(0, 1, 2);
//     g.adicionaArco(0, 2, 1);
//     g.adicionaArco(1, 3, 3);
//     g.adicionaArco(2, 3, 6);

//     cout << "Grafo gerado:" << endl;
//     cout << g;

//     int *dist = g.caminhoMinimo(0, 3);
//     cout << "Distância mínima entre 0 e 3: " << dist[3] << endl;
//     free(dist);

//     return 0;
// }

int main() {
    int n, Q = 0;

    int v[150] = { 0 };  
    int p[150] = { 0 };  
    int q[150] = { 0 };  

    for( int i = 0; i < 150; i++)
    {
      cout << "(" << i << ") " << v[i] << " " << p[i] << " " << q[i] << endl;
    }
    cout << "---" << endl;

    cin >> n >> Q;
    for( int i = 0; i < n; i++)
    {
      cin >> v[i] >> p[i] >> q[i];
    }


    cout << n << " " << Q << endl;
    for( int i = 0; i < n; i++)
    {
      cout << v[i] << " " << p[i] << " " << q[i] << endl;
    }



}
