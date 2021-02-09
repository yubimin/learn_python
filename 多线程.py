#邮件发送方（发送方地址，发送方客户端授权密码，smtp地址）
#邮件内容
#邮件接收方
import threading
lock=threading.Lock() #创建一个线程锁（互斥锁）

num=100

def run(name):
	lock.acquire()  #设置锁
	global num  #
	num=num-1
	print("线程",i,"执行了，目前num的值为：",num)
	lock.release()	#释放锁	

for i in range(100):
	t=threading.Thread(target=run,args=(i+1,))
	t.start()

#全局解释器锁（GIL）
#不管cpu有多少个核，都保证python程序中同一时间点只能执行一个线程
#使用多进程解决GIL所造成的问题

