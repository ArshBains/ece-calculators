import numpy as np
import math

class Array: 
    TCHEBYSCHEFF = [[0,0,0,0,0,0,0,0,0,1],                  #T0
                    [0,0,0,0,0,0,0,0,1,0],                  #T1
                    [0,0,0,0,0,0,0,2,0,-1],                 #T2
                    [0,0,0,0,0,0,4,0,-3,0],                 #T3
                    [0,0,0,0,0,8,0,-8,0,1],                 #T4
                    [0,0,0,0,16,0,-20,0,5,0],               #T5
                    [0,0,0,32,0,-48,0,18,0,-1],             #T6
                    [0,0,64,0,-112,0,56,0,-7,0],            #T7
                    [0,128,0,-256,0,160,0,-32,0,1],         #T8
                    [256,0,-576,0,432,0,-120,0,9,0]]        #T9
    # for coff in TCHEBYSCHEFF:
    #     print(np.poly1d(coff))

    def __init__(self, n, sll, d=1/2):
        self.n = n
        self.sll = sll
        self.r = self.calc_r(self.sll)
        self.m = n-1
        self.d = d
        self.x0 = self.x_0(self.r, self.m)
        self.c = self.coff(self.n)

    def calc_r(self, sll):
        r = math.pow(10, sll/20)        #antilog
        return round(r, 2)

    def x_0(self, r, m):
        x_0 = ( math.pow( r + math.pow(math.pow(r, 2)- 1, 1/2),1/m ) + math.pow( r - math.pow(math.pow(r, 2)- 1, 1/2),1/m ) )/2
        return round(x_0, 4)

    def coff(self, n):
        #En(z)=Tn-1(x)
        E_2Dmatrix = []
        if n % 2 == 0:
            for x in range(1, n, 2):
                E_2Dmatrix.append(self.TCHEBYSCHEFF[x])
        else:
            for x in range(0, n, 2):
                E_2Dmatrix.append(self.TCHEBYSCHEFF[x])
        E_2Dmatrix = np.array(E_2Dmatrix).transpose()
        r = E_2Dmatrix
        r=r[~np.all(r == 0, axis=1)]        #remove all zero rows
        T_x = self.TCHEBYSCHEFF[n-1]
        degree = 9
        Tx = []
        for x in T_x:
            if x != 0:
                Tx.append(x*math.pow(self.x0, degree))
            degree = degree - 1
        coefficient = np.linalg.inv(r).dot(Tx)
        coefficient = [round(coff,3) for coff in coefficient]
        # print(coefficient)
        return coefficient
        

    def results(self):
        print("\nSide lobe level below main lobe maximun in dB = 20log(r)")
        print("{}=20log(r)".format(self.sll))
        print("r={};\n".format(self.r))
        print("n = {0};\nm = n-1\n∴ m = {0}-1 = {1};\n".format(self.n, self.m))
        print("Tchebyscheff polynomial of degree m is T{}(x0)".format(self.m))
        print("T{}(x0)=r".format(self.m))
        print("------------------- REPLACE (x with x0) -------------------------")
        print(str(np.poly1d(self.TCHEBYSCHEFF[self.m]))+ " = {}".format(self.r))
        print("-----------------------------------------------------------------")
        print("x0 = {}\n".format(self.x0))
        print("VALUES OF COEFFICIENTS")
        x=0
        for a_x in self.c:
            print("a_{} = {}".format(x, a_x))
            x=x+1


d_tche = Array(7, 20)       #Array(no. of sources, side lobe level)
d_tche.results()
