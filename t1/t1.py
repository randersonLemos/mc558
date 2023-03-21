import copy

class SpecialIntegerSequence:
    def __init__(self, positions, degrees):
        self.positions = positions
        self.degrees = degrees
        self.n = len(positions)
        self.sortedpositions = sorted(positions, key=lambda x: degrees[x], reverse=True)


    def subsequence(self):
        sortedposition = self.sortedpositions[0]
        d = self.degrees[sortedposition]
        n = self.n
        if ( (n-1-d) >= 0 ) and ( (n-1) > 0 ):
            sortedpositions = self.sortedpositions[::][1:]
            degrees = self.degrees[::]
            for pos in range(d):
                sortedposition = sortedpositions[pos]
                degrees[sortedposition] = degrees[sortedposition] - 1

            return SpecialIntegerSequence(sortedpositions, degrees)
        

    def adjacentvertices(self):
        u = self.sortedpositions[0] 
        d = self.degrees[u]
        n = self.n

        adjs = []
        if n - d > 0:
            for i in range(d):
                v = self.sortedpositions[i+1]
                adjs.append( (u, v) )
        return adjs
        

    def __bool__(self):
        return bool(self.positions)


    def __str__(self):
        _str_  = '{} - ({}) POSITIONS        \n'.format(self.positions, self.n)
        _str_ += '{} - ({}) DEGREES          \n'.format([self.degrees[pos] for pos in self.positions], self.n)
        _str_ += '{} - ({}) SORTED POSITIONS \n'.format(self.sortedpositions, self.n)
        _str_ += '{} - ({}) SORTED DEGREES   \n'.format([self.degrees[pos] for pos in self.sortedpositions], self.n)
        return _str_


    def __repr__(self):
        return self.__str__()
        

if __name__ == '__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    #args = parser.parse_args()
    #n = int( args.file.readline().strip() )
    #D = list( map(int, args.file.readline().strip().split(' ') ) )

    n = int( input().strip() )
    D = list( map(int, input().strip().split(' ')) )

    positions = list(range(n))
    degrees = D
    sis = SpecialIntegerSequence(positions, degrees)
    
    adjs = {}
    for v in positions:
        adjs[v+1] = set()

    E = sis.adjacentvertices()
    for u,v in E : adjs[u+1].add(v+1); adjs[v+1].add(u+1)

    for _ in range(n):
        _sis = sis.subsequence()
        if not _sis:
            break
        sis = _sis

        E = sis.adjacentvertices()
        for u,v in E : adjs[u+1].add(v+1); adjs[v+1].add(u+1)

    msg ='Não é sequência gráfica!'
    if sis.n == 1:
        pos = sis.sortedpositions[0]
        deg = sis.degrees[pos]
        if deg == 0: # É sequência gráfica
            msg = ''
            for u in adjs:
                msg += ( ' '.join( map(str, sorted(adjs[u])) ) if adjs[u] else '' ) + '\n'
            msg = msg[:-1]
                
    print( msg )

