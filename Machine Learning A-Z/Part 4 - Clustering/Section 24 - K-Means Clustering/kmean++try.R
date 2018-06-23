dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]
#using elbow method to find optimum no of clusters
set.seed(6)
wcss = vector()
for(i in 1:10) wcss[i] = sum(kmeans(X,i)$withinss)
plot(1:10,wcss, type = 'b',main = paste('Cluster number'), xlab = 'number of cluster' , ylab = 'WCSS')

#fit kmeans to data set
set.seed(29)
kmeans = kmeans(X,5,iter.max = 300,nstart = 10)

#visualizing the clusters
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 1,
         shade = TRUE,
         color = TRUE,
         labels = 0,
         plotchar = TRUE,
         span = TRUE,
         main = paste('cluster of clients'),
         xlab = 'Income',
         ylab = 'score')
