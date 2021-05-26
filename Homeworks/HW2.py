"""
AI730 - Ödev 2
Çağdaş Yalman

"""

""" 1 - Create 5 dictionaries. Each dictionary should represent a CV. """

cv_1 = {'name': 'Ahmet', 'surname': 'Yılmaz', 'age': 26, 'job': 'Data Analyst', 'Experience Year': 4 }
cv_2 = {'name': 'Hakan', 'surname': 'Güner', 'age': 28, 'job': 'Data Analyst', 'Experience Year': 6 }
cv_3 = {'name': 'Melis', 'surname': 'Gümüş', 'age': 23, 'job': 'Data Analyst', 'Experience Year': 1 }
cv_4 = {'name': 'Ayşe', 'surname': 'Meriç', 'age': 40, 'job': 'Data Analyst', 'Experience Year': 18 }
cv_5 = {'name': 'Serdar', 'surname': 'Çelik', 'age': 36, 'job': 'Data Analyst', 'Experience Year': 14 }



""" 2 - Create a CV containing the information of the 5 created people, """

cv_all = []
cv_all.append(cv_1)
cv_all.append(cv_2)
cv_all.append(cv_3)
cv_all.append(cv_4)
cv_all.append(cv_5)



""" 3 - Print the information on CV’s created on the screen. """

for v in cv_all:
  print(v)

