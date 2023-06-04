#include <vector>
#include "shortest_path.hpp"

using namespace std;

//int main() {
//    Grafo g(4);
//
//    g.adicionaArco(0, 1, 2);
//    g.adicionaArco(0, 2, 1);
//    g.adicionaArco(1, 3, 3);
//    g.adicionaArco(2, 3, 6);
//
//    cout << "Grafo gerado:" << endl;
//    cout << g;
//
//    int *dist = g.caminhoMinimo(0, 3);
//    cout << "Distância mínima entre 0 e 3: " << dist[3] << endl;
//    free(dist);
//
//    return 0;
//}

void loadCoins( int& n, int& Q, int& N, vector<int>& vi, vector<int>& vv, vector<int>& vp, vector<int>& vq ) {
    // Source
    vi.push_back( N ); vv.push_back( 0 ); vp.push_back( 0 ); vq.push_back( 1 );
    N += 1;

    cin >> n >> Q;
    for( int i = 0; i < n; i++)
    {
      int v, p, q = 0;
      cin >> v >> p >> q;
      for( int j = 0; j < q; j++)
      {
        // Coins
        vi.push_back( N ); vv.push_back( v ); vp.push_back( p ); vq.push_back( 1 );
        N += 1;
      }
    }
    // Target
    vi.push_back( N ); vv.push_back( 0 ); vp.push_back( 0 ); vq.push_back( 1 );
    N += 1;
}


void showCoins( int N, vector<int>& vi, vector<int>& vv, vector<int>& vp, vector<int>& vq )
{
    for( int i = 0; i < N; i++)
    {
      cout << "(" << vi[i] << ") " << vv[i] << " " << vp[i] << endl;
    }
}

int computeVerticeIndexFromCQ( int c, int q, int Q)
{
  return c*(Q+1)+q;
}

void computeCQFromVerticeIndex( int idx, int Q)
{
  return;
}


int main() {
    int n, Q, C = 0;
    vector<int> vi, vv, vp, vq;

    loadCoins( n, Q, C, vi, vv, vp, vq );

    showCoins( C, vi, vv, vp, vq );
    cout << endl;

    for( int c = 0; c < C ; c++)
    {
      for( int q = 0; q < Q+1; q++)  
      {
        int cc0 = c+1; int qq0 = q; int pp0 = 0;
        int cc1 = c+1; int qq1 = q + vv[c+1]; int pp1 = vp[c+1];

        cout << "(" << c << "," << q <<  ")" << "->" << pp0 << "->" << "(" << cc0 << "," << qq0 << ")" << endl; 
        cout << "(" << computeVerticeIndexFromCQ(c, q, Q) <<  ")" << "->" << pp0 << "->" << "(" << computeVerticeIndexFromCQ(cc0, qq0, Q)  << ")" << endl; 
        cout << "(" << computeVerticeIndexFromCQ(c, q, Q) << "," << computeVerticeIndexFromCQ(cc0, qq0, Q)  << "," << pp0 <<")" << endl; 

        cout << "---" << endl;

        cout << "(" << c << "," << q <<  ")" << "->" << pp1 << "->" << "(" << cc1 << "," << qq1 << ")" << endl; 
        cout << "(" << computeVerticeIndexFromCQ(c, q, Q) <<  ")" << "->" << pp1 << "->" << "(" << computeVerticeIndexFromCQ(cc1, qq1, Q)  << ")" << endl; 
        cout << "(" << computeVerticeIndexFromCQ(c, q, Q) << "," << computeVerticeIndexFromCQ(cc1, qq1, Q)  << "," << pp1 <<")" << endl; 
        cout << endl;
      }
      cout << endl;
      break;
    }
    
    Grafo g( 5 );


    cout << "Grafo gerado:" << endl;
    cout << g;

}

