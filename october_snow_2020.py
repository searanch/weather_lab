import matplotlib.pyplot as plt
import seaborn as sns

y = [8.2,7.4,5.5,3.0,2.6]
x = ['10-31-1991','10-20-2020','10-29-1905','10-20-1916','10-27-1919']



#dates=tuple(x)
#print(dates)
#print(ax=sns.barplot(x,y))

ax = sns.barplot(x, y)
ax