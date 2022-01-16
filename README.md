# Gene_Selection_Sheep_Body_Weight
A modified memetic algorithm with an application to gene selection in a sheep body weight study

# Article link: 
https://www.mdpi.com/2076-2615/12/2/201

# Simple Summary
Due to lacking exploitation capability, traditional genetic algorithm cannot accurately identify the minimal best gene subset. Thus, the improved splicing method is introduced into a genetic algorithm to enhance exploitation capability for achieving balance between exploitation and exploration of GA. It can effectively identify true gene subsets with high probability. Furthermore, a dataset of the body weight of Hu sheep has been used to show that the proposed method can obtain a better minimal subset of genes with a few iterations, compared with all considered algorithms including genetic algorithm and adaptive best-subset selection algorithm.

# Abstract
Selecting the minimal best subset out of a huge number of factors for influencing the response is a fundamental and very challenging NP-hard problem because the presence of many redundant genes results in over-fitting easily while missing an important gene can more detrimental impact on predictions, and computation is prohibitive for exhaust search. We propose a modified memetic algorithm (MA) based on an improved splicing method to overcome the problems in the traditional genetic algorithm exploitation capability and dimension reduction in the predictor variables. The new algorithm accelerates the search in identifying the minimal best subset of genes by incorporating it into the new local search operator and hence improving the splicing method. The improvement is also due to another two novel aspects: (a) updating subsets of genes iteratively until the no more reduction in the loss function by splicing and increasing the probability of selecting the true subsets of genes; and (b) introducing add and del operators based on backward sacrifice into the splicing method to limit the size of gene subsets. Additionally, according to the experimental results, our proposed optimizer can obtain a better minimal subset of genes with a few iterations, compared with all considered algorithms. Moreover, the mutation operator is replaced by it to enhance exploitation capability and initial individuals are improved by it to enhance efficiency of search. A dataset of the body weight of Hu sheep was used to evaluate the superiority of the modified MA against the genetic algorithm. According to our experimental results, our proposed optimizer can obtain a better minimal subset of genes with a few iterations, compared with all considered algorithms including the most advanced adaptive best-subset selection algorithm.

# Please cite as

AMA Style

Miao M, Wu J, Cai F, Wang Y-G. A Modified Memetic Algorithm with an Application to Gene Selection in a Sheep Body Weight Study. Animals. 2022; 12(2):201. https://doi.org/10.3390/ani12020201

Chicago/Turabian Style

Miao, Maoxuan, Jinran Wu, Fengjing Cai, and You-Gan Wang. 2022. "A Modified Memetic Algorithm with an Application to Gene Selection in a Sheep Body Weight Study" Animals 12, no. 2: 201. https://doi.org/10.3390/ani12020201
