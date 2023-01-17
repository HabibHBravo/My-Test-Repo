# Simulates 10K game of Hi Ho! Cherry-O 
# Setup _very_ simple timing. 
import time 
start_time = time.time() 
import multiprocessing 
from statistics import mean 
import random 
numGames = 20000

def cherryO(game): 
    spinnerChoices = [-1, -2, -3, -4, 2, 2, 10] 
    turns = 0 
    cherriesOnTree = 10 

    # Take a turn as long as you have more than 0 cherries 
    
    while cherriesOnTree > 0: 
        # Spin the spinner 
        spinIndex = random.randrange(0, 7) 
        spinResult = spinnerChoices[spinIndex] 
        # Print the spin result     
        #print ("You spun " + str(spinResult) + ".") 
        # Add or remove cherries based on the result 
        cherriesOnTree += spinResult 
        # Make sure the number of cherries is between 0 and 10    
        if cherriesOnTree > 10: 
            cherriesOnTree = 10 
        elif cherriesOnTree < 0: 
            cherriesOnTree = 0 
        # Print the number of cherries on the tree        
        #print ("You have " + str(cherriesOnTree) + " cherries on your tree.")
        turns += 1 
    # return the number of turns it took to win the game 
    return(turns) 

def mp_handler(): 
    with multiprocessing.Pool(multiprocessing.cpu_count()) as myPool:
       ## The Map function part of the MapReduce is on the right of the = and the Reduce part on the left where we are aggregating the results to a list. 
       turns = myPool.map(cherryO,range(numGames)) 
    # Uncomment this line to print out the list of total turns (but note this will slow down your code's execution) 
    #print(turns) 
    # Use the statistics library function mean() to calculate the mean of turns 
    print(mean(turns)) 

if __name__ == '__main__': 
    mp_handler() 
    # Output how long the process took. 
    print ("--- %s seconds ---" % (time.time() - start_time))