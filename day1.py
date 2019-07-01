print('trust yourself，change yourself')  #打印
print(10)
print(1024+998+324) #加减计算
print(328-64)
print( 100*1.001*1.001*1.001*1.001*1.001)


a = 5
b = 3
print( 4*a + 3*b )

# day1 = 100 + 100 * 0.1
# day2 = day1 + day1 * 0.1
# day3 = day2 + day2 * 0.1
# day4 = day4 + day4 * 0.1
# day5 = day5 + day5 * 0.1

import keyword
print(keyword.kwlist)

print(2**10)
print(5%2)
print(5/2)
print(1<2)
print(1>2)
print(1<=2)
print(1>=2)
print(1==2)
print(1==1)
print(2!=1)
print(1!=1)

a = 0
a += 5
a -= 5
print(a)

a=5
a *= 5
a /= 5
print(a)

#交换变量
i = 5
j = 11
i += j
j = i - j
i -= j
print(i,j)

i , j  = j ,i
print(i,j)

a, b, c, d = 1,2,3,4
a, b, c, d,= d,c,a,b
print(a,b,c,d)

#变量赋值
i ,j = 5 ,11
print(i,j)

#三引号
b = '''
我是姜姜
  啦啦啦啦
'''
print(b)

p ='''today      my heed really aches because of the bad smell but i really feel  happy  as 
,i Made a lot of new friends they have different backgrounds   
,but we have the same goal that is : to learn python for a better job'''

print(p.capitalize())
print(p.replace('the','yyyyyy'))
print(p.count('t'))
print(p.upper())
print(p.lower())
print(p.isupper())
print(p.islower())
print(p.isdigit()) #是否全为数字
print(p.find('ppppp'))
#print(p.index('ppppp'))

jiang = '01234567890'
print(jiang.index('4'))
print(jiang[-7])
print(jiang[6:9:2])
print(jiang[0:1])
print(jiang[0:12:2])
print(jiang[:7])
print(jiang[2::2])