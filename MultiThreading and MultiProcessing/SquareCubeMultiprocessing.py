import time
import multiprocessing

Numbers=[i for i in range(5)]

def FindSquare(List):
    for i in List:
        time.sleep(3)
        print(i*i)
def FindCube(List):
    for i in List:
        time.sleep(3)
        print(i*i*i)
        
#without Multiprocessing


StartTime=time.time()
FindSquare(Numbers)
FindCube(Numbers)
EndTime=time.time() - StartTime
print(f"Execution was completed in {EndTime}")
        

if __name__ == '__main__':
    starttime=time.time()
    p1=multiprocessing.Process(target=FindSquare,args=(Numbers,))
    p2=multiprocessing.Process(target=FindCube,args=(Numbers,))
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    endtime=time.time()-starttime
    
    print(f"Execution was completed in {endtime}")
