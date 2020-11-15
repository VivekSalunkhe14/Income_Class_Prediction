#Importing the dataset
Salary <- read.csv("C:/Users/vivek/Desktop/indeed_job_dataset.csv")

str(Salary)

Salary$Job_Type = as.factor(Salary$Job_Type)
Salary$Salary = as.factor(Salary$Salary)
Salary$python <- as.factor(Salary$python)
Salary$sql <- as.factor(Salary$sql)
Salary$machine.learning <- as.factor(Salary$machine.learning)
Salary$r <- as.factor(Salary$r)
Salary$hadoop <- as.factor(Salary$hadoop)
Salary$tableau <- as.factor(Salary$tableau)
Salary$sas <- as.factor(Salary$sas)
Salary$spark <- as.factor(Salary$spark)
Salary$java <- as.factor(Salary$java)
Salary$Others <- as.factor(Salary$Others)


#Splitting the dataset into training and test set with a ratio of 80 to 20
library(caTools)
set.seed(123)
split = sample.split(Salary$Salary, SplitRatio = 0.8)
training_set = subset(Salary, split == TRUE)
test_set = subset(Salary, split == FALSE)

#Naive Bayes
library(e1071)
bayes <- naiveBayes(Salary ~ .,data = training_set)
summary(bayes)
trainp <- predict(bayes,training_set)
train_cm <- table(trainp,training_set$Salary)
train_cm
sum(diag(train_cm))/sum(train_cm)


testp <- predict(bayes,test_set)
test_cm <- table(testp,test_set$Salary)
test_cm
sum(diag(test_cm))/sum(test_cm)

#Multinomial
library(nnet)
multinomial = multinom(formula = Salary ~ .,data = training_set)
summary(multinomial)

trainpr <- predict(multinomial,training_set)
train_cma <- table(trainpr,training_set$Salary)
train_cma
sum(diag(train_cma))/sum(train_cma)


testpr <- predict(multinomial,test_set)
test_cma <- table(testpr,test_set$Salary)
test_cma
sum(diag(test_cma))/sum(test_cma)


#Decision Tree
#install.packages("rpart")
library(rpart)
dt = rpart(formula = Salary ~ .,
           data = training_set)
x <- predict(dt,training_set,type="class")
cm2 <- table(x,training_set$Salary)
sum(diag(cm2))/sum(cm2)

dtest <- predict(dt,test_set,type="class")
dtcm <- table(dtest,test_set$Salary)
dtcm
sum(diag(dtcm))/sum(dtcm)

