#ex-1 DataFrame [The dataFrame is an objects of pandas]
import pandas as pd

data={
    "Name":["swapnil","krishna","krishna"],
    "age":[26,5,24]
}
df=pd.DataFrame(data)
print(df)

print('----------------------')

#ex-2 Series [it is one 1Diamensional labels of an array]
import pandas as pd

data=pd.Series([10,20,30,40,50])

print(data)

#ex- Custom index-
import pandas as pd

s=pd.Series([10,20,30],index=['a','b','c'])

print(s)

#ex- Access Values()
#uding indexing
print(s["b"])

print('-----------------------------------------')

#Series of Dictionary 
import pandas as pd

data={
    "name":"swapnil",
    "age":26,
    "sub":"python"
}
ans=pd.Series(data)
print(ans)

print('--------------------------------------------------')

#ex- DataFrame-[Excel table with rows and columns.]
import pandas as pd

data={
    "Name":["Rahul","Akash","Vishal","Kalpesh"],
    "Age":[35,25,23,26],
    "Marks":[87.55,65.05,75.45,82.14],
    "Rollno":[61,47,87,35]
}
result=pd.DataFrame(data)
print(result)

#ex- access column
# print(df["Name"])
print(result[["Name", "Marks"]])

#ex-shape- [to show the column and rows]
print(result.shape)

#ex-Access rows and column saperatly
print(result.shape[0])
print(result.shape[1])

#Ex-head()[is use to see the first row of DataFrame, just slicing type, select number of row]
print(result.head(2)) # First two row print
print(result.head(1))

#ex- tail() [is used to get the last rows of a DataFrame.]
print(result.tail(2)) #print the last two rows data record
print(result.tail(1))

#ex- info() [gives you complete basic information about your DataFrame.]
print(result.info())

print('-----------------------------------------------')

#ex- describe() [gives a statistical summary of the numeric columns in a DataFrame.]
import pandas as pd

data={
    "marks":[90.53,76.54,90.21,72.12],
    "price":[120,70,80,110]
}
s=pd.DataFrame(data)
print(s.describe())

#ex- loc[] [is used to select rows and columns by label/name. one person specific record return]
import pandas as pd 

data={
    "Name":["Rahul","Akash","Vishal","Kalpesh"],
    "Age":[35,25,23,26],
    "Marks":[87.55,65.05,75.45,82.14],
    "Rollno":[61,47,87,35]
}
result=pd.DataFrame(data)
print(result.loc[0])

#ex- select multiple rows
print(result.loc[0:1])
print(result.loc[3:4])

#ex- select specific rows+column
print(result.loc[2,"Marks"])

#ex- select rows and specific column
print(result.loc[0:2,["Name","Marks"]])

print('--------------------------------')

#ex- iloc[] [is used to select rows and columns using integer positions.]
print(result.iloc[0])
print(result.iloc[1])

#select multiple row
print(result.iloc[0:2])

print('---------------------------------')

#select row+column
print(result[0:4][0:3])

print('----------------------------Filtering DataFrame-----------------------------')

#ex- Filtering DataFrame [selecting only the rows that satisfy a condition.]
import pandas as pd

data={
    "Name":["Rahul","Akash","Vishal","Kalpesh"],
    "Age":[35,25,23,26],
    "Marks":[87.55,65.05,75.45,82.14],
    "Rollno":[61,47,87,35]
}
result=pd.DataFrame(data)
# print(result)

#Marks greater than 80
print(result[result["Marks"]>70])

print('--------------------------------')

#2. Age greater than 25
print(result[result["Age"]>18])

#3. Marks equal to 75.45
print(result[result["Marks"]==75.45])

print('---------------------------------')

#4. Multiple conditions — AND
print(result[(result["Age"]>22) & (result["Age"]<75)])

print('--------------------------------')

#5. Multiple conditions — OR
print(result[(result["Age"]>17) | (result["Age"]<75)])

print('-------------------------------Topic 12: Add, Update & Delete Columns--------------------------------------')

#Add, Update & Delete Columns 
#1. Add a new column
import pandas as pd

data={
    "sub":["Physics","Chemistry","Math"],
    "marks":[78,45,90]
}
ans=pd.DataFrame(data)
print(ans)

#Add a new column
ans["city"]=["pune","mumbai","Nashik"]
print(ans)

#Update a column
ans['marks']=ans['marks']+2
print(ans)

ans.loc[0,"marks"]=95
print(ans)

print('---------------------------------')

#4. Delete a column
ans=ans.drop("city",axis=1)
print(ans)

print('---------------------------------')

#ex- 5. Delete multiple columns
ans=ans.drop(["sub","marks"], axis=1, inplace=True)
print(ans)

print('------------------------Find missing values-------------------------------')

#1.isnull()
import pandas as pd

data={
    "Name":['Tushar','Yogesh','mohit'],
    "rollno":[41,12,54]
}
s=pd.DataFrame(data)
print(s)

#1.isnull() #return false
print(s.isnull())

#Remove missing rows — dropna()
print(s.dropna())

