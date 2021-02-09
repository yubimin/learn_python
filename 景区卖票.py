import threading

lock=threading.Lock() #创建一个线程锁（互斥锁）
num=100

#买票
def sale(name):
	lock.acquire()  #设置锁
	global num
	if num>0:
		num=num-1
		print(name,"卖出一张票，还剩",num,"张票")
	lock.release()	#释放锁

#程序执行时，程序本身就是一个线程，叫主线程
#手动创建的线程，叫子线程
#主线程的执行中，不会等待子线程执行完毕，就会直接执行后面的代码
#售票窗口（2个线程）
while 1==1:
	if num>0:
		ta=threading.Thread(target=sale,args=("A窗口",))
		tb=threading.Thread(target=sale,args=("B窗口",))
		ta.start()
		tb.start()
		ta.join() #等待子线程执行完毕之后再执行主线程后面的内容
		tb.join() #等待子线程执行完毕之后再执行主线程后面的内容
	else:
		break
print("票已经卖完")