#!/usr/bin/env python
# coding: utf-8

# # Assignment 4

# Q1. Write a Python Program (with class concepts) to find the area of the triangle use the below formula.
# area = s*(s-a)*(s-b)*(s-c)
# Function to take the length of the sides of triangle from user should be defined in the parent and class function to calculate the area should be defined in sub class.

# In[1]:


class Triangle:
    def __init__(self):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __getattr__(self, area):
        for i in item:
            item = a + b + c / 2
            print("i")

a = int(input("Enter a number: "))
b = int(input("Enter a nummber: "))
c = int(input("Enter a number: "))
s = a + b + c / 2
area = s * (s - a) * (s - b) * (s - c) ** 0.5
print("the area of triangle is ", area)


# Q2. Write a function filter_long_words() that takes a list of words and an integer n and returns list of words that are longer than n.

# In[2]:


class my_list:
 def __init__(self,word):
  self.word = word
  print("Initialised my_list object")

 def filter_long_words(self,a):
  return list(filter(lambda y: len(y) > a, self.word))

instance = my_list(["Today","is","an","important","day"])
print("new list of words =>" + str(instance.filter_long_words(4)))


# Q3. Write a python program using the function that maps list of words into list of integers representing the lenghts of corresponding words.
# Hint : If a list [ab,cde,erty] is passed onto the python function output should come as [2,3,4].
# Here 2,3 and 4 are the length of the words in the list.

# In[1]:


my_words = ["Today","it","is","a","good","start"]
def wordlength(my_words):
 return list(map(lambda y: len(y),my_words))

print("words lengths in array =>" + str(wordlength(my_words)))


# Q4. Write a python function which takes character(i.e. string of a length 1) and returns True if it is a vowel, False otherwise.

# In[18]:


# Function to check whether the word is a vowel  and return  True or False

def check_vowel(word):
    if (word == 'v' or word == 'a' or word == 's' or word == 'u' or word == 'd' or word == 'h' or word == 'a'):
        return True
    else:
        return False

# Take user input
word = input("Enter a character : ")

# If Invalid input, exit
if(word.isalpha() == False):
    exit()
     

#Invoke Function
if(check_vowel(word)):
    print(word, "is a vowel.")

else:
    print(word, "is not a vowel.")


# In[19]:


# Function to check whether the word is a vowel  and return  True or False

def check_vowel(word):
    if (word == 'v' or word == 'a' or word == 's' or word == 'u' or word == 'd' or word == 'h' or word == 'a'):
        return True
    else:
        return False

# Take user input
word = input("Enter a character : ")

# If Invalid input, exit
if(word.isalpha() == False):
    exit()
     

#Invoke Function
if(check_vowel(word)):
    print(word, "is a vowel.")

else:
    print(word, "is not a vowel.")


# In[ ]:




