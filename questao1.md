### **Questão 1**
<br>

#### *O que é um arquivo FASTQ e como validá-lo?*
***
Um arquivo FASTQ é um tipo de arquivo de formato de sequência de DNA que contém informações sobre as bases nucleotídicas (A, C, G, T) e suas respectivas qualidades de sequenciamento.

Cada registro em um arquivo FASTQ é composto por quatro linhas: a primeira linha começa com o caractere "@" e contém um identificador de sequência; a segunda linha contém a sequência de DNA; a terceira linha começa com o caractere "+" e pode conter uma descrição opcional; e a quarta linha contém a sequência de qualidade que corresponde à sequência de DNA na linha anterior.

Para verificar se um arquivo FASTQ é válido, você pode usar ferramentas de validação de arquivos FASTQ, como o "FastQC" ou "Qualimap". Essas ferramentas fornecem informações detalhadas sobre a qualidade dos dados de sequenciamento, incluindo estatísticas de qualidade, distribuição de qualidade, comprimento de sequência e presença de adaptadores ou contaminantes.

Outra forma de verificar a validade do arquivo FASTQ é executar uma análise de controle de qualidade dos dados de sequenciamento, que geralmente envolve o uso de ferramentas de alinhamento e montagem para identificar erros de sequenciamento, lacunas ou problemas de qualidade. Alguns programas populares incluem o "Bowtie2", "BWA" e "SPAdes".

Em resumo, para verificar a validade de um arquivo FASTQ, você pode usar ferramentas de validação de arquivos FASTQ ou executar uma análise de controle de qualidade dos dados de sequenciamento usando ferramentas de alinhamento e montagem.