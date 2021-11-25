import random
def uniform_crossover_operator(parent1,parent2,P_0):
    featur_num=len(parent1)
    offspring=[]
    for i in range(featur_num):
        if random.uniform(0,1)<=P_0[i]:
            offspring.append(parent1[i])
        else:
            offspring.append(parent2[i])
    return offspring
        