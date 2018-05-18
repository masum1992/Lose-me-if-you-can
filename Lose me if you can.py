import numpy as np
import random
import copy
import time


#  ------------------------------------------------------------------------------------------------function section ------------------------------------------------------------------------------------------------

def flor(q):
        for i in range(len(q)):
                q[i]=map(int,q[i])



def random_func(inp,r):
        action=[]
        for i in range(len(r[inp])):
                if r[inp][i]>=0:
                        action.append(i)
        return random.choice(action)  


def max(next,q):
        a=copy.deepcopy(q)
        a[next].sort()
        return a[next][-1]

def select_max(indx,tmp):
        add=[]
        a=copy.deepcopy(tmp)
        a[indx].sort()
        a=a[indx][-1]
        if a==0:
                return random.choice([0,1,2])
        else:
                frequency=tmp[indx].count(a)
                if frequency>1:
                        for i in range(len(tmp[indx])):
                                if tmp[indx][i]==a:
                                        add.append(i)

                        return random.choice(add)
                else:
                        a= tmp[indx].index(a)
                        return a
        

def training():

        print 'Training time is going on: '
        for i in range(10):
                
                current=15
                next_action=0
                while(current !=0 and current !=1):
                        
                        action=random_func(current,r)

                        if action==0:
                                        next_action=current-2
                        elif action==1:
                                        next_action=current-3
                        else:
                                        next_action=current-5
                                        
                        qmax=max(next_action,q)

                        learn_value=r[current][action]+Gamma*qmax

                        q[current][action]=learn_value
    
                        current=next_action



def play_human(chal,left_dice):
        moves=[2,3,5]
        while(1):
                if chal not in moves:
                        print 'Invalid move'
                        chal=input("\nGive your Move: ")
                else:
                        break
        return left_dice-chal
        
def play_machine(left_dice,q):

        if left_dice>1:
                
                chal=select_max(left_dice,q)
        
                if chal==0:
                        print '\nMachine gave -> ',2
                        return left_dice-2
                elif chal==1:
                        print '\nMachine gave -> ',3
                        return left_dice-3
                else:
                        print '\nMachine gave -> ',5
                        return left_dice-5
        else:
                print 'You lose the game'
                return -1
        
# ------------------------------------------------------------------------------------------------end of function section  ------------------------------------------------------------------------------------------------

        
r=[[-1,-1,-1], [-1,-1,-1], [100,-1,-1], [100,100,-1], [0,100,-1], [0,0,100], [0,0,100], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ]

#q=np.array([[0 for i in range(6)] for i in range(6)])

q=[[0 for i in range(3)] for i in range(16)]

Gamma=.8

session=0

for i in range(10):
        training()
        time.sleep(2)
        print '\n\n Available moves -> 2 , 3 , 5 \n\n'
        flor(q)
       
        tmp=copy.deepcopy(q)
        total_dice=15
        left_dice=total_dice

        o=0
        #session+=1
        #print  'session %d is running\n\n'%(session)
        while(1):
                o+=1
                print 'Total number of dices are left -> ',left_dice
                
                if o%2!=0:
                        if left_dice>1:
                                left_dice=play_human(input("\nGive your Move: "),left_dice)
                                print 'After your\'s  Turn -> ',left_dice
                        else:
                                time.sleep(3)
                                print '\nYou lose '
                                break
                else:
                        if left_dice>1:
                                time.sleep(3)
                                left_dice=play_machine(left_dice,q)
                                print 'After machine\'s Move -> ',left_dice
                        else:
                                time.sleep(3)
                                print '\nMachine lose'
                                break


        time.sleep(2)
        opinion=raw_input("\n\n\nDo you want to play another session? \n 1. Yes\n 2. No \n")
        
        if opinion=='yes' or opinion=='Yes':
                pass
        elif opinion=='no' or opinion=='No':
                break
        else:
                pass

        
