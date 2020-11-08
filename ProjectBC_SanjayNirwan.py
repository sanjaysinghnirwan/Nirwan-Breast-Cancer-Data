#!/usr/bin/env python
# coding: utf-8

# 
# 
# # EDA on Breast Cancer Survival Data
# 
# Project for Feb 08 2020 INSAID <br>
# Submitted By: Mr Sanjay Singh Nirwan

# # Table of Content 
# 1. Problem Statement <br>
# <br>
# 
# 2. Importing Packages <br>
# <br>
# 
# 3. Loading data <br>
#     a. Description of the Datasets <br>
#     b. Pandas Profiling before Data Preprocessing <br>
# <br>
# 4. Data Preprocessing <br>
#     1 Data Preprocessing <br>
#     2.Pandas Profiling after Data Preprocessing<br><br>
# <br>
# 
# 5. Data Visual Analysis <br><br>
#     a. Univariate Analysis <br>
#     b. Bivariate Analysis <br>
#     c. Multivariate Analysis <br>
# <br>
# 6. Conclusion<br><br>
# <br>
# 7. Insights<br>

# # 1. Problem Statement <Br>
#     
# #### The problem statemnet is that with the age, Pos Axillary Nodes are we able to predict the survival status of the patinet after 5 years of operation.<Br>
#     

# # 2. Importing packages

# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings


# # 3. Importing dataset
# 
# **Breast Cancer Survival** dataset has been downloaded from GitHUB using the Code below.
# 

# In[10]:


bc_df = pd.read_csv('https://raw.githubusercontent.com/insaid2018/Term-1/master/Data/Projects/Breast_cancer_survival.csv')            # write the url of the csv file within ''.
bc_df


# ### Description of Breat Cancer Survival DataSet
# The Breast Cancer survival data set provides <br>
#     1. Age of the patient
#     2. Years of Operation: The year in 1900 when the operation was done 
#     3. Pos_Axillary_Nodes: The count of Post Axillary Nodes that the Patinet had
#     4. Status wherein 
#         1= The patient survivded for More than 5 Years after the Operation
#         2= The Patinet did not survive after 5 years of the operation 

# In[11]:


bc_df.info()


# #### **Info** Gives the the following Information  <br> 
#     1. There are 306 samples(rows) and 4 Columns in the daatframe
#     2. There are 0 Missing Data in the dataset 
# 

# In[12]:


print(bc_df.shape)


# In[13]:


print(bc_df.columns)


# In[14]:


bc_df['Status'].value_counts()


# In[15]:


81/306 *100


# #### 26 % of the Patients did not survive after 5 Years of the Operation

# In[16]:


bc_df.describe()


# #### Describe gives the following Information:<br>
# 1. The mean age of the Patients who underwent operation is 52 
# 2. Pos Axillarry node has mean of 4 and 25% quartile data has 0 mean and in the last Quartile there are more than 4 Pos Axillary nodes observed ...Max being 52
# 3. In terms of Status two are observed 1. survived more than 5 Years, and 2 Did Not survive more than 5 Years.
# 4. Years of Operation Gives infromation in which the Operation was done in 1900. The Data rnage is from 1958 to 1969.
# 

# # 4. Visualising the data
# 

# ### Observations from Pandas Profiling before Data Processing
# 
# Dataset info:
# 
# Number of variables: 4 <br>
# Number of observations: 306 <br>
# Missing cells: 0 (0.%) <br>
# Duplicate Rows: 17 (5.6%) <br>
# 
# Variables types: <br>
# Numerical Type :3  <br>
# Categorical Type: 1 <br>
# 
# #### Other Important observations
# 1. Pos Axillary Nodes has 136 Zeros (44%), but this is Normal as in breast cancer The patient may have Pos Axillay Nodes. 
# Pos Nodes count and status as N Meaning as below from https://ww5.komen.org/BreastCancer/LymphNodeStatusandStaging.html <br>
# 
# N = 0 Means Axillary and other nearby lymph nodes do not have cancer or only have isolated tumor cells (individual cancer cells), when looked at under a microscope <br>
# 
# N= 1 Means icrometastases (very small clusters of cancer) OR 1–3 axillary lymph nodes have cancer AND/OR Internal mammary nodes have cancer or micrometastases (very small clusters of cancer cells) found on sentinel node biopsy <br>
# 
# N= 2 Means 4–9 axillary lymph nodes have cancer OR Internal mammary nodes have cancer, but axillary lymph nodes do not have cancer <br>
# 
# N = 3 Means 10 or more axillary lymph nodes have cancer OR Infraclavicular (under the clavicle) nodes have cancer OR Internal mammary nodes have cancer plus 1 or more axillary lymph nodes have cancer OR 4 or more axillary lymph nodes have cancer plus internal mammary nodes have cancer or micrometastases found on sentinel node biopsy OR Supraclavicular (above the clavicle) nodes have cancer <br>
# 
# 
# 1. Status . 81 of the Patients (26%) did not survive more than 5 Years post the operation. <br>
# 
# 2. Age has Minimum 30 and max 83 and the Mean is 52.   <br>
# 
# 3. Pos axillary Nodes and Age has a High Positive Correlation Higher the Pos Axillary Nodes, higher the stuatus changes from 1 to 2, meaning that more no of axillary Nodes leads to Patinet not surbviving more than 5 years post operation.  <br>
# 
# 4. Years of Operation shows that maximum ferquency of Operation 60 (19.6%) were done in the year 1958. <br>

