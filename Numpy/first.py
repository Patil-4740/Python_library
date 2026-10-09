import numpy as np 

number=np.array([10,20,30,40,50])
print(number)

#ex- add of two array
a=np.array([1,2,3])
b=np.array([1,2,3])

print(a+b)

#ex demo 
import numpy as np

numbers=np.array([5,10,15,20,25])

print(numbers)
print(numbers+5)
print(numbers*5)

#propertise of array
import numpy as np

numbers=np.array([10,20,30,40])
print(numbers.ndim) #Array diamension
print(numbers.size) #Array size
print(numbers.shape) #Array shape

print('---------------indexing-----------------')

#ex-1 indexing positive
import numpy as np

num=np.array([10,20,30,40,50])
print(num[0])
print(num[1])
print(num[4])

print('--------------------------')

#ex-2 indexing negative
import numpy as np

num=np.array([10,20,30,40,50])
print(num[-1])
print(num[-3])
print(num[-4])

print('----------slicing-------------')

#ex- positive slicing
import numpy as np 

name=np.array(['swapnil','krishna','chetan','vinod','kartik'])
print(name[1:4])
print(name[0:5:2])
print(name[0:5:3])

print('--------------------')

#ex- negative slicing
import numpy as np

num=np.array([10,20,30,40,50])
print(num[-1:-5:-1])
print(num[-1:-6:-2])
print(num[-1:-6:-3])

print('-------------------2D Array----------- ')

#ex-1 2d array
import numpy as np 

num=np.array([[10,20,30],
              [40,50,60]])
print(num)

#ex- accessing element 2d array
print(num[0,0])
print(num[0,1])
print(num[1,2])

#check shape
print(num.shape)

print('-----------------------')

#ex-3 practise excersise
import numpy as np

num=np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(num[1,0])
print(num[2,0])
print(num.shape)

print('------------------------slicing---------------------------------')

#ex-1
import numpy as np

num=np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(num[0]) #first index
print(num[1]) #second index
print(num[2]) #Thired index

#Get multiple rows
print(num[0:2])

#Ex-1
print(num[:,0])
print(num[:,1])
print(num[:,2])

print('-----------------------')

#Ex-2 slicing
print(num[0:2, 1:3])

print('----------------------reshape----------------------------------')

#reShape() [To change the array shape do not change the element]
import numpy as np 

num=np.array([10,20,30,40,50,60])
print(num)
print(num.shape)

#arrage number
print(num.reshape(2,3))
print(num.reshape(3,2))

#flatten()[means 2D is convert to 1D]
import numpy as np

num=np.array([[1,2,3],
              [3,4,5]])
print(num.flatten())

#ravel() [2D is making to 1D]
import numpy as np

num=np.array([[1,2,3],
              [3,4,5]])
print(num.ravel())

#transpose() [interchange row-column, row la column karat and column la row karat]
import numpy as np

num=np.array([[10,20,30],
              [40,50,60]])
print(num.transpose())

#cancatinate() [To array joinning]
import numpy as np

First_name=np.array(['swapnil'])
last_name=np.array(['patil'])
print(np.concatenate((First_name,last_name)))

#vstack() [mean to joing upper lower]
import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.vstack((a,b)))

#hstack() [To join the near by array]
import numpy as np

a=np.array([1,2,5])
b=np.array([4,3,6])
print(np.hstack((a,b)))

#spliting() [means breaking one array into small array]
import numpy as np

num=np.array([1,2,3,4,5,6])
print(np.split(num,2))

#max(), min(), sum(), mean()
import numpy as np

num=np.array([10,20,30,40,50,60,70])

print(num.max())
print(num.min())
print(num.sum())
print(num.mean())

#ex-axis() tells NumPy which direction to calculate.
import numpy as np

num=np.array([[10,20,30],
              [40,50,60]])
print(num.sum(axis=1))


#ex-Boolean indexing() Boolean indexing means filtering values using a condition.
import numpy as np

num=np.array([10,20,30,40,50,60,70])
print(num[num>25])

#ex= where() finds positions (indexes) where a condition is True
import numpy as np

num=np.array([10,20,30,40,50,60,70])
print(np.where(num>30))

#ex- random number()
import numpy as np

print(np.random.randint(1,10))

#sorting in numPy [To sort the array by using numpy built in function through] descending to ascending
import numpy as np

num=np.array([1,5,3,2,6,4])
print(np.sort(num))

#ex-2 Ascending 
import numpy as np

num=np.array([1,5,3,2,6,4])
print(np.sort(num))

#ex- Descending
import numpy as np

num=np.array([1,3,2,4,5])
print(np.sort(num)[::-1])

