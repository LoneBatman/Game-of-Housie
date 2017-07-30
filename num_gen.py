'''
generates numbers from 1 to 100 randomly, without repetitions
'''
import random

class Number:
    generated_numbers=[]
    
    def num_generator(self):
        while(1):
            num=random.randrange(1,91)
            if(num not in Number.generated_numbers):
                Number.generated_numbers.append(num)
                break
        return num
    @staticmethod
    def get_generated_numbers():
        return Number.generated_numbers
