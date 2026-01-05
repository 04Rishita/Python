import pandas as pd

data=pd.read_csv('hotel_bookings.csv')
data
data.columns
data.rename({'adults':'num_adults','children':'num_children','babies':'num_babies'},axis=1,inplace=True)
data.columns
data.isnull().sum() *100/len(data)
data['agent'].fillna(-1,inplace=True)
data[data['num_children'].isna()]
data.dropna(subset=['num_children'],inplace=True)
data.drop(columns=['company'],inplace=True)
data.isnull().sum() *100/len(data)
data=data.astype({'is_canceled':'boolean','is_repeated_guest':'boolean','num_children':'int','agent':'int'})
data.dtypes
data['lead_time'].unique()
data['lead_time'].describe()
bins=[0,100,200,300,400,500,600,700,800]
labels=['0-100','101-200','201-300','301-400','401-500','501-600','601-700','701-800']
data['lead_time_binned']=pd.cut(data['lead_time'],bins=bins,labels=labels)
data[['lead_time','lead_time_binned']]
# Seperating columns

data['arrival_date_month']=data['arrival_date'].str.split('-',expand=True)[0]
data['arrival_date_year']=data['arrival_date'].str.split('-',expand=True)[1]
data.head()
#String Cleaning

data['hotel']=data['hotel'].replace(r"[\*\n\^]",'',regex=True)
data['hotel'].unique()
#Remove Duplicates

data.loc[data.duplicated(keep=False)]
data.drop_duplicates(keep="first",inplace=True)
data.loc[data.duplicated(keep=False)]

data.shape
