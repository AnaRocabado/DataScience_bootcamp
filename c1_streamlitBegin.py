import streamlit as st
from PIL import Image


image = Image.open('pythonimg.jpeg')



st.write("""
# 10 Cool Beginner Python Tricks That Will Make Your Life Easier
""")

st.image(image, caption='Photo by Miesha Maiden from Pexels')

st.write("""
## 1. Walrus operator


The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.


If we want to check and print the length of a list:


*Example*

```python
Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)
```

*Output*

```python
3
```


""")

st.write("""
## 2. Splitting a string


If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!


*Example*
```python
string = “hello world”
string.split()

```

*Output*
```python
[‘hello’, ‘world’]
```

""")


st.write("""
## 3. Reversing a string


If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.


*Example*
```python
str=”hello world!”
a=str[::-1]
print(a)
```

*Output*
```python
!dlrow olleh
```

""")


st.write("""
## 4. Merging two dictionaries


This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:


*Example*
```python
d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)

```

*Output*
```python
{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}

```

""")


st.write("""
## 5. The zip() function


The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.


*Example*
```python
colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)

```

*Output*
```python
red apple
yellow banana
green mango

```

The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.


*Example*
```python
students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)

```

*Output*
```python
{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}

```

""")


st.write("""
## 6. Assigning multiple list values to a variable


If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:


*Example*
```python
mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)

```

*Output*
```python
a = 1
b = [2, 3, 4, 5]

```

This process is also called list unpacking and you can apply this method for more than 2 variables also!

""")


st.write("""
## 7. Remove duplicate list items


Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.



*Example*
```python
mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)

```

*Output*
```python
{1, 2, 3, 4, 5, 6, 7, 8, 9}

```

""")

st.write("""
## 8. Lambda function


If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.


*Example*


Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :


```python
mul = lambda a,b: a*b
mul(5,6)
Output

```

*Output*
```python
30

```

""")


st.write("""
## 9. Swapping variable value


One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:


*Example*
```python
a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)

```

*Output*
```python
a = 200
b = 100

```

""")



st.write("""
## 10. Use a password in your code

This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!


*Example*
```python
from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)
```

*Output*
```python
password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password
```

""")



st.write("""
## Conclusion


These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.

Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.

However, the recommended resource is experienced by me and helped me in my data science career journey.


""")
