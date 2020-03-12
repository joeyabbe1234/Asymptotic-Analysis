import matplotlib.pyplot as plt
import math

n = int(input("enter a number: "))
acc = []
def logarithmic(n):

    print(math.log(n))
    acc.append(math.log(n))

def linearithmic(n):

    print(n*math.log(n))
    acc.append(n*math.log(n))

def linear(n):

    print(n)
    acc.append(n)

def quadratic(n):

    print(n**2)
    acc.append(n**2)

def polynomial(n):

    print(n**3)
    acc.append(n**3)

def exponential(n):

    print(2**n)
    acc.append(2**n)

logarithmic(n)
linearithmic(n)
linear(n)
quadratic(n)
polynomial(n)
exponential(n)

x = ["Logarithmic","Linearithmic","Linear","Quadratic","Polynomial","Exponential"]
y = acc
plt.xlabel('Functions')
plt.ylabel('Result')
plt.plot(x, y)
plt.title("Asymptotic Analysis")
plt.show()