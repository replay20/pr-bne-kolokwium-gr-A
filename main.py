import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#zad1
x = np.linspace(1, 10, 9,endpoint=False)
#print(x)

plt.plot(x, (x*x+4)/2**x, label="f(x)=(x*x+4)/(2**x)")
plt.title("Wykres funkcji f(x)=(x*x+4)/(2**x)")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend()
plt.show()

#zad2

x2 = np.linspace(-3,3,100,endpoint=True)

plt.subplot(1,3,1,)
plt.plot(x2, x2*x2 + 5, label="x^2+5")
plt.xticks([-3,0,3])
plt.xlim(-3,3)
plt.title("Wykres funkcji f(x)=x^2+5")
plt.ylabel('wartości funkcji')
plt.xlabel('x')
plt.legend()


plt.subplot(1,3,2,)
plt.plot(x2, x2*x2 + 5, label="x^2+5", color="red", linewidth=6)
plt.plot(x2, -(x2*x2) + (4 * x2), label="-x^2+4x", color="green", linewidth=6)
plt.xticks([-3,0,3])
plt.xlim(-3,3)
plt.title("Wykres dwóch funkcji")
plt.ylabel('wartości funkcji')
#plt.subplots_adjust(wspace=3)
plt.ylabel('wartości funkcji')
plt.xlabel('x')
plt.legend()

plt.show()

#zad3

df = pd.read_csv('automobile.csv',header=0, sep=";", decimal=".")
losowe_wiersze = df.sample(n=100, replace=False)
df2 = losowe_wiersze
#print(df)

grouped = df2.groupby('Car model').size()

#print(grouped)

grouped.plot(kind='pie', subplots=True, autopct='%.0f %%', fontsize=14)
plt.legend()
plt.show()

#zad4

srednia = df.groupby('Car model')['Price'].mean()

plt.figure(figsize=(12,8))
srednia.plot(kind='bar')
plt.xlabel('Model samochodu')
plt.ylabel('Średnia cena')
plt.title('Średnia cena samochodów dla każdej z marek')
plt.show()