# #  Data Processing <br>
# 
# #### Please Note that since the data does not have any missing value and any Data that needs to be changed we are not doing any processing of the Data and the data will be used as it is for further Anaylsis 
# 
# 

# ### Profiling Data Post Processing
# ### Since we have not done data Processing to change anything in the data the same data is maintained 

# # 5. Exploratory Data Analysis
# 
# Now we proceed towards the exploratory data analysis of the the data
# 

# ## 5. 1 Univariate Analysis
# Kindy Note Univariate Analysis was done using the Profiling data and is presented in the presentation.

# # # 5.2 Bivariate Analysis

# # Analysis of Correlation Between Pos Axillary Nodes and Age in Breast Cancer
# 

# In[20]:


bc_df.plot(kind='scatter', x='Pos_axillary_nodes', y='Age')
plt.grid()
plt.title('Scatter Plot of Age and Axillary Nodes')
plt.show()


# The Above Scatter Plot between Age and Pos Axillary Node show the  data as overlapped hence we will use sns to plot with colour difference below

# In[21]:


sns.set_style('whitegrid')
sns.FacetGrid(bc_df, hue= 'Status', height=7)  .map(plt.scatter,'Pos_axillary_nodes', 'Age')  .add_legend();
plt.title('Facetgrid of Age and Axillary Nodes')
plt.show();


# In the above Scatter Plot we are able to see in blue dots that represent survival more than 5 years and orange dots represent survival less than 5 years. <br>
# 
# The above plot shows that though at Pos Axillay nodes 0 to 5 there is a mix of survival and non survival status but on the righter side of the graph we can see that the Survival chances are less as the Pos Axillaty  nodes incraeses and also as the age and Pos Axillay nodes increases. <br>

# To do further analysis on the three paratemeters we have for classification , we are using pairplots from seaborn to plot of various combination from which we can select best pair for our further operation and final conclusion. 

# In[22]:


plt.close();
sns.set_style('whitegrid');
sns.pairplot(bc_df, hue='Status', height=5, vars=['Age','Years_of_operation', 'Pos_axillary_nodes'])
plt.show()


# Above image is the combinations plot of all features in data. 
# Plot 1,Plot 5 and Plot 9 are the histograms of all combinations of features which explain the density of data by considering different features of data.
# 
# ***Plot 2:-*** In this plot we see that there is Operation Age on X-axis and Age on Y-axis and the plot of there data is mostly overlapping on each other data so we cannot distinguish if there is any orange point present below blue point or vice versa.So I am rejecting these 2 data feature combination for further analysis.
# 
# ***Plot 3:-*** In this plot there are some points which is distinguishable but still it is better from other plot as we can provide conclusion more precisely by histogram and CDF which iwill learn ahead. In this plot the overlap of points are there but still it is better than all other plots comparatively. So I will select the data feature of this plot ie. Age and Axillary nodes.
# 
# ***Plot 4:-*** It is plotted using the data feature Operation Age and Age which shows similar type of plot like Plot 2 but it just rotated by 90 degree. So I also reject this feature
# 
# ***Plot 6:-*** It is a plot on the feature Operation Age and Axillary nodes which is somewhat similar to the Plot 2 but overlapping of points seems to be more in this plot comparative to other. So, I will also reject this combination
# 
# ***Plot 7:-*** This plot is similar as Plot 3 only feature interchange its axis so the plot will rotate by 90 degree. Also, I will accept this combination for further operations
# 
# ***Plot 8:-*** It is same as Plot 6 only feature on axis interchange.
# So, I consider the feature Age and Axillary nodes plotting in the Plot 3 and 7 for my all further data operations

# In[23]:


sns.FacetGrid(bc_df,hue='Status', height=6).map(sns.distplot,'Pos_axillary_nodes').add_legend()
plt.title('PDF Axillary Nodes')


