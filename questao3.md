### **Questão 3**
<br>

#### *Considerando que o alinhamento de sequências biológicas é uma das atividades maisrecorrentes e importantes na área de bioinformática. Comente sobre os algoritmos computacionais de alinhamentos mais utilizados e em que cenários uns são mais indicados do que outros?*
***

Sendo um dos pilares da bioinformática, o alinhamento de sequências pode ser realizado entre duas ou múltiplas sequências, e são aplicados para comparar o nível de identidade entre elas, dentre outras várias aplicações. Desde os anos 70, o alinhamento vem sendo utilizado na bioinformática, e os algorítimos utilizados são classificados como dito a seguir:

### Alinhamento par  a par

O alinhamento par a par, também conhecido como alinhamento de duas sequências, é um método de comparação de duas sequências biológicas, como sequências de DNA ou proteína, para encontrar regiões de similaridade e identificar as diferenças entre elas. O algorítimo utiliza a representação *dot-matrix* para detecção de indels.

### Matrizes de substituição

Desenvolvido por Margareth Dayhoff ainda na década de 60, sendo a pioneira na área de Quimioinformática, foi a primeira a desenvolver o Sequence Atlas, um banco de dados de proteínas.
O algoritmo de matrizes de substituição é um método utilizado em bioinformática para avaliar a similaridade entre duas sequências. Ele funciona criando uma matriz de pontuações para cada possível par de resíduos em duas sequências, atribuindo uma pontuação para a probabilidade de que aqueles dois resíduos sejam substituídos por um ao longo da evolução. Essas pontuações são baseadas em observações de frequências de substituição em conjuntos de sequências homólogas. A partir da matriz de substituição, é possível calcular o score de alinhamento entre duas sequências.
Alguns exemplos de matrizes de substituição comumente utilizadas são a matriz BLOSUM para alinhamento de sequências de proteínas, a matriz PAM para análises filogenéticas de proteínas 

### Algoritmo de sequências local

O algoritmo de sequência local é um método de alinhamento de sequências que tem como objetivo encontrar a região de maior similaridade entre duas sequências, sem necessariamente alinhar todas as posições das sequências. O algoritmo de sequência local mais conhecido é o algoritmo Smith-Waterman, que utiliza uma abordagem de programação dinâmica para encontrar a região de maior similaridade entre duas sequências, mesmo que estejam em regiões divergentes;

O algoritmo de alinhamento local foi criado a partir dos algoritmos de alinhamento global. A ferramenta mais popular para realizar alinhamentos locais é o BLAST (Basic Local Alignment Search Tool), que pode comparar uma sequência de interesse com um banco de dados contendo muitas outras sequências. O BLAST detecta sementes em todas as entradas do banco de dados usando matrizes de substituição para encontrar os melhores alinhamentos, que são estendidos ao máximo local seguindo regras de pontuação. Essas pontuações geram um valor de escore e o BLAST calcula um valor de significância chamado e-value (Expectation value). O e-value não é uma probabilidade típica da estatística, mas representa a chance de encontrar por acaso um alinhamento igual ou melhor do que o apresentado. Quanto mais negativo for o valor, mais significativo será o resultado.

### Algoritmo de sequências global

O algoritmo de alinhamento global é utilizado para comparar duas sequências completas, ou seja, do início ao fim, considerando todas as posições de cada sequência. Ele é aplicado quando as sequências em questão têm um alto grau de similaridade e quando é importante identificar correspondências de nucleotídeos ou aminoácidos em todas as posições. Alguns exemplos de aplicação incluem a identificação de homologias entre sequências genômicas ou proteicas, a identificação de variantes genéticas e a análise de similaridade entre proteínas de diferentes espécies. O algoritmo de Needleman-Wunsch é um exemplo de algoritmo de alinhamento global amplamente utilizado.

### Algorítmo de alinhamento de múltiplas sequências

O algoritmo de alinhamento múltiplo de sequências é utilizado para comparar mais de duas sequências ao mesmo tempo. Ele é aplicado quando se deseja identificar relações evolutivas entre diversas sequências, como, por exemplo, na construção de árvores filogenéticas. Também é utilizado para a identificação de regiões conservadas em múltiplas sequências, que podem estar associadas a funções importantes, como sítios de ligação a proteínas ou locais de splicing em transcritos.

O algoritmo mais utilizado para alinhamento múltiplo é o algoritmo de alinhamento progressivo, que é uma abordagem heurística que envolve a construção de uma árvore filogenética a partir das sequências e o alinhamento de sequências próximas na árvore antes de alinhar sequências mais distantes. Outros algoritmos de alinhamento múltiplo incluem o algoritmo de programação dinâmica de MSA (Multiple Sequence Alignment) e o algoritmo de agrupamento de sequências. O alinhamento múltiplo de sequências é amplamente utilizado em estudos de genômica comparativa, análises de famílias de proteínas e em outras aplicações de bioinformática que envolvem a análise comparativa de múltiplas sequências biológicas.
