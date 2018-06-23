# Data Preprocessisng
# install.packages("arules")
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv',sep = ',',rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset,topN = 50)

# Traing Apriori on Dataset
rules = apriori(dataset,parameter = list(support = 0.004, confidence = 0.2))
inspect(sort(rules[1:20],by= 'lift'))