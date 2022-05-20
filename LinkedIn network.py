#!/usr/bin/env python
# coding: utf-8

# ## **Understanding my LinkedIn network**
# The following script allows us to access our LinkedIn first-degree common connections' network. The compiled edge list can be exported to CSV and processed in Gephi / Cytoscape / your original scripts for social network analyses.
# 
# 1. [Installing LinkedIn API](#Installing-LinkedIn-API-by-tomquirk)
# 2. [Getting own profile](#Getting-own-profile)
# 3. [Creating connections dataframe](#Creating-dataframe-for-own-connections)
# 4. [Getting connections' common connections](#Getting-connections'-common-connections)
# 
# ### **Remark**
# If there is no common connection between you and your connection's connections, the results will return the same data as your own. Please carefully inspect whether these connections do share a completely same connections as you do or you have no common connections with this person.

# ### **Installing LinkedIn API by tomquirk**
# 
# Please see [linkedin-api](https://github.com/tomquirk/linkedin-api) GitHub page for more information

# In[ ]:


#Install linkedin API 
get_ipython().system('pip3 install git+https://github.com/tomquirk/linkedin-api.git')


# ### **Getting own profile**

# In[ ]:


from linkedin_api import Linkedin

#Access LinkedIn
api = Linkedin('your_username', 'your_password')

#Get my own profile. You can check your URN id here.
profile = api.get_profile('your_public_id')
profile

#Get my own connections
connections = api.get_profile_connections('your_URN_id')
connections


# ### **Creating dataframe for own connections**

# In[ ]:


#append my own connections
import pandas as pd

my_list = pd.DataFrame(columns = ['source', 'target'])
    
for person in range(len(connections)):
    connect_name = connections[person]['public_id']
    my_list = my_list.append({'source':'your_name', 
                                     'target': connect_name}, ignore_index = True)


# ### **Getting connections' common connections**
# 
# Export with *utf-8* instead of *utf-8-sig* if you are exporting to Gephi

# In[ ]:


#Find connections' connections 
edge_list = pd.DataFrame(columns = ['source', 'target'])

for i in range(len(connections)):
    org_person = connections[i]['public_id']
    cconnect = connections[i]['urn_id']
    temp = api.get_profile_connections(cconnect)
    
    for person in range(len(temp)):
        connect_name = temp[person]['public_id']
        edge_list = edge_list.append({'source':org_person, 
                                     'target': connect_name}, ignore_index = True)

combined = my_list.append(edge_list)


# In[ ]:


#Save list
combined.to_csv('path', encoding = 'utf-8-sig')

