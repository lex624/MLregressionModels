datasets = read.csv('Salary_Data.csv')
#datasets = datasets[,2:3]

#split datasets for training and tests
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split (datasets$Salary, SplitRatio = 2/3)
training_set = subset(datasets, split == TRUE)
test_set = subset(datasets, split == FALSE)

#Feature Scaling
# training_set[,2:3]=scale(training_set[,2:3])
# test_set[,2:3]=scale(test_set[,2:3])

#fitting simple linear reg
regressor = lm (formula = Salary ~ YearsExperience,
                data = training_set)

#predicting new values
y_pred = predict(regressor, newdata = test_set)

#plot results
#install.packages('ggplot2')

library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y= training_set$Salary),
             colour = 'red')+
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata = training_set)),
                colour = 'blue')+
              ggtitle ('salary vs years of Experience')+
              xlab('years of experience')+
              ylab('salary')

#against test results
library(ggplot2)             
ggplot()+
  geom_point(aes(x=test_set$YearsExperience, y= training_set$Salary),
             colour = 'red')+
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata = training_set)),
            colour = 'blue')+
            ggtitle ('salary vs years of Experience(Test)')+
            xlab('years of experience')+
            ylab('salary')