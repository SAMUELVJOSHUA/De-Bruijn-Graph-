#build debruijn graph
def deBruijn_graph(text,k):

    k_1mer = []
    for i in range(len(text)-k+2):
        k_1mer.append(text[i:i+k-1])

    k_1mer = sorted(list(set(k_1mer)))

    

text = 'ACGTTCTAGATTCT'
k = 4
temp = deBruijn_graph(text,k)
