import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)

MojeDane = pd.read_csv(r"/Users/dawidczech/Desktop/mojedane.csv", delimiter=';', engine='python') 
kanal1=MojeDane["pierwsza"]
numer=MojeDane["Cyfra"]

czestProbkowania = 200
t=np.linspace(0, 37.96, 200*37.96)

plt.subplot(2, 1, 1)
plt.plot(t,kanal1[:int(200*37.96)])
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')

przefiltrowany = ag.pasmowozaporowy(kanal1, czestProbkowania, 49,51)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany, czestProbkowania, 1,50)

plt.subplot(2, 1, 2)
plt.plot(t,przefiltrowany2[:int(200*37.96)])
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')

plt.show()

x=7603
y=0.1

print("Badana osoba mrugała widząc cyfrę: ")

for i in range (x):
    if przefiltrowany2[i]>y:
        print(numer[i])