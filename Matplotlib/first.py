#plot()[is use for line graph draw]
# import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[10,20,15,30]

# plt.plot(x,y)
# plt.show()

#lables and table
# import matplotlib.pyplot as plt

# x=[1,2,3]
# y=[5,10,15]

# plt.plot(x,y)
# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.title("Display Sells")
# plt.show()


#plt.bar() चा वापर categories मधील values compare करण्यासाठी केला जातो
# import matplotlib.pyplot as plt

# name=["swapnil","krishna","chetan","vinod","kartik"]
# marks=[88,59,90,35,67]

# plt.bar(name,marks)
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title("Student Details")
# plt.show()

#plt.scatter()[relateion between two numeriacal values]
# import matplotlib.pyplot as plt

# age=[66,18,29,23]
# salary=[16000,33500,49,10000]

# plt.scatter(age,salary)
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.title("Person Details")
# plt.show()

#plt hits() [it shows the distribution of numerical data.]

# import matplotlib.pyplot as plt 

# marks=[45,56,76,89,90,53,78,85,50]

# plt.hist(marks)
# plt.xlabel("Marks")
# plt.ylabel("Number of Student")
# plt.title("Student Marks")
# plt.show()

#pie() [It shows how different categories contribute to a whole.]
# import matplotlib.pyplot as plt 

# subject=['python','java','mysql','.net']
# marks=[55,78,90,85]

# plt.pie(marks,labels=marks)
# plt.xlabel("Subject")
# plt.ylabel('Marks')
# plt.title('Subject and Marks')
# plt.show()

#plt.legend() [is used to identify different data series in a graph.]

# import matplotlib.pyplot as plt

# month=[1,2,3,4]
# sales=[100,250,700,650]
# profit=[10,20,30,40]

# plt.plot(month,sales,label='sales')
# plt.plot(month,profit,label='profit')

# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.title("Sales and Profit")
# plt.legend()
# plt.show()

#plt.grid() is used to add grid lines to a graph. Grid lines make it easier to read and compare values.
# import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[10,20,30,40,50]

# plt.plot(x,y)
# plt.xlabel('Dayes')
# plt.ylabel('Sales')
# plt.title('Days and Sales')

# plt.grid()
# plt.show()

#plt.figure() [is used to create a new figure (canvas) for plotting.]
import matplotlib.pyplot as plt 

plt.figure(figsize=(8,10))

x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.plot(x,y)
plt.xlabel("Sales")
plt.ylabel("Graph")
plt.title('Sales and Graph')
plt.show()


