list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list1,list2,list3)
a=[0,1,2,3,4,5,6]
print(a)
"""
for i <= len(a):
	printa[i]
	"""
i=0
while  i<len(a):
     print("a[",i,"]is:",a[i])
     i=i+1	
aa="Hello" + " " + "World"     
print(aa)
print(len(aa))
z=aa.find("H")	
print(z)
i=0
while i<len(aa):
	print(aa[i])
	i+=1
z=aa.find("h")	
print(z)
zz='This is a book'.split(' ')
print(zz)
aa={'table': 100, 'xiao': 100}
print('----------------------------------')
import bisect
import random
SIZE=7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
print(aa)