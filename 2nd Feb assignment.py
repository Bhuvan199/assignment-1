#!/usr/bin/env python
# coding: utf-8

# Q.1 - Explain with an example each when to use a for loop and a while loop. 

# In[20]:


# for loop is used when the iteration is known . 
# for ex..

for i in range(0,5):
    print("iteration is ",i)  # here we know iteration is 5..i.e..(0,1,2,3,4)


# In[21]:


# while loop is used when we dont know iteration and while loop executes until the condition become false
# for ex...

count = 0
while count<9:
    print("hi")
    count = count+1
# as the values of count becomes 9 ..condition becomes false and terminate loop


# Q2.  Write a python program to print the sum and product of the first 10 natural numbers using for  and while loop. 
# 

# In[25]:


n = int(input("enter any number"))

sum = 0
prod = 1
for i in range(1,n+1):
    sum = sum + i
    prod = prod * i
    
print("the sum is ",sum,"and product is ",prod)

    
    


# In[19]:


n = int(input("enter any number"))
summer= 0
prod = 1
counter = 1

while counter<n+1:
    summer = summer+counter
    prod = prod*counter
    counter = counter+1
    
print("the sum is ",sum,"and product is ",prod)


# Q3. Create a python program to compute the electricity bill for a household. 
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per  unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will  be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit. 
# You are required to take the units of electricity consumed in a month from the user as input. 
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is  310, the total electricity bill should be 2250. 
# 

# In[3]:


n = int(input("electricity consumed in a month "))

if n <=100:
    print("electricity bill =",n*4.5)
elif n <=200:
       print("electricity bill =",(n*4.5)+(n-100)*6)
elif n <= 300:
       print("electricity bill =",(100*4.5)+(100*6)+(n-200)*10)
else:
       print("electricity bill =",(100*4.5)+(100*6)+(100*10+(n-300)*20))
    
    


# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each  number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print  that list. 
# 

# In[4]:


l = []
for i in range(1,101):
    l.append(i)
    


new_l = []
for i in l:
    if i**3 % 4 ==0 or i % 5 == 0:
        new_l.append(i)
print(new_l)
    


# In[5]:


l = []
for i in range(1,101):
    l.append(i)

    
new_l = []
counter = 1
while counter <= len(l):
    if counter**3 % 4 == 0 or counter**3 % 5 == 0:
        new_l.append(counter)
    counter = counter+1
print(new_l)


# Q5.  Write a program to filter count vowels in the below-given string. 
# string = "I want to become a data scientist" 
# 

# In[23]:


s = "I want to become a data scientist"
s = s.lower()
count = 0
for i in range(0,len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o"  or s[i] == "u":
        count = count+1
print(count)


# In[ ]:




