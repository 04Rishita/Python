import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('udemy_courses.csv',parse_dates=['published_timestamp'])
data

data.dtypes

**1. Display Top 10 Rows of The Dataset**
data.head(10)

**2. Check Last 5 Rows of The Dataset**
data.tail(5)

**3. Find Shape of Our Dataset (Number of Rows And Number of Columns)**
data.shape

**4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement**
data.info()

**5. Check Null Values In The Dataset**
data.isnull().sum()

**6. Check For Duplicate Data and Drop Them**
dup=data.duplicated().any()
dup
data=data.drop_duplicates()
dup=data.duplicated().any()
dup

**7. Find Out Number of Courses Per Subjects**
data['subject'].value_counts()
sns.countplot(data['subject'])

**8. For Which Levels, Udemy Courses Providing The Courses**
data['level'].value_counts()
sns.countplot(data['level'])
plt.xlabel('Counts per levels')
plt.ylabel('Levels')
plt.show()

**9. Display The Count of Paid and Free Courses**
data['is_paid'].value_counts()

**10. Which Course Has More Lectures (Free or Paid)?**
data.groupby('is_paid').mean(numeric_only=True)

**11. Which Courses Have A Higher Number of Subscribers Free or Paid?**
sns.barplot(x='is_paid',y='num_subscribers',data=data)

**12. Which Level Has The Highest Number of Subscribers?**
data.columns
sns.barplot(x='level',y='num_subscribers',data=data)

**13. Find Most Popular Course Title**
data[data['num_subscribers'].max() == data['num_subscribers']]['course_title']

**14. Display 10 Most Popular Courses As Per Number of Subscribers**
data.sort_values(by='num_subscribers',ascending=False)['course_title'].head(10)

**15. Find The Course Which Is Having The Highest Number of Reviews.**
sns.barplot(x='subject',y='num_reviews',data=data)
plt.xticks(rotation=45)
plt.show()

**16. Does Price Affect the Number of Reviews?**
plt.scatter(x=data['price'],y=data['num_reviews'])
plt.xlabel('Price')
plt.ylabel('Number of Reviews')
plt.title('Does Price Affect the Number of Reviews?')
plt.show()

**17. Find Total Number of Courses Related To Python**
len(data[data['course_title'].str.contains('Python',case=False)])

**18. Display 10 Most Popular Python Courses As Per Number of Subscribers**
python=data[data['course_title'].str.contains('Python',case=False)].sort_values(by='num_subscribers',ascending=False).head(10)
sns.barplot(x='num_subscribers',y='course_title',data=python)
plt.show()

**19. In Which Year The Highest Number of Courses Were Posted?**
data.columns
data['Year']=data['published_timestamp'].dt.year
data.head(1)
sns.countplot(x='Year', data=data)

**20. Display Category-Wise Count of Posted Subjects [Year Wise]**
data.groupby('Year')['subject'].value_counts()


