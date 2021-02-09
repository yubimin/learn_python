from multiprocessing import Process
import time

def run(name):
	print(name,"进程执行了！")
	time.sleep(5)

if __name__ == '__main__':
	#创建线程
	p1=Process(target=run,args=("p1",)) 
	p2=Process(target=run,args=("p2",)) 
	p3=Process(target=run,args=("p3",)) 
	p4=Process(target=run,args=("p4",)) 
	p5=Process(target=run,args=("p5",)) 

	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()

	print("进程执行完毕")

#多进程可以真正实现同一时间多个任务并行