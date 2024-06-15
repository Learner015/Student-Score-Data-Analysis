import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Expanded_data_with_more_features.csv')
print(df.head())
describe = df.describe()
print(describe)
info = df.info()
print(info)

null = df.isnull().sum()
print(null)

#drop unnamed column
df = df.drop("Unnamed: 0", axis=1)
print(df.head()) 

# Change the weekly study hours column
df["WklyStudyHours"] =df["WklyStudyHours"].str.replace("05-Oct","5-10")
print(df["WklyStudyHours"])

# Gender Distribution
plt.figure(figsize=(5,5))
distribution =sns.countplot(data= df, x ='Gender')
distribution.bar_label(distribution.containers[0])
plt.show()

# from the above chart we have analyze the number of females are more than number of males

# now analyze the parents's education on scores

gp = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore" :'mean',"WritingScore":"mean"})
print(gp)
heat_map = sns.heatmap(gp, annot= True)
plt.show()

# CONCLUSION :
# A parents group having a master degree :  Has highest avg marks show in lighter shade
# whereas high school completed parents : Has difference ot 11 marks which shows the impact of parent's education

# Analyses according to the Parent Marital status
gb = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore" :'mean',"WritingScore":"mean"})
print(gb)

plt.figure(figsize=(8,8))
plt.title(" Relationship between Parent Marital Status and Student Avg Scores")
heat_map = sns.heatmap(gb, annot= True)
plt.show()
# CONCLUSION :
# # Reading Score in not much affected but a small impact can seen in maths score 
# # Hence there is a small/negligible/no impact on status of marriage of parents on a child

# # TO DETECT EXTREME VALUES
val = sns.boxplot(data= df, x= 'MathScore')
plt.show()

val = sns.boxplot(data= df, x= 'ReadingScore')
plt.show()

val = sns.boxplot(data= df, x= 'WritingScore')
plt.show()
# CONCLUSION :
# Maths is difficult subject than reading and writing


# PIE CHART

grpA = df.loc[(df['EthnicGroup'] == 'group A' )].count()
print(grpA)
grpB = df.loc[(df['EthnicGroup'] == 'group B' )].count()
grpC = df.loc[(df['EthnicGroup'] == 'group C' )].count()
grpD = df.loc[(df['EthnicGroup'] == 'group D' )].count()
grpE = df.loc[(df['EthnicGroup'] == 'group E' )].count()

csfont = {'fontname': 'Comic Sans MS'}
hfont = {'fontname': 'Helvetica'}
plt.title("Pie Chart Of different ethnic groups", **csfont)
lbel = ['group A','group B','group C','group D','group E']
plt.xlabel(lbel, **hfont)
mlist = [grpA['EthnicGroup'],grpB['EthnicGroup'],grpC['EthnicGroup'],grpD['EthnicGroup'],grpE['EthnicGroup']]
plt.pie(mlist, labels= lbel, textprops=({'fontname' : 'Comic Sans MS'}))
plt.show()

