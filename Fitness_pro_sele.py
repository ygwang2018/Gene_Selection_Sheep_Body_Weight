import numpy as np
import random
def FPS(F,N):
    Fit=1/np.array(F)
    sum_fitness=np.sum(Fit)
    survival_probability=[]
    for i in range(N):
        p=Fit[i]/sum_fitness
        survival_probability.append(p)
    cul_probability=[0]
    cul_pro=0
    sele_individual=0
    #Roulette Wheel Sampling
    for i in range(N):
        cul_pro=cul_pro+survival_probability[i]
        cul_probability.append(cul_pro)
    for i in range(N):
        if cul_probability[i]<=random.uniform(0,1)<cul_probability[i+1]:
            sele_individual=i
    return sele_individual