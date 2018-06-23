dataset = read.csv('Data.csv')
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x,na.rm = TRUE)),
                     dataset$Age)