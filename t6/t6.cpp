#include <queue>
#include <tuple>
#include <vector>
#include <numeric>
#include "shortest_path.hpp"


using namespace std;


int loadCoins( int& n, int& Q,  vector<int>& vi, vector<int>& vv, vector<int>& vp, vector<int>& vq ) 
{
    int N = 0;
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

    return N;
}


void showCoins( int N, vector<int>& vi, vector<int>& vv, vector<int>& vp, vector<int>& vq )
{
    for( int i = 0; i < N; i++)
    {
      cout << "(" << vi[i] << ") " << vv[i] << " " << vp[i] << endl;
    }
}


void getTuplecq(int &c, int &q, tuple< int, int > _tuple)
{
  c = get<0>(_tuple); q = get<1>(_tuple);
}


int computeVerticeIndex( int c, int q, int Q)
{
  return c*(Q+1)+q;
}


int main() {
    int n, Q;
    vector<int> vi, vv, vp, vq;

    int C = loadCoins( n, Q, vi, vv, vp, vq );
    int V = accumulate(vv.begin(), vv.end(), 0 );
    int P = accumulate(vp.begin(), vp.end(), 0);

    if( V < Q )
    {
      cout << V << " " << P << endl;
      return 0;
    }

    //cout << "C:" << C << " Q: " << Q << " V: " << V << endl;
    //showCoins( C, vi, vv, vp, vq );
    //cout << "---" << endl;
    
    Grafo g( C*(Q+1) );

    //int c, q = -1;
    //tuple<int, int> _tuple;
    //queue< tuple<int, int> > waitroom;
    //waitroom.push( make_tuple(0,0) );

    //while( !waitroom.empty() )
    //{
    //  _tuple = waitroom.front();
    //  getTuplecq( c, q, _tuple);

    //  if( c == (C -1) )
    //    break;

    //  int cc0 = c+1; int qq0 = q;           int pp0 = 0;
    //  int cc1 = c+1; int qq1 = q + vv[c+1]; int pp1 = vp[c+1];
    //  int i   = computeVerticeIndex(c,   q,   Q);
    //  int ii0 = computeVerticeIndex(cc0, qq0, Q);
    //  int ii1 = computeVerticeIndex(cc1, qq1, Q);

    //  cout << c   <<  ", " << q;

    //  if ( (cc0 < C) && ( qq0 < (Q + 1) ) )
    //  {
    //    cout << " => " << cc0 <<  ", " << qq0;
    //    waitroom.push( make_tuple( cc0, qq0 ) );
    //    g.adicionaArco(i, ii0, pp0);
    //  }
    //  if ( (cc1 < C) && (qq1 < (Q + 1) ) )
    //  {
    //    cout << " and " << cc1 <<  ", " << qq1;
    //    waitroom.push( make_tuple( cc1, qq1 ) );
    //    g.adicionaArco(i, ii1, pp1);
    //  }
    //  cout << endl;
    //  waitroom.pop();
    //}
    
    //cout << "---" << endl;
    //cout << g;
    //cout << "---" << endl;

    //cout << "C: "<< C << " Q: " << Q << endl;
    //showCoins( C, vi, vv, vp, vq );
    //cout << endl;

    for( int c = 0; c < C ; c++)
    {
      if( c == (C - 1) ) continue;

      for( int q = 0; q < Q+1; q++)  
      {
        int cc0 = c+1; int qq0 = q;           int pp0 = 0;
        int cc1 = c+1; int qq1 = q + vv[c+1]; int pp1 = vp[c+1];
        int i   = computeVerticeIndex(c,   q,   Q);
        int ii0 = computeVerticeIndex(cc0, qq0, Q);
        int ii1 = computeVerticeIndex(cc1, qq1, Q);

        if( c == 0 && q == 0 )
        {
          //cout << "| (" << c << "," << q <<  ")" << "->" << pp0 << "->" << "(" << cc0 << "," << qq0 << ") => "; 
          //cout << "(" << i << "," << ii0  << "," << pp0 <<") \t| "; 
          g.adicionaArco(i, ii0, pp0);
          if( ( qq1 < Q+1 ))
          {
            //cout << "(" << c << "," << q <<  ")" << "->" << pp1 << "->" << "(" << cc1 << "," << qq1 << ") => " ; 
            //cout << "(" << i << "," << ii1 << "," << pp1 <<")"; 
            g.adicionaArco(i, ii1, pp1);
          }
          //cout << endl;
        }
        //if( ( c > 0 )  && ( c <  (C - 2) ) )
        if( ( c > 0 )  && ( c <  (C - 1) ) )
        {
          //cout << "| (" << c << "," << q <<  ")" << "->" << pp0 << "->" << "(" << cc0 << "," << qq0 << ") => "; 
          //cout << "(" << i << "," << ii0  << "," << pp0 <<") \t| "; 
          g.adicionaArco(i, ii0, pp0);
          if( ( qq1 < Q+1 ))
          {
            //cout << "(" << c << "," << q <<  ")" << "->" << pp1 << "->" << "(" << cc1 << "," << qq1 << ") => " ; 
            //cout << "(" << i << "," << ii1 << "," << pp1 <<")"; 
            g.adicionaArco(i, ii1, pp1);
          }
          //cout << endl;
        }
      }
      //cout << "===" << endl;
    }
    
    //cout << "Grafo gerado:" << endl;
    //cout << g;
    //cout << "---" << endl;
    
    
    int source = 0; bool first = true;
    for( int q = Q; q >=0; q--)
    {
      int target = computeVerticeIndex(C-1, q, Q);
      int *dist = g.caminhoMinimo(source, target);

      if( (first) && (dist[target] != 2147483647 ))
      {
        cout << dist[target] << endl;
        break;
      }

      if( !(first) && dist[target] != 2147483647 )
      {
        cout << q << " " << dist[target] << endl;
        break;
      }
      first = false;
    }
}

