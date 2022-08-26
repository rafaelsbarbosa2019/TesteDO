import pandas as PD
import numpy as NP
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def entra_arquivo():
    df = PD.read_csv('DOentra.csv', sep=';')
    bongo = df.loc[[0]].to_numpy()
    a, b, c, d = NP.array(bongo[0], dtype=float)
    soma = a + b + c + d
    return soma
def sai_arquivo(inpu,ind):
    saida = NP.array([inpu])
    nomearq = 'DOsai' + str(ind) + '.csv'
    NP.savetxt(nomearq, saida)
    xflag = 1
    return xflag
