import random

__import__("random")
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
       if low!=high:
           guess=random.randint(1,x)
       else:
           guess=low   #could be also high becuase they are equal
       feedback=input(f'Is {guess} is too high(H),too low(L) or correct(C)'.lower() )
       if feedback=='h':
           high=guess-1
       elif feedback=='l':
           low=guess+1
    print(f'Good job.You found {guess} correctly this time ')
computer_guess(8)

