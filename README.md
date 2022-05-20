# LinkedInNetwork

## **Understanding my LinkedIn network**
The following script allows us to access our LinkedIn first-degree common connections' network. The compiled edge list can be exported to CSV and processed in Gephi / Cytoscape / your original scripts for social network analyses.

1. [Installing LinkedIn API](#Installing-LinkedIn-API-by-tomquirk)
2. [Getting own profile](#Getting-own-profile)
3. [Creating connections dataframe](#Creating-dataframe-for-own-connections)
4. [Getting connections' common connections](#Getting-connections'-common-connections)

### **Remark**
If there is no common connection between you and your connection's connections, the results will return the same data as your own. Please carefully inspect whether these connections do share a completely same connections as you do or you have no common connections with this person.
