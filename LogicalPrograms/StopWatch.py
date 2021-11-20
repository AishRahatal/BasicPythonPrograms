'''	
@Author: Aishwarya
@Date: 2021-11-18 
@Last Modified:2021-11-19
@Title : Stop Watch
'''
########################################################################################################
import time

def stop_watch():
    """"
    Description: printing the time elapsed 
    Parameter: none

    Return: none
    """
    try:
        input("Press Enter to start and ctr+c for stop the watch:") 
        #variable stores current time  in format hour :minutes:seconds
        start_time=time.time()
        print("Stopwatch has started")
        while True:
            #printing second by deducting start_time from current time 
            print("Time elapsed:" ,round(time.time()-start_time,0),'secs',end='\n')
            #sleep() is used to delay execution
            time.sleep(1)
    except KeyboardInterrupt: # it is an exception occured by pressing ctr+c while running program
        print("Stopwatch has stopped")
        #it will store the current time
        end_time=time.time()
        #printing total time elapsed from start_time to end_time
        print("The time elapsed:",round(end_time-start_time,2),'secs')
    

if __name__=='__main__':
    stop_watch()


