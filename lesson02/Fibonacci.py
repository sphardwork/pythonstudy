#find out Fibonacci sequence
#times是找出的个数
times=2
now=1
before=now
#打印出第一个和第二个数字
print('the 1 Fibonacci sequence is 1')
print('the 2 Fibonacci sequence is 2')


while(times<100):
    #把当前数值存在临时变量temp中
    temp=now
    #进行移动
    now+=before
    #更新before,并增加times
    times+=1
    before=temp
    print('the',times,'Fibonacci sequence is ',now)
