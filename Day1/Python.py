
# ## Python Program

# In[27]:


# This is a variable 


# In[53]:


a,b,c,d,e = 10,20,30,40,50


# In[55]:


e


# In[26]:


a =10


# In[30]:


a = "This is India"


# In[31]:


len(a)


# In[32]:


a[4:7]


# In[38]:


a


# In[2]:


a = 'Hello'


# In[3]:


a = "ABC"


# In[4]:


b = "DEF"


# In[6]:


a +" " + b


# In[9]:


a * 2


# In[51]:


10+10


# In[52]:


20/2*5+6


# In[55]:


1999/23


# In[8]:


a = '5'


# In[6]:


a = int(a)


# In[9]:


a


# In[59]:


a = 18956422540


# In[10]:


a = 10


# In[12]:


a == 9


# In[8]:


if a==9:
    print("This is true")


# In[14]:


a = 100


# In[15]:


b = a


# In[16]:


b


# In[22]:


str = "my name is Sahil"
print(str.upper())


# In[23]:


str = "my name is Sahil"
print(str.lower())


# In[20]:


str = "my name is Sahil"
print(str.capitalize()) 


# In[25]:


b = len(str)
b


# In[28]:


# Capitalizes first letter of string
print(str.count("my")) # returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.


# In[29]:


print(str.find("me",4,len(str)))


# In[39]:


z = 'Fndia'


# In[40]:


z.find('i')


# In[45]:


z[3]


# In[94]:


a = 'this'


# In[95]:


a.upper()


# In[96]:


a.lower()


# In[47]:


print("HELLO".isupper())


# In[98]:


print("Hello".isupper())


# In[48]:


print(" ".isspace())


# In[52]:


str = "Hello World Hello World"
print(str.replace("Hello","Hi",1))


# In[9]:


str = 5


# In[10]:


a = [10,19]


# In[116]:


type(a)


# In[117]:


z = [19,238,'jashdkj']


# In[118]:


type(z)


# In[119]:


z


# In[121]:


del z[1]


# In[122]:


z


# In[123]:


z


# In[124]:


z.clear()


# In[125]:


z


# In[134]:


list1 = ['physics', 'chemistry', 1997, 2000];
print(list1)
del list1[2];
print("After deleting value at index 2 : ")
print(list1)


# In[130]:


print("Hello")


# In[129]:


a = input("Enter your name : ")
print("Hello",a)


# In[132]:


list1


# In[135]:


print(len(list1)) # length
print([1, 2, 3] + [4, 5, 6])


# In[1]:


str = "HelloWorld"
print(str.capitalize())


# In[6]:


print(str.count("o",0,len(str)))


# In[8]:


print(str.find("el",0,len(str)))


# In[14]:


list1 = ['physics', 'chemistry', 1997, 2000]



# In[19]:


print("This is first index value : ", list1[0])


# In[33]:


lst = [ 100,881, 2, 3, 4, 5, 6, 7 ]


# In[28]:


sorted(lst)


# In[29]:


lst.reverse()


# In[35]:


lst.sort()


# In[36]:


lst


# In[37]:


tup2 = (1, 2, 3, 4, 5, 6, 7 )


# In[40]:


tup2[0:5]


# In[41]:


A = {0, 2, 4, 6, 8} 
B = {1, 2, 3, 4, 5}


# In[42]:


A.union(B)


# In[43]:


A.intersection(B)


# In[46]:


B - A


# In[45]:


A ^ B


# In[47]:


a = {'name' : 'ABC',
    'Age':20}


# In[48]:


a


# In[49]:


a.keys()


# In[50]:


a.items()


# In[56]:


a = {'name' : ['ABC','BCD','hhh'],
    'Age':[20,56,77],
    'Email' :['a','d','d']}


# In[58]:


print(a)


# In[53]:


a = '4'


# In[54]:


a


# In[55]:


print(a)


# In[73]:


a = 1
for i in range(1,10):
    a*=i
a


# In[68]:


for i in range(1,3):
    print(i)


# In[78]:


a = 5
b = 10
if  a > 0  and  b > 0 :
    
    


# In[91]:


for i in range(1,20,2):
    if i == 15:
        break
    print(i)


# In[93]:


a = 0 
for i in range(1,101,2):
    a +=i
a


# In[1]:


for i in range(1,11//2):
    print(i)


# In[6]:


11//2


# In[8]:


start = 900
end = 1000
for num in range(start, end + 1):   
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[12]:


def summation(a,b):
    """Addition function"""
    return a + b
def Mutliplicaion(a,b):
    """Mutliplicaion function"""
    return a * b



a = 6#int(input("Enter value of a = "))
b = 78 #int(input("Enter value of a = "))

summ,v,w,sub = mitul(a,b)

print(f'Sum of {a} and {b} is {summ}')
print(f'multi of {a} and {b} is {v}')
print(f'Division of {a} and {b} is {w}')
print(f'sub of {a} and {b} is {sub}')


# In[26]:


l1 = list(map(int,input().strip().split()))
l2 = list(map(int,input().strip().split()))


# In[27]:


l1


# In[28]:


l2


# In[29]:


l1+l2


# In[54]:


def temp(b,*a):
    print(b)
    print(a)
temp(89,22,344)


# In[52]:


def printinfo(a):
    print("Hello")
    print("Prakash")
    print("Mitul")
    print(a)


    
        
printinfo(10)


# In[60]:





# In[4]:


class animal:
    def eat(self):
        print("Animal Class")

class dog(animal):
    def bark(self):
        print("Child class")


# In[6]:


c = dog()
c.eat()
c.bark()


# In[8]:


a = 10 
while a != 0:
    print(a)
    a -= 1


# In[1]:


class Calculator:

    def multiplyNums(x, y):
        return x + y

# create addNumbers static method
Calculator.multiplyNums = staticmethod(Calculator.multiplyNums)

print('Product:', Calculator.multiplyNums(15, 110))


# In[3]:


class Calculator:

    # create addNumbers static method
    @staticmethod
    def multiplyNums(x, y):
        return x + y

print('Product:', Calculator.multiplyNums(15, 110))


# In[4]:





# In[ ]:




