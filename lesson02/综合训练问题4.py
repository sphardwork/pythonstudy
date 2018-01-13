s,i=0,0  #phthon语言特色，相当于s=0,i=0；两句
while True:    #死循环（须用break退出，return也可，但不推荐）
    i+=1
    if i%2==1:continue   #如果是奇数则无需继续，直接跳下一次循环
    cs,ci=0,i
    while ci>0:
        cs+=ci%10   #取出当前个位
        ci//=10      #取十位的数
    if cs==9:
          s+=1
          print(i)
    if s==10:break        #只需要10个
    
