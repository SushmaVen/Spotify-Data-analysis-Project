#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df_tracks = pd.read_csv('C:/Users/sushm/OneDrive/Documents/tracks.csv')
df_tracks.head()


# In[6]:


#null values

pd.isnull(df_tracks).sum()


# In[4]:


df_tracks.info()


# In[7]:


#10 list popular songs in spotify 

sorted_df = df_tracks.sort_values('popularity',ascending= True).head(10)
sorted_df


# In[8]:


#descriptive statistic for numerical values
df_tracks.describe().transpose()


# In[9]:


#top 10 most popular songs in spotofy

most_popular =df_tracks.query('popularity>90',inplace= False).sort_values('popularity',ascending = False)
most_popular[:10]


# In[10]:


df_tracks.set_index("release_date",inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[11]:


#finding artist present in 18th location 
df_tracks[["artists"]].iloc[18]


# In[12]:


#converting songs from milisec to secs

df_tracks["duration"]=df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms",inplace= True, axis =1)


# In[13]:


df_tracks.duration.head()


# In[14]:


#creating visualiztion , droping 3 unwanted columns key , mode and explicit and apply pearson corr 
# and using season using heatmap to craete corr fucntion
corr_df= df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True, fmt=".1g", vmin=-1, vmax=1, center=0, cmap="inferno", linewidths=1, linecolor="Black")
heatmap.set_title("Correlation heatmap between variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# In[15]:


#regression plot for smple data filed

sample_df = df_tracks.sample(int(0.004*len(df_tracks)))


# In[16]:


print(len(sample_df))


# In[17]:


#plotting energy vs Loudness in regression plot
plt.figure(figsize=(10,6))
sns.regplot(data = sample_df , y= "loudness", x = "energy" , color = "c").set(title ="Loudness vs Energy Correlation")


# In[18]:


#plotting popularity  vs acousticness in regression plot
plt.figure(figsize=(10,6))
sns.regplot(data = sample_df , y= "popularity", x = "acousticness" , color = "b").set(title ="Popularity vs Acousticness Correlation")


# In[19]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[20]:


#pip install -- user seaborn== 0.11.0


# In[21]:


#plotting distplot for findging total Number of songs per year
sns.displot(years,discrete=True,aspect=2, height=5, kind="hist").set(title="Number of songs per year")


# In[22]:


total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax= ax , errwidth = False).set(title = " Year Vs Duration")
plt.xticks(rotation=90)


# In[23]:


df_genre=pd.read_csv("C:/Users/sushm/OneDrive/Documents/SpotifyFeatures.csv")


# In[24]:


df_genre.head()


# In[26]:


plt.title("Duration of songs in different genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in Millisec")
plt.ylabel("Genres")


# In[28]:


sns.set_style(style="darkgrid")
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity",ascending = False).head(10)
sns.barplot(y='genre',x='popularity',data=famous).set(title="Top 5 Genres by popularity")


# In[ ]:




