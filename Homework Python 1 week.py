#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
print (a, "is of type", type (a))


# In[2]:


b = 3.14


# In[5]:


print (b, "is of type", type (b))


# In[7]:


c = ("Big Data!")


# In[8]:


print (c, "is of type", type (c))


# In[11]:


d = ('Big data!')


# In[12]:


print (d, "is of type", type (d))


# In[13]:


e = True


# In[14]:


print (e, "is of type", type (e))


# In[15]:


f = False


# In[16]:


print (f,"is of type", type (f))


# In[17]:


e = [1,2,"intruder",3]
print (e, "is of type", type (e))


# In[40]:


for i in range(0,100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif 1 % 5 == 0:
        print("buzz")
        continue
    print(i)


# In[19]:


total_sum = 0 
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print (total_sum)


# In[23]:


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
word = "concOrdIa"
empty_string = ""
for letter in word:
    if letter not in vowels:
        empty_string += letter

print(empty_string)


# In[ ]:





# In[25]:


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('Babak Khosravifar'))


# In[4]:


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('This is Phyton. Phyton is fun!'))


# In[7]:


items = input("Input comma separated sequence of words" )
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


# In[ ]:





# In[ ]:




