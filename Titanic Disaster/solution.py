import pandas as pd
data=pd.read_csv('train.csv')
data

**1. Display Top 5 Rows of The Dataset**
data.head(5)

**2. Check the Last 3 Rows of The Dataset**
data.tail(3)
  
**3. Find Shape of Our Dataset (Number of Rows & Number of Columns)**
data.shape
  
**4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement**
data.info()
  
**5. Get Overall Statistics About The Dataframe**
data.describe()
  
**6. Data Filtering**
data[['Name','Age']]
data[data['Sex']=='male']
sum(data['Sex']=='male')
sum(data['Survived']==1)
data[data['Survived']==1]
  
**7.Check Null Values In The Dataset**
data.isnull().sum()
# visulazing NULL values
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(data.isnull())
plt.show()
missing=data.isnull().sum() * 100/len(data)
missing

**8. Drop the Column**
data.drop('Cabin',axis=1,inplace=True)
data.isnull().sum()
  
**9. Handle Missing Values**
filling=data['Embarked'].mode()
filling
data['Embarked'].fillna('filling',inplace=True)
data.isnull().sum()
data['Age'].fillna(data['Age'].mean(),inplace=True)
data.isnull().sum()

**10. Categorical Data Encoding**
data['sex_encoded']=data['Sex'].map({'male':1,'female':0})
data.head(3)
x=data['sex_encoded']=data['Sex'].map({'male':1,'female':0})
data.insert(5,'sex_new',x)
data.head(3)
pd.get_dummies(data,columns=['Embarked'])
data1=pd.get_dummies(data,columns=['Embarked'],drop_first=True)
data1.head()

**11. What is Univariate Analysis?**
**How Many People Survived And How Many Died?**
data['Survived'].value_counts()
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Survived',data=data)

**How Many Passengers Were In First Class, Second Class, and Third Class?**
data.columns
data['Pclass'].value_counts()
sns.countplot(x='Pclass',data=data)
plt.show()

**Number of Male And Female Passengers**
data['Sex'].value_counts()
sns.countplot(x='Sex',data=data)
plt.show()
plt.hist(data['Age'])
plt.show()
sns.boxplot(data['Age'],orient='v')
plt.show()
  
**12. Bivariate Analysis**
**How Has Better Chance of Survival Male or Female?**
sns.barplot(x='Sex',y='Survived',data=data)
plt.show()
  
**Which Passenger Class Has Better Chance of Survival (First, Second, Or Third Class)?**
sns.barplot(x='Pclass',y='Survived',data=data)
plt.show()
  
**13. Feature Engineering**
data['family_size']=data['SibSp']+ data['Parch']
data.head(2)
data['fare_per_person']=data['Fare']/(data['family_size']+1)
data.head(2)
