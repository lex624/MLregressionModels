#multilinear regression

datasets = read.csv('50_Startups.csv')
#datasets = datasets[,2:3]

#encode cathegorical vals
 datasets = factor (datasets$State,
                    levels= c('New York', 'California','Florida'),
                    labels = c(1,2,3))

#split datasets for training and tests
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split (datasets$Profit, SplitRatio = 0.8)
training_set = subset(datasets, split == TRUE)
test_set = subset(datasets, split == FALSE)

#Feature Scaling
# training_set[,2:3]=scale(training_set[,2:3])
# test_set[,2:3]=scale(test_set[,2:3])

#regressor = lm (formula = Profit ~ R.D.Spend +Administration +Mareting.Spend+State)
# regressor = lm (formula = Profit ~., 
#                 data = training_set)

regressor = lm (formula = Profit ~R.D.Spend +Administration +Marketing.Spend+State, 
                data = datasets)

regressor = lm (formula = Profit ~R.D.Spend +Administration +Marketing.Spend, 
                data = datasets)

regressor = lm (formula = Profit ~R.D.Spend +Marketing.Spend, 
                data = datasets)

regressor = lm (formula = Profit ~R.D.Spend, 
                data = datasets)

summary(regressor)

#prediction
#y_pred = predict( regressor, newdata = test_set)