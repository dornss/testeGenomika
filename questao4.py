def overlap(s1, s2):
    maxOverlap = 0
    for i in range(min(len(s1), len(s2))):
        if s1[-i:] == s2[:i]:
            maxOverlap = i
    return maxOverlap


def mergeReads(reads):
    """
    Função que realiza o processo de merging de strings.
    Retorna a superstring resultante.
    """
    while len(reads) > 1:
        maxOverlap = 0
        for i in range(len(reads)):
            for j in range(i+1, len(reads)):
                o1 = overlap(reads[i], reads[j])
                o2 = overlap(reads[j], reads[i])
                if o1 > maxOverlap or o2 > maxOverlap:
                    if o1 >= o2:
                        maxOverlap = o1
                        mergeIndex = (i, j)
                    else:
                        maxOverlap = o2
                        mergeIndex = (j, i)
        i, j = mergeIndex
        mergedString = reads[i] + reads[j][maxOverlap:]
        reads = reads[:i] + [mergedString] + reads[i+1:j] + reads[j+1:]
    return reads[0]


# Lendo as reads do arquivo de entrada
with open("input.txt", "r") as f:
    dnaReads = f.read().splitlines()

# Chamando a função que realiza o merge
superstring = mergeReads(dnaReads)

# Escrevendo a superstring resultante no arquivo de saída
with open("output.txt", "w") as f:
    f.write(superstring)