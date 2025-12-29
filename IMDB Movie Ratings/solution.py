import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv('IMDB-Movie-Data.csv')
data

**1. Display Top 10 Rows of The Dataset**
data.head(10)
  
**2. Check Last 10 Rows of The Dataset**
data.tail(10)
  
**3. Find Shape of Our Dataset (Number of Rows And Number of Columns)**
data.shape
  
**4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement**
data.info()
  
**5. Check Missing Values In The Dataset**
data.isnull().sum()
  
**6. Drop All The  Missing Values**
data.dropna(axis=0,inplace=True)
data.isnull().sum()
  
**7. Check For Duplicate Data**
dup=data.duplicated().any()
dup

**8. Get Overall Statistics About The DataFrame**
data.describe()

**9. Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes**
data.columns
data[data['Runtime (Minutes)']>=180]['Title']

**10. In Which Year There Was The Highest Average Voting?**
data.groupby('Year')['Votes'].mean().sort_values(ascending=False)
  
**11. In Which Year There Was The Highest Average Revenue?**
data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
sns.barplot(x='Year',y='Revenue (Millions)',data=data)
  
**12. Find The Average Rating For Each Director**
data.groupby('Director')['Rating'].mean()
  
**13. Display Top 10 Lengthy Movies Title and Runtime**
data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]
  
**14. Display Number of Movies Per Year**
data['Year'].value_counts()
  
**15. Find Most Popular Movie Title (Highest Revenue)**
data.columns
data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]

**16. Display Top 10 Highest Rated Movie Titles And its Directors**
data.nlargest(10,'Rating')[['Title','Rating']]
  
**17. Display Top 10 Highest Revenue Movie Titles**
data.nlargest(10,'Revenue (Millions)')['Title']
  
**18.  Find Average Rating of Movies Year Wise**
data.columns
data.groupby('Year')['Rating'].mean()
  
**19. Does Rating Affect The Revenue?**
sns.scatterplot(data=data,x='Rating',y='Revenue (Millions)')
plt.show()
  
**20. Classify Movies Based on Ratings [Excellent, Good, and Average]**
def rating(rating):
    if rating >= 7.0:
        return "Excellent"
    elif rating >=6.0:
        return "Good"
    else:
        return "Average"
data['Rating_Category']= data['Rating'].apply(rating)
data.head(3)

**21. Count Number of Action Movies**
len(data[data['Genre'].str.contains("Action")])