#3. Fill missing values — fillna()
s['rollno']=s['rollno'].fillna(0)
print(s)

print('---------------sort values----------------------------') #Ascending Descending

##ex- 1.Sort values Ascending
import pandas as pd

data={
    "Name":["Rakesh","jayesh","Yogesh","jayesh"],
    "Rollno":[54,22,90,34],
    "Age":[45,12,43,21]
}
result=pd.DataFrame(data)
print(result)

#Ascending:
print(result.sort_values("Rollno"))

print('------------------Descending------------------')

#Descending:
print(result.sort_values("Rollno",ascending=False))


print('---------------------------values count-----------------------------------')

#ex- values count()
print(result['Name'].value_counts()) #name count
print(result["Age"].value_counts()) #age count
print(result["Name"].value_counts(ascending=True))

print('-------------------------dropt duplicate---------------------------------')

#drop duplicate 
import pandas as pd

data={
    "Name":["Rakesh","jayesh","Yogesh","jayesh"],
    "Rollno":[54,22,90,22],
    "Age":[45,12,43,12]
}
result=pd.DataFrame(data)
print(result.drop_duplicates())

#check specific column
print(result.drop_duplicates(subset=["Name"]))

#Keep first duplicate
print(result.drop_duplicates(subset=["Name"],keep="first"))
#last duplicate
print(result.drop_duplicates(subset=["Name"],keep="last"))

print('---------------------------------rename()--------------------------------------')

#rename()
import pandas as pd

data={
    "Name":["Rakesh","jayesh","Yogesh","jayesh"],
    "Rollno":[54,22,90,22],
    "Age":[45,12,43,12]
}
result=pd.DataFrame(data)
print(result.rename(columns={"Rollno":"roll_no"})) #rename one column

print(result.rename(columns={"Name":"name","Rollno":"rollno","Age":"age"})) #rename multiple column

print('------------------------------csv--------------------------------')
#csv
import pandas as pd

data={
    "Name":["swapnil","krishna","Omma"],
    "marks":[77,90,62],
    "age":[24,23,37]
}
result=pd.DataFrame(data)
result.to_csv("student.csv",index=False)

#read csv
new_data=pd.read_csv("student.csv")
print(new_data)

print('-----------------------------astype()--------------------------------')

#astype()
print(result.dtypes)

#Convert int → float
result["age"]=result["age"].astype(float)
print(result.dtypes)

#Convert int → str
result["marks"]=result["marks"].astype(str)
print(result.dtypes)

#Convert str → int
# result["Name"]=result["Name"].astype(int)
# print(result.dtypes)

#Convert Multiple Columns
result=result.astype({
    "age":int,
    "marks":str
})
print(result.dtypes)

print('----------------------groupby()--------------------')

#groupby()
#single column
b=result.groupby("Name")["age"].mean()
print(b)

print('------------------------------')

#multiple column
a=result.groupby("Name")["age"].agg(["min","max","sum","count"])
print(a)

print('-------------------merge()-------------------')

#merge()
import pandas as pd

a1=pd.DataFrame({
    "stu_id":[1,2,3,4],
    "Name":["Paresh","Kishor","vishal","Dashrath"]
})
a2=pd.DataFrame({
    "stu_id":[1,2,3,4],
    "Name":["Rahul","Akshay","Rohit","Vijay"]
})
result=pd.merge(a1, a2, on="stu_id")
print(result)

print('---------------------------Types of Merge-------------------------')

#Types of Merge
#Inner Merge: [फक्त दोन्ही DataFrames मध्ये matching records]
x=pd.merge(a1,a2, on="stu_id", how="inner")
print(x)

#Left Merge [Left DataFrame मधील सर्व records ठेवतो]
y=pd.merge(a1,a2,on="stu_id", how="left")
print(y)

#Right Merge [Right DataFrame मधील सर्व records ठेवतो]
z=pd.merge(a1,a2,on="stu_id", how="right")
print(z)

#Outer Merge [दोन्ही DataFrames मधील सर्व records ठेवतो]
om=pd.merge(a1,a2, on="stu_id", how="outer")
print(om)

print('---------------------------concat()-------------------------------')

#concat() [concat() is used to combine two or more Pandas DataFrames.]
#ex-1
import pandas as pd

d1=pd.DataFrame({
    "Name":["krishna","kartik"],
    "rollno":[32,56]
})

d2=pd.DataFrame({
    "Name":["chetan","Omma"],
    "rollno":[46,77]
})

result=pd.concat([d1,d2])
print(result)

print('----------------------------------')

#reset index()
result=pd.concat([d1,d2], ignore_index=True)
print(result)

print('----------------------------apply()-------------------------------------')

#apply() [Pandas मधील apply() वापरून आपण DataFrame किंवा Series मधील values वर custom function लागू करू शकतो.]
#ex-1
import pandas as pd

data={
    "Name":["kishor","Gunvant","Tushar"],
    "age":[25,25,16]
}
ans=pd.DataFrame(data)
ans["new_age"]=ans["age"].apply(lambda x:x+5)
print(ans)