# It has been observed that people survive long if they have less axillary nodes detected and vice versa but still it is hard to classify but this is the best data you can choose among all. So, we can conclude below result <br>
# 
# If ***(AxillaryNodes≤0)*** <br>
#     Patient= Long survival <br>
# 
# else if ***(AxillaryNodes≥0 & Axillary nodes≤3.5(approx))*** <br>
#     Patient= Long survival chances are high <br>
# 
# else if ***(Axillary nodes ≥3.5)*** <br>
#     Patient = Short survival <br>

# In[24]:


sns.FacetGrid(bc_df,hue='Status', height=5).map(sns.distplot,'Years_of_operation').add_legend()
plt.title('PDF Years of Operation')


# The above shows that there is equal number of density in each data point. The PDF of both classification overlap on each other.
# some observations as below 
# 1. Status 2 dominates over status 1 till 1958, hence patients had less srvival chance before 1958
# 2. from 1958 to 1962 the status 1 dominates showing that the patients had more suruval chances
# 3. However in 1965 the survival chances were less as shows a peak.

# In[25]:


sns.FacetGrid(bc_df,hue='Status', height=5).map(sns.distplot,'Age').add_legend()
plt.title('PDF Age')


# In above plot it is observed that at the age range from 30–75 the status of survival and death is same. So, using this datapoint we can see the below observations
# 1. Survival chances are high between age 30-40
# 2. survival chances are less between 40-50 <br>
# however later after 50 years the graphs overlap.

# # 1 D Scatter Plot fo Data

# In[26]:


import numpy as np

bc_df_Long_Survive = bc_df.loc[bc_df['Status'] == 1];
bc_df_Short_Survive = bc_df.loc[bc_df['Status'] == 2];
plt.plot(bc_df_Long_Survive['Pos_axillary_nodes'], np.zeros_like(bc_df_Long_Survive['Pos_axillary_nodes']),'o')
plt.plot(bc_df_Short_Survive['Pos_axillary_nodes'], np.zeros_like(bc_df_Short_Survive['Pos_axillary_nodes']),'o')


# Here in the  1 D scatter plot we observe the data of short survival status are mostly overlap on long survival status due to which we  will not able to conclude on this data.

# # CDF of Long Survive Data

# In[27]:


counts, bin_edges = np.histogram(bc_df_Long_Survive['Pos_axillary_nodes'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf);
print(bin_edges);
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf);
plt.plot(bin_edges[1:],cdf)


# 1. From above CDF we can observe that orange line shows there is a 85% chance of long survival if number of axillary nodes detected are < 5. 
# 2. Also you we can see as number of axillary nodes increases survival chances also reduces means it is clearly observed that 80% — 85% of people have good chances of survival if they have less no of auxillary nodes detected and as nodes increases the survival status also decreases as a result 100% of people have less chances of survival if nodes increases >40
# 
# ***Thus this imphasis the need to check before tha axillary  odes get out of proportion and the survival chances become less***
# 

# # CDF of Short Survive Data

# In[28]:


counts, bin_edges = np.histogram(bc_df_Short_Survive['Pos_axillary_nodes'], bins=10, 
                                 density = True)
pdf = counts/(sum(counts))
print(pdf);
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:], cdf)
plt.show();


# From the above it is seen thatin Short survival nearly 55% of people who have nodes less than 5 and there are nearly 100% of people in short survival if nodes are > 40

# ### Predicting patients status by applying mathematical formulae like Standard Deviation and Mean

# In[29]:


print('Means:')
print (np.mean(bc_df_Long_Survive['Pos_axillary_nodes']))
print (np.mean(np.append(bc_df_Long_Survive['Pos_axillary_nodes'],50)))
print (np.mean(bc_df_Short_Survive['Pos_axillary_nodes']))
print('\nStandard Deviation:')
print(np.mean(bc_df_Long_Survive['Pos_axillary_nodes']))
print(np.mean(bc_df_Short_Survive['Pos_axillary_nodes']))


# 1. We observe that for Long survive the Pos axillary Nodes mean is 2.79 and including outlier it is 3 that is almost same, but the mean of Short survive is 7.4 which is comparatively much higher than Long survive. 
# 2. So the probability for short survive is more in data set.
# 3. We also observe that the standard deviation Long survive has standard deviation of only 2.79 and Short survive has 7.45, means the spread of data for short survive is more.

# ### Using Median, Quantiles, Percentile  of the Data for Analysis

# In[30]:


