import copy


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    file = args.file
    n, m =  map( int, file.readline().strip().split(' ') )

    adjs = {}
    plas = {}
    for i in range(n):
        adjs[i] = []
        plas[i] = 0

    for i in range(m):
        u, v, c = map( int, file.readline().strip().split(' ') )
        v_pos_u = len(adjs[u]); u_pos_v = len(adjs[v])

        adjs[u].append( (v, c, u_pos_v, 0) )
        adjs[v].append( (u, c, v_pos_u, 0) )

    import IPython; IPython.embed()
