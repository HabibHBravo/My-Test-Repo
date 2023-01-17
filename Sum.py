# Setup _very_ simple timing. 
import time 
start_time = time.time() 

sum = 0 
for i in range(0,100): 
    sum += i 
    #print(sum) 
 
# Output how long the process took. 
print ("--- %s seconds ---" % (time.time() - start_time)) 
print(sum)