print('Medians:')
print(np.median(bc_df_Long_Survive['Pos_axillary_nodes']))
print(np.median(np.append(bc_df_Long_Survive['Pos_axillary_nodes'],50)))
print(np.median(bc_df_Short_Survive['Pos_axillary_nodes']))
print('\nQuantiles:')
print(np.percentile(bc_df_Long_Survive['Pos_axillary_nodes'],np.arange(0,100,25)))
print(np.percentile(bc_df_Short_Survive['Pos_axillary_nodes'],np.arange(0,100,25)))
print('\n90th percentile:')
print(np.percentile(bc_df_Long_Survive['Pos_axillary_nodes'],90))
print(np.percentile(bc_df_Short_Survive['Pos_axillary_nodes'],90))
from statsmodels import robust
print ('\nMedian Absolute Deviation')
print(robust.mad(bc_df_Long_Survive['Pos_axillary_nodes']))
print(robust.mad(bc_df_Short_Survive['Pos_axillary_nodes']))


# From above observation it is clear that 
# 1. Average axillary nodes in long survival is 0 and for short survival it is 4. ie, Patients who have average 4 auxillary nodes have short survival status.
# 2. Quantiles shows that nearly 50th% of axillary nodes are 0 in long survival and 75th% of patients have nodes less than 3 that is 25% patients are having nodes more than 3.
# 3. In short survival 75th% of patients have minimum 11 nodes detected.
# 4. At 90th% there if nodes detected is >8 then it has long survival status and if nodes are >20 then patients will have short survival status

# ### Using a Box Plot to analyse Status and Pos Axillary Nodes 

# In[37]:


sns.boxplot(x='Status',y= 'Pos_axillary_nodes',data=bc_df) 
plt.show()


# In above box whiskers 25th percentile and 50th percentile are nearly same for Long survive and threshold for it is 0 to 7. Also, for short survival there are 50th percentile of nodes are nearly same as long survive 75th percentile. Threshold for the Short survival is 0 to 25 nodes and 75th% is 12 and 25th% is 1 or 2.
# 

# ### Using a Box Plot to analyse Status and Age

# In[32]:


sns.boxplot(x='Status',y= 'Age',data=bc_df) 
plt.show()


# ### Using a Violin  Plot to analyse Status and Pos Axillary Nodes 

# In[33]:


sns.violinplot(x= 'Status', y='Pos_axillary_nodes',data=bc_df)
plt.legend
plt.show()


# #### In above violin plot we observe that For long survive density for it is more near the 0 nodes and also it has whiskers in range 0-7 and in violin 2 it shows the short survival density more from 0–20 and threshold from 0–12
# Thus more the Pos Axillary node , less the survival chances of the Patient afetr 5 years of operation

# # Contour Plot 
# we will not draw a contour plot of the data between axillay nodes and age to see the max density for Long survival 

# In[34]:


sns.jointplot(x='Age',y='Pos_axillary_nodes', data=bc_df_Long_Survive,kind= 'kde')
plt.grid()
plt.show()


# ### In the 2D density plot for long survival using feature age and axillary nodes The density of point for long survival is more from age range 47–60 and axillary nodes from 0–3.
# Also the above data in graph form gives a clear cut indication that if breast cancer is detected by early screening when the Pos Axillary Nodes are less and operation is done, the survival chances increases of the Patients.

# ### Joint Plot to analyse Age  and Pos Axillary Nodes for Short Survival Data 

# In[35]:


sns.jointplot(x='Age',y='Pos_axillary_nodes', data=bc_df_Short_Survive,kind= 'kde')
plt.grid()
plt.show()


# #### In the 2D density plot for short survival using feature age and axillary nodes The density of point for long survival is more from age range 40-50 and axillary nodes from 0–10.
# Also the above data in graph form gives a clear cut indication that if breast cancer is detected by early screening when the Pos Axillary Nodes are less and operation is done, the survival chances increases of the Patients.

# # Conclusions 
# 
# The Breast Cancer survival data was analysed and the following conlcusions are drawn from the data <br>
# 
# It was observed that 26% of the Patients in the data set did not survive after 5 years of operation<br>
# 
# Patients with Pos Axillary Nodes 0-7 have long survival chances, but Patients who have average 4 axillary nodes have short survival status.<br>
# 
# Patients between age 40-60 with Pos axillary node 0-10 have short survival chances.<br>
# 
# Patients between age 47-60 with Pos axillary node 0-3 have longer survival chances. <br>
# 
# As the age and Pos Axillary Nodes Increase the chances of survival  beyond 5 Years reduce for the patients<br>
# 

# # Insights
# 
# Pos Axillary Nodes provide an insight into the survival status of the Patients <br>
# 
# Early age detection can help catch the disease at early stage <br>
# 
# Mass Screenings should be done at age >30 for Women to detect the count of Pos Axillary Nodes <br>
# 
# Early Detection of Breast Cancer is the best way to fight against the disease <br>
# 
# More studies with parameters like Vegan/Non Veg ,History, smoking, alcohol consumption, genetic structure needs to be empanelled to understand the disease better and prevent prognosis <br>
# 
