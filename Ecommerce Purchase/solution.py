import pandas as pd
data=pd.read_csv('Ecommerce Purchases')
data
**1. Display Top 10 Rows of The Dataset**
data.head(10)

**2. Check Last 10 Rows of The Dataset**
data.tail(10)

**3.Check Datatype of Each Column**
data.dtypes

**4. Check null values in the dataset**
data.isnull()

**5. How many rows and columns are there in our Dataset?**
data.shape

**6. Highest and Lowest Purchase Prices.**
data['Purchase Price'].min()
data['Purchase Price'].max()

**7. Average Purchase Price**
data['Purchase Price'].mean()

**8. How many people have French 'fr' as their Language?**
data[data['Language']=='fr'].count()
len(data[data['Language']=='fr'])

**9. Job Title Contains Engineer**
len(data[data['Job'].str.contains('engineer',case=False)])

**10. Find The Email of the person with the following IP Address: 132.207.160.22**
data[data['IP Address']=='132.207.160.22']['Email']

**11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?**
data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]

**12. Find the email of the person with the following Credit Card Number: 4664825258997302**
data[data['Credit Card']=='4664825258997302']['Email']

**13. How many people purchase during the AM and how many people purchase during PM?**
data.columns
data['AM or PM'].value_counts()

**14. How many people have a credit card that expires in 2020?**
len(data[data['CC Exp Date']=='2020'])

**15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)**
data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()
