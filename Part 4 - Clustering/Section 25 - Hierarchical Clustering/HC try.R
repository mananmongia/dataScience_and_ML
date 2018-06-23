# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# using dendrogram to find optimum no. of cluster
dendrogram = hclust(dist(X, method = 'euclidean'),method = 'ward.D')
plot(dendrogram,
     main = paste('dendrogram'),
     xlab = 'Coustomers',
     ylab = 'Eucliden Distances')

#fit cluster to dataset
hc = hclust(dist(X, method = 'euclidean'),method = 'ward.D')
y_hc = cutree(dendrogram,5)

#visualizing the results via plots
library(cluster)
clusplot(X,
         y_hc,
         shade = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('cluster of clients'),
         xlab = 'Income',
         ylab = 'score')