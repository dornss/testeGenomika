### **Questão 2**
<br>

#### *Quais são as etapas mais comuns de um pipeline de bioinformática de NGS para DNAseq, e quais ferramentas podem ser usadas em cada etapa?*
***
Um pipeline de bioinformática são as múltiplas etapas nas quais trabalhamos os dados gerados no sequenciamento. O "workflow" é a sequência organizada desses comandos. Cada exame possui seu pipeline específico.

Os pipelines são consistentes de alguns alguns passos principais:

 * Controle de qualidade  
 * Geração da sequência de interesse
 * alinhamento da sequência com o genoma de referência;
 * chamada de variantes;
 * anotação das variantes;
 * seleção das variantes;

### Controle de qualidade

Verifica a qualidade dos dados brutos (FASTQ) gerados pela plataforma de sequenciamento, identificando erros técnicos e outros problemas. Ferramentas comuns usadas nesta etapa incluem FastQC e Trimmomatic.

### Geração da Sequência de interese

Geração de sequência (processamento de sinal e chamada de base) é o processo que converte dados de sensores (ópticos e não ópticos) da plataforma de sequenciamento e identifica a sequência de nucleotídeos para cada um dos fragmentos curtos de DNA na amostra preparada para análise. Para cada nucleotídeo sequenciado nesses fragmentos curtos (ou seja, *reads* brutos), é atribuída uma *score* Phred, correspondente, que é específica da plataforma de sequenciamento. As sequências de reads juntamente com o *score* Phred são armazenadas em um arquivo FASTQ, que é um padrão para representar informações de sequência biológica.

 ### Alinhamento da sequência com o genoma de referência

 O processo de alinhamento de sequências de DNA consiste em determinar a posição exata no genoma de referência onde cada fragmento sequenciado se encaixa. Durante esse processo, são avaliados os *scores* de qualidade Phred para cada leitura e é determinada a localização genômica correspondente a cada leitura alinhada. Essas informações podem ser utilizadas para calcular a cobertura do sequenciamento. O resultado do alinhamento é armazenado em um arquivo BAM. Ferramentas comuns usadas nesta etapa incluem BWA e Bowtie.

### Chamada de variantes

A chamada de variantes é  uma etapa para identificar trocas (SNPs), deleções ou inserções (indels). O resultado é um arquivo contendo apenas essas alterações, em um formato chamado VCF. No VCF cada linha representa uma variante detectada, contendo sempre de forma fixa as informações de: cromossomo/posição/alelo referência/alelo alternativo. A acurácia da chamada de variantes é muito dependente da qualidade das bases chamadas e dos reads alinhados. O ANNOVAR é a principal ferrament   a utilizada.

### Anotação das variantes

Depois de identificar as variantes, o próximo passo é a anotação, que envolve adicionar informações relevantes para "enriquecê-las".
Isso inclui determinar a localização genômica, a sequência de aminoácidos prevista e seu impacto na proteína, a frequência alélica, doenças associadas (OMIM), classificação em bancos de dados de variantes clínicas (CLINVAR) e de predição in silico (Polyphen, entre outros), bem como a frequência populacional. Nessa fase, a aplicação de filtros é crucial para obter resultados precisos. Inicialmente, pode haver mais de 100 variantes, mas a filtragem adequada pode reduzir essa lista para apenas uma ou duas variantes relevantes. Outras ferramentas para o processo de anotação são: ANNOVAR e VEP.

### Seleção de variantes e elaboração do laudo clínico

Após a anotação das variantes, as que são clinicamente relevantes são identificadas para revisão e interpretação. É de extrema importância que os pipelines de bioinformática estejam devidamente alinhados e validados para garantir que nenhuma variante importante para o paciente seja perdida durante o processo. Uma vez selecionadas, as variantes são classificadas seguindo as diretrizes da ACMG