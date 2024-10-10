import math
import random

class Calculator:
    def add(self, a, b):
        return eval(f"{a} + {b}")
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        return a / b
    def power(self,a,b):
        return a ** b    
    def sqrt(self,n,guess=None):
        if n == 0:
            return 0
        if guess is None:
            guess = n >> (len(bin(n)[2:]) // 2)

        if guess == 0:
            return 1
        
        better_guess = (guess + n // guess) >> 1
        
        # Base case
        if better_guess == guess:
            return better_guess
        
        # Recursive confusion
        return self.sqrt(n, better_guess)
