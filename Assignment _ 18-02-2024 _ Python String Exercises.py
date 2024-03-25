#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


a = "tutor joes"
len(a)


# In[7]:


tj = "tutorjoes"
tfrq = {}
for i in tj:
    if i in tfrq:
        tfrq[i] += 1
    else:
        tfrq[i] = 1
print(tfrq)


# In[25]:


cstr="tutor joes"
print("Original String :",cstr)
ch1 = cstr[0]
cstr = cstr.replace(ch1, '@')
cstr = ch1 + cstr[1:]
print("Replaced String :",cstr)


# In[27]:


a = 'abc'
b = 'xyz'
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)


# In[29]:


def remove_ch(str, n):
      a = str[:n] 
      b = str[n+1:]
      return a + b
print(remove_ch('Tutor Joes', 2))


# In[31]:


str = "Python"
print("Before Swap -",str)
s = str[0]
e = str[-1]
res = e + str[1:-1] + s
print("After Swap -",res)


# In[33]:


str="Computer Education"
res = ""
print("String -",str) 
for i in range(len(str)):
    if i % 2 == 0:
        res = res + str[i]
print("Remove Odd Index Char -",res)


# In[35]:


str = "To change the overall look your document. To change the look available in the gallery"
x = dict()
txt = str.split(" ")
for t in txt:
    if t in x:
        x[t] += 1
    else:
        x[t] = 1
print(x)


# In[38]:


str = input("Enter String :")
print("Upper Case :",str.upper())
print("Lower Case :", str.lower())


# In[41]:


str=input("Enter the String :")
if len(str) % 4 == 0:
   print(''.join(reversed(str)))
else:
    print(str)


# In[53]:


str = input("Enter String :")
txt_upper = 0
for letter in str[:4]: 
    if letter.upper() == letter:
        txt_upper += 1
if txt_upper >= 2:
    print(str.upper())
else:
    print(str.title())


# In[ ]:


str=input("Enter String :")
print(sorted(sorted(s), key=str.upper()))


# In[2]:


str = "\nTutor \nJoes \nComputer \nEducation\n"
print(str)
print(''.join(str.splitlines())) # after removal of \n


# In[3]:


str = "Tutor Joes Computer Education"
print(str.startswith("Tu"))


# In[10]:


import textwrap
txt = "Python is an interpreted, object-oriented, high-level programming language that can be used for a wide variety of applications. Python is a powerful general-purpose programming language."
print(textwrap.fill(txt, width=35))
print("\n",textwrap.fill(txt, width=100))


# In[18]:


import textwrap
txt = """
    Python is an interpreted, object-oriented, high-level programming language
    that can be used for a wide variety of applications. Python is a powerful
    general-purpose programming language
"""
print(txt)
ded = textwrap.dedent(txt)
print(ded)


# In[20]:


import textwrap
para = """
        Python is an interpreted, object-oriented, high-level programming language
        that can be used for a wide variety of applications. Python is a powerful
        general-purpose programming language
"""
without_Indent = textwrap.dedent(para)
txt = textwrap.fill(without_Indent, width=70)
res = textwrap.indent(txt, '* ')
print(res)


# In[ ]:




