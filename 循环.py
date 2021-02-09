i=1
sum=0
while i<=20:
	print("第",i,"年到了。。。。")
	if i==10:
		print("今年你受伤了，就不用给了")
		i=i+1
		continue
		#break 结束本次循环
		
	j=1
	while j<=12:

		if j==6:
			print("第",i,"年,第",j,"月到了，这个月不用给")
			j=j+1
			continue
		sum=sum+0.1
		print("第",i,"年,第",j,"月，支付彩礼0.1万！累计已经支付：",round(sum,2),"万")
		j=j+1
	

	i=i+1	