# -*- coding: utf-8 -*-
"""klawye.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sCuRttGrF2qExKXyY7wGqtpEhqLaXS6f
"""

left_letters =list("qwertasdfgzxcvb")
right_letters =list("yuiophjklnmşğç")
right_left=set(left_letters+right_letters)

while True: 
    word=set(input("please enter a word : "))
    for i in word:
        test=i in right_left
        if test==False:
          print("This word contains letters out of (a-z)")
          break
    if test==True:
      break

for i in word:
     left= i in left_letters
     if left==True:
        break 
        
for i in word:
     right= i in right_letters
     if right==True:
        break

if  (left and right)==True:
       print("True","(uses both hand fingers)")
elif left==False:
        print(left,"(uses only left-hand fingers)")    
else:
        print(right,"(uses only right-hand fingers)")

from typing import Set
left_letters =set("qwertasdfgzxcvb")
right_letters =set("yuiophjklnmşğç")
right_left=set(list(left_letters)+list(right_letters))

while True:
  word=set(input("please enter a word : "))
  if word - right_left != set():
    print("This word contains letters out of (a-z)")
  else:
    break
if word - left_letters == set():
  print(word - left_letters != set(),"(uses only left-hand fingers)")
elif word - right_letters == set():
  print(word - right_letters != set(),"(uses only right-hand fingers)")
else:
  print(True,"(uses only both-hand fingers)")