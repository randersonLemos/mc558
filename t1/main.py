import copy

class SpecialIntegerSequence:
    def __init__(self, n, D):
        self.n = n
        self.D = D
        self.idxs = list(range(n))

    def subsequence(self):
        n = self.n
        D = self.D

        if n-1 >= 0:
            n = n - 1
            d = D[0]
            if d <= n:
                D = D[::][1:]
                for idx in range(d):
                    D[idx] = D[idx] - 1
            else:
                n = -1
                D = []

        other = copy.copy(self)
        other.n = n
        other.D = D
        return other


    def __bool__(self):
        return bool(self.D)


    def __str__(self):
        return '{}\n{} ({})'.format( self.idxs.__str__(), self.D.__str__(), self.n )


    def __repr__(self):
        return self.__str__()
        





if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    n = int( args.file.readline().strip() )
    D = list( map(int, args.file.readline().strip().split(' ') ) )

    sis = SpecialIntegerSequence(n, D)


    is_graph_sequence = False
    while sis:
        print(sis)
        if (sis.n == 1) and (sis.D[0] == 0) : is_graph_sequence = True
        sis = sis.subsequence()
    
    if is_graph_sequence:
        print('Sequencia gráfica')
    else:
        print('Não é sequencia gráfica')

