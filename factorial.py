# -*- coding: utf-8 -*-
"""factorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bijt055ANwLt94pF2QnmWKdSuVulyO7K
"""

def factor(num):
  sonuc=1
  for i in range(1,num+1):
    sonuc *= i
  return sonuc
factor(5)