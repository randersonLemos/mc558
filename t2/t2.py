import copy
import pprint


class AdjacencyListElements:
    def __init__(self, vertice, color, neighbor_index, visited):
        self.vertice = vertice
        self.color = color
        self.neighbor_index = neighbor_index
        self.visited = visited


    def __hash__(self):
        return hash(self.vertice)


    def __repr__(self):
        return '(v:{}-c:{}-n:{}-v:{})'.format(self.vertice, self.color, self.neighbor_index, self.visited)


class AdjacencyList:
    def __init__(self):
        self.lst = []
        self.blocked = set()


    def append(self, adjacencylistelement):
        self.lst.append( adjacencylistelement )


    def get_element(self, index):
        return self.lst[index]


    def free_indexes(self):
        return set( range( len(self.lst) ) ) - self.blocked


    def block_element(self, index):
        self.blocked.add( index )


    def __len__(self):
        return self.lst.__len__()

    
    def __repr__(self):
        return '{} - {}'.format(self.lst.__repr__(), self.free_indexes().__repr__())


def computeMaximalTrail( root, adjs, edge_color=-1 ):
    T = [];
    T.append( root )
    #edge_color = -1

    #pprint.pprint( adjs ); print('---')
    #print( T ); print('+++')

    while True:
        v = T[-1]
        previous_edge_color = edge_color
        adjacencylist_v = adjs[v]
        found_vertice = False

        if not adjacencylist_v.free_indexes(): # No free elements
           return [], -1

        for u_idx_v in adjacencylist_v.free_indexes():
            u_adjacencyelement_v = adjacencylist_v.get_element(u_idx_v)
            u          = u_adjacencyelement_v.vertice
            v_idx_u    = u_adjacencyelement_v.neighbor_index
            edge_color = u_adjacencyelement_v.color

            if edge_color != previous_edge_color:
                found_vertice = True
                T.append(u)
                u_adjacencyelement_v.visited = 1
                adjacencylist_u = adjs[u]
                v_adjacencyelement_u = adjacencylist_u.get_element(v_idx_u)
                v_adjacencyelement_u.visited = 1

                adjacencylist_u.block_element(v_idx_u)
                adjacencylist_v.block_element(u_idx_v)
                break

        #pprint.pprint( adjs ); print('---')
        #print( T ); print('+++')

        if not found_vertice : return [], -1
        if T[0] == T[-1] : return T, edge_color
    

def concatTrail( trail, pivot, other ):
    if pivot == -1:
        return other

    trail[pivot:pivot] = other[:-1]
    return trail


def computeEulerianTrail( adjs ):
    EulerianAlternateTrail = [0]
    maximaltrail = []
    edge_color = -1
    while True:
        free_indexes = False
        for pivot, v in enumerate( EulerianAlternateTrail ): 
            adjacencylist = adjs[ v ]
            if adjacencylist.free_indexes():
                free_indexes = True
                root = v
                break

        if not free_indexes:
            return EulerianAlternateTrail

        maximaltrail, edge_color = computeMaximalTrail( root, adjs, edge_color )

        if not maximaltrail:
            return []
            #return 'Não possui trilha Euleriana alternante'

        #print('R', root) 
        #print('E', EulerianAlternateTrail)
        #print('M', maximaltrail)

        EulerianAlternateTrail = concatTrail( EulerianAlternateTrail, pivot, maximaltrail)

        #print('E', EulerianAlternateTrail)
            

if __name__ == '__main__':
    #import argparse; parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    #args = parser.parse_args()
    #file = args.file
    #n, m =  map( int, file.readline().strip().split(' ') )

    n, m = map( int, input().strip().split(' ') )

    adjs = {}
    for i in range(n):
        adjs[i] = AdjacencyList()


    for i in range(m):
        #u, v, c = map( int, file.readline().strip().split(' ') )
        u, v, c = map( int, input().strip().split(' ') )
        v_pos_u = len(adjs[u]); u_pos_v = len(adjs[v])

        adjs[u].append( AdjacencyListElements(vertice = v, color = c, neighbor_index = u_pos_v, visited = 0) )
        adjs[v].append( AdjacencyListElements(vertice = u, color = c, neighbor_index = v_pos_u, visited = 0) )

    result = computeEulerianTrail( adjs )
    
    stg = 'Não possui trilha Euleriana alternante'
    if result: 
        stg = ' '.join(map( str, result) )

    print( stg )


