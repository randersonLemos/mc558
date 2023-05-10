import copy
import math
import pprint

class Sets():
    def __init__(self):
        self.dict = {}


    def make_set(self, elem):
        self.dict[elem] = set([elem])


    def find_set(self, elem):
        for key in self.dict:
            _set = self.dict[key]
            if elem in _set:
                return key
        return None


    def union(self, u ,v ):
        uset = self.dict[u]
        vset = self.dict[v]
        uset    = uset.union( vset )
        self.dict[u] = uset
        del self.dict[v]


    def __len__(self):
        return len(self.dict)


    def __repr__(self):
        return self.dict.__repr__()


def KRUSKAL( Adjs, W ):
    sets = Sets()
    A = set()

    for v in Adjs:
        sets.make_set(v)

    sW = sorted( W, key=W.get)

    for (u,v) in sW:        
        print( u, v )
        print( sets )
        useed = sets.find_set( u ) 
        vseed = sets.find_set( v )
        if useed != vseed:
            A.add( (u,v) )
            sets.union( useed, vseed )
    return A


if __name__ == '__main__':
    import argparse; parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    file = args.file
    n, m, k =  map( int, file.readline().strip().split(' ') ) # N -> computadores. M -> conexões, K -> Clusters
    
    W = {}
    Adjs = {}

    for i in range(n):
        Adjs[i] = []

    for i in range(m):
        x, y, w = map( int, file.readline().strip().split(' ') )
        Adjs[x].append( y )
        W[ (x,y) ] = w


    A = KRUSKAL( Adjs, W ) 

    import IPython; IPython.embed()
    
    #ini, end, cor, pai = DFS(Adjs, s, t)

    #TopSorLst = TopologicalSort(end)
   
    #q = CountPaths(Adjs, TopSorLst, s, t)

    #print( sum(q[t].values()) )
