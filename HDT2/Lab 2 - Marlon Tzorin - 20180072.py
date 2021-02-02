import numpy as np

print("\n \n Lab 2 - Marlon Tzorin - 20180072 \n \n ")

#{P1}
print("\n \nProblema 1\n \n")

m = np.array([
    [1,1,0,0,0,0,1],
    [0,1,1,0,0,1,0],
    [0,0,1,1,0,0,0],
    [0,0,0,1,1,0,1],
    [1,0,0,0,0,1,1],
    [0,0,0,0,1,1,1],
    [1,1,1,0,0,0,1]
])

m1 = np.array([
    [1,1,0,0,0,1,1],
    [1,1,1,0,1,0,0],
    [0,1,1,1,1,0,0],
    [0,0,1,1,0,0,1],
    [0,1,1,0,1,1,1],
    [1,0,0,0,1,1,1],
    [1,0,0,1,1,1,1]
])

m2 = np.array([
    [1,1,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1]
])

print(m,'\n \n',m1,'\n \n ',m2)   

def refle (m):
    if(np.diagonal(m).sum() == m.shape[0]):
        print('Es Reflexiva')
    else: 
        print('No es Reflexiva')
   

def sim(m): 
    if ((m == np.transpose(m)).all()):
        print('Es Simetrica')
    else:
        print('No es Simetrica')


def trans(m):
    M = m.dot(m)
    M[M>=1] = 1
    if ((m==M).all()):
        print('Es transitiva')
    else: print('No es transitiva')

print('\n \n La Primera Matriz es \n ')
refle(m)
sim(m)
trans(m)

print('\n \nLa Segunda Matriz es \n')
refle(m1)
sim(m1)
trans(m1)

print('\n \n La Tercera Matriz es \n ' )
refle(m2)
sim(m2)
trans(m2)




#{P2}
print("\n \nProblema 2\n \n")

A = np.arange(5,9).reshape(2,2)
B = np.arange(-7,-1).reshape(2,3)
C = np.arange(4,14,3).reshape(2,2)
D = np.identity(2)
E = np.zeros(6).reshape(2,3)

Z = np.vstack((A,D))
Y = np.vstack((D,C))
J =  np.vstack((E,B))
O = np.hstack((Z,Y))
H = np.hstack((O,J))

print("Matriz A \n " , A , '\n')
print("Matriz B \n " , B , '\n')
print("Matriz C \n " , C , '\n')
print("Matriz D \n " , D , '\n')
print("Matriz E \n " , E , '\n')


print('Matriz Resultante H \n \n ',H,'\n')
print()

#{P3}
print("\n \nProblema 3\n ")


P = np.arange(0,24).reshape(4,6)

print("\n \n Matriz Original \n \n",P)

def rota90(m):
    t = np.transpose(m)
    print(" \n \n 90 grados \n \n" , np.flip(t,0))
    
def rota180(m):
    print("\n \n 180 grados \n \n" , np.flip(m))

def rota270(m):
    t = np.flip(m,0)
    print("\n \n 270 grados \n \n" , np.transpose(t))

rota90(P)
rota180(P)
rota270(P)

def rota90_otro_lado(m):
    t = np.transpose(m)
    print(" \n \n 90 grados al otro lado \n \n" , np.flip(t,1))

def rota180_otro_lado(m):
    print("\n \n 180 grados al otro lado \n \n" , np.flip(m))

def rota270_otro_lado(m):
    t = np.transpose(m)
    print(" \n \n 270 grados al otro lado\n \n" , np.flip(t,0))

rota90_otro_lado(P)
rota180_otro_lado(P)
rota270_otro_lado(P)




#{P4}
print("\n \nProblema 4\n \n")


print('Forma de reglones X A Y B Z C T D')
a = np.array([
[2,1,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0],
[-1,2,0,0,0,0,0,0],
[0,0,2,1,0,0,0,0],
[0,0,1,1,0,0,0,0],
[0,0,-1,2,0,0,0,0],
[0,0,0,0,2,1,0,0],
[0,0,0,0,1,1,0,0],
[0,0,0,0,-1,2,0,0],
[0,0,0,0,0,0,2,1],
[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,-1,2]])

b = np.array([
    [4],
    [3],
    [3],
    [3],
    [2],
    [1],
    [6],
    [4],
    [2],
    [-3],
    [-1],
    [4]
])

x = np.linalg.lstsq(a,b,rcond=-1)
print(x)