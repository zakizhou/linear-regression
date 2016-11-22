library(ggplot2)
library(MASS)
dataframe = t(read.csv("C:/linear_model/data/3.16.txt",header = FALSE,sep = " "))
colnames(dataframe) = c("X1","X2","y")
row.names(dataframe) = c(1:nrow(dataframe))
dataframe = as.data.frame(dataframe)
head(dataframe,n = 3)

model=lm(y~X1+X2,data=dataframe)
summary(model)

qplot(predict(model),resid(model),size=20,xlab = expression(hat(y)),ylab = expression(hat(e)))

boxcox.model = boxcox(y~X1+X2,data=dataframe)

lambda <- boxcox.model$x[which.max(boxcox.model$y)]
lambda

new.model = lm(y^lambda~X1+X2,data = dataframe)

qplot(predict(new.model),resid(new.model),size=20,xlab = expression(hat(y)),ylab = expression(hat(e)))