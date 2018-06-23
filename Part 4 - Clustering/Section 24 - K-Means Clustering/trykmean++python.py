# Data Preprocessing Template
%reset -f
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

#using the elbow method to find optimum no. of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init = 'k-means++',max_iter= 300, n_init=10,random_state= 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('elbow Method')
plt.xlabel('number of clusters')
plt.ylabel('WCSS')
plt.show()
 #apply KMEANS
kmeans = KMeans(n_clusters=5,init = 'k-means++',max_iter= 300, n_init=10,random_state= 0)
y_kmeans = kmeans.fit_predict(X)
 

#plt KMEAMS
plt.scatter(X[y_kmeans == 0,0],X[y_kmeans == 0,1],s = 50,c = 'red' ,label = 'careful')
plt.scatter(X[y_kmeans == 1,0],X[y_kmeans == 1,1],s = 50,c = 'blue' ,label = 'standard')
plt.scatter(X[y_kmeans == 2,0],X[y_kmeans == 2,1],s = 50,c = 'green' ,label = 'target')
plt.scatter(X[y_kmeans == 3,0],X[y_kmeans == 3,1],s = 50,c = 'cyan' ,label = 'careless')
plt.scatter(X[y_kmeans == 4,0],X[y_kmeans == 4,1],s = 50,c = 'magenta' ,label = 'sensible ')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'centeroid')
plt.legend()
plt.xlabel('income')
plt.ylabel('spending score')
plt.show()