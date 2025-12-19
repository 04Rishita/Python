import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data=pd.read_csv('adult.csv')
data

**1.Display Top 10 Rows of The Dataset**
data.head(10)

**2.Display Last 10 Rows of The Dataset**
data.tail(10)

**3. Find Shape of Our Dataset (Number of Rows And Number of Columns)**
data.shape

**4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement**
data.info()

**5. Fetch Random Sample From the Dataset (50%)**
data.sample(frac=0.50)

**6.Check Null Values In The Dataset**
data.isnull().sum()

**7.Perform Data Cleaning [ Replace '?' with NaN ]**
data.isin(['?']).sum()
data['workclass']=data['workclass'].replace('?',np.nan)
data['occupation']=data['occupation'].replace('?',np.nan)
data['native-country']=data['native-country'].replace('?',np.nan)
data.isin(['?']).sum()

**8. Drop all The Missing Values**
missing=data.isnull().sum()*100/len(data)
missing
data.dropna(how='any',inplace=True)
data.isnull().sum()

**9. Check For Duplicate Data and Drop Them**
dup=data.duplicated().any()
print(dup)
data=data.drop_duplicates()
data.shape

**10. Get Overall Statistics About Our Dataframe**
data.describe()

**11. Drop The Columns education-num,capita-gain and capital-loss**
data=data.drop({'educational-num','capital-gain','capital-loss'},axis=1)

**Univariate Analysis**
**12. What Is The Distribution of Age Column?**
data.describe()
data['age'].hist()

**13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method**
sum(data['age'].between(17,48))

**14. What is The Distribution of Workclass Column?**
data['workclass'].describe()
plt.figure(figsize=(10,10))
data['workclass'].hist()

**15. How Many Persons Having Bachelors or Masters Degree?**
len(data[(data['education']=='Master') | (data['education']=='Bachelors')])
data.columns

**16. Bivariate Analsis**
import matplotlib.pyplot as plt
sns.boxplot(x='income',y='age',data=data)

**17. Replace Salary Values With 0 and 1**
data['income'].unique()
data['income'].value_counts()
sns.countplot(x='income',data=data)
def salary(sal):
    if sal=='<=50K':
        return 0
    else:
        return 1
data['encoded_salary']=data['income'].apply(salary)
data.head(2)
data.replace(to_replace=['<=50K','>50K'],value=[0,1],inplace=True)
data.head(1)

**18. Which Workclass Getting The Highest Salary?**
data.groupby('workclass')['income'].mean().sort_values(ascending=False)

**19.How Has Better Chance To Get Salary greater than 50K Male or Female?**
data.groupby('gender')['income'].mean().sort_values(ascending=False)

**20. Covert workclass Columns Datatype To Category Datatype**
data.info()
data['workclass']=data['workclass'].astype('category')
data.info()
    
