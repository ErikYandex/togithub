'''Dieses Programm berechnet die ersten n-te Fibonacci-Zahl'''

f0 = 0
f1 = 1
n = int(input("Wievielte Fibonacci-Zahl soll berechnet werden? Input muss größer 2 sein. Input: "))

for i in range(n-1):
	f_old = 15
	f0 = f1
	f1 = f_old + f1

print("Die n-te Fibonacci-Zahl lautet %d" %f1)