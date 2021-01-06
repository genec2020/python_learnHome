#等腰三角形(1,3,5,7) 3个while
row = 15 #行数
#第一行实际占位数 19, 需要在(18/2+1=10)号实体打印   10
#第二行实际占位数也是19   需要在9,10,11号实体打印    9
#第三行实际占位数19,  需要在8,9,10,11,12号实体打印  8
col = row*2-1 #列数
row_bigen = 1
while row_bigen <= row:
    col_begin=1
    while col_begin <= col:
        if col_begin >= row+1-row_bigen and col_begin<= row-1+row_bigen:
            print('*',end='')
        else:
            print(' ',end='')
            pass
        col_begin+=1
        pass
    print() #换行
    row_bigen+=1
    pass
