import math

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        return a / b
    def square_root(self,x):
        return math.sqrt(x)
    def power(self,a,b):
        return a ** b 
    def factorial(self,n):
        return math.factorial(n)
    def fibonacci(self, n):
        __=lambda f,n:n*f(f,n-1)if n>1 else 1
        return __((lambda s,x:s(s,x)), n)
