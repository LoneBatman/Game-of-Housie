'''
generates a ticket with 15 numbers, 5 in each row
'''
import random

class Ticket:

    def ticket_generator(self):
        ones=list(range(1,11))
        tens=list(range(11,21))
        twenties=list(range(21,31))
        thirties=list(range(31,41))
        forties=list(range(41,51))
        fifties=list(range(51,61))
        sixties=list(range(61,71))
        seventies=list(range(71,81))
        eighties=list(range(81,91))
        num_ranges=[ones,tens,twenties,thirties,forties,fifties,sixties,seventies,eighties]
        ticket=[]
        for num in num_ranges:
            x=random.randrange(0,10)
            ticket.append(num[x])
            num.remove(num[x])
            x=random.randrange(0,9)
            ticket.append(num[x])
        x=random.randrange(0,9)
        y=random.randrange(0,10)
        ticket.append(num_ranges[x][y])
        i=0
        while(i!=4):
            z=random.randrange(0,len(ticket)-i)
            ticket.remove(ticket[z])
            i+=1
        return ticket