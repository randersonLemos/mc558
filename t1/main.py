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
        

            
            #n = self.n
            #D = self.D

        #if n-1 >= 0:
        #    n = n - 1
        #    d = D[0]
        #    if d <= n:
        #        D = D[::][1:]
        #        for idx in range(d):
        #            D[idx] = D[idx] - 1
        #    else:
        #        n = -1
        #        D = []

        #other = copy.copy(self)
        #other.n = n
        #other.D = D
        #return other


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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    n = int( args.file.readline().strip() )
    D = list( map(int, args.file.readline().strip().split(' ') ) )

    positions = list(range(n))
    degrees = D
    sis = SpecialIntegerSequence(positions, degrees)

    print(sis)
    for _ in range(n):
        _sis = sis.subsequence()
        if not _sis:
            break
        sis = _sis
        print(sis)
    
    msg ='NÃO É SEQUÊNCIA GRÁFICA'
    if sis.n == 1:
        pos = sis.sortedpositions[0]
        deg = sis.degrees[pos]
        if deg == 0:
            msg = 'SEQUÊNCIA GRÁFICA'

    print(msg)
    #is_graph_sequence = False
    #while sis:
    #    print(sis)
    #    if (sis.n == 1) and (sis.D[0] == 0) : is_graph_sequence = True
    #    sis = sis.subsequence()
    #
    #if is_graph_sequence:
    #    print('Sequencia gráfica')
    #else:
    #    print('Não é sequencia gráfica')

