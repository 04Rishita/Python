import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('datasets.csv')
data
data.head()

data.tail()

data.shape

data.info()

data.describe()

data.isnull().sum()

data.dropna(inplace=True)

data.isnull().sum()

data.duplicated().sum()

data.drop_duplicates(inplace=True)
data.duplicated().sum()

data['id']=data['id'].astype(object)
data.dtypes

#Identifying Outliers
sns.boxplot(data=data,x='price')
plt.title('Price Outliers')

df=data[data['price']<1500] 

sns.boxplot(data=df,x='price')
sns.histplot(x='price',data=df,bins=100)
plt.title('Price Distribution')
plt.ylabel('Frequency')
plt.show()

sns.histplot(x='availability_365',data=df)
plt.title('Availability_365 Distribution')
plt.ylabel('Frequency')
plt.show()

df.groupby('neighbourhood_group')['price'].mean()
df['price per bed']=df['price']/df['beds']

df['price per bed']
df.groupby('neighbourhood_group')['price per bed'].mean()

**BIVARAITE ANALYSIS**
sns.barplot(data=df,x='neighbourhood_group',y='price',hue='room_type')
plt.title('Price Dependency of Neighbourhood')
plt.show()
  
sns.scatterplot(x='number_of_reviews',y='price',data=df,hue='neighbourhood_group')
plt.title('Locality and Review Dependency')
plt.show()
  
data.columns

sns.pairplot(data=df,vars=['price','minimum_nights','number_of_reviews_ltm','availability_365'],hue='room_type')
plt.show()
plt.figure(figsize=(10,7))
sns.scatterplot(data=df,x='longitude',y='latitude',hue='room_type')
plt.title('Geographical Distribution of Airbnb Listings')
plt.show()
  
corr=df[['latitude','longitude','price','minimum_nights','number_of_reviews','reviews_per_month','availability_365','beds']].corr()
corr
sns.heatmap(data=corr,annot=True)
