#!/usr/bin/env python
# coding: utf-8

# In[2]:


# PSET4 - Kimberly Bennett
# This code generates a PRELIMINARY rendition of a figure related to our
# project. A heatmap of 500 genes' expression counts over several cell
# samples will be created. The top 500 genes out of 28336 genes are displayed
# from 3186 different cell samples. Future work will include a breakdown
# of the types of cells samples in order to distinguish significance.

# Import necessary toolboxes:
import pandas as pd
import seaborn
import matplotlib.pyplot as plt


# In[4]:


# Add a tool to read the given MTX Matrix Market file:
from scipy.io import mmread

# Import a file with Normalized Counts of gene expression (unit = cpm)
Normalized_Counts = (mmread
                     ('E-GEOD-98816.aggregated_filtered_normalised_counts.mtx'))
#file taken from the NCBI database and upload to the project github

NC = Normalized_Counts.todense() #process the MTX file

df = pd.DataFrame(NC, range(1, NC.shape[0] + 1), range(1, NC.shape[1] + 1))
# convert the MTX file into a pandas df

new_df = df.iloc[:500,:3186] #take the first 500 genes of the df
print(new_df) #print the df to view values


# In[5]:


# Generate the Heatmap:

plt.figure(figsize=(18,12)) #changes figsize in inches

#use seaborn to create a heatmap (input the modified df, set color bar min/max,
#change color of cmap if needed, and create cbar) 
heatMap = seaborn.heatmap(new_df, vmin=0, vmax=2000, cmap=None, cbar=True)

#add plot labels:
plt.title('Heatmap of Gene Expression within each cell sample')
plt.xlabel('Cell Sample')
plt.ylabel('Gene')

print(heatMap) #visualize heatmap
fig = heatMap.get_figure()
fig.savefig('./Heatmap.png', bbox='tight') #save heatmap to file


# In[ ]:




