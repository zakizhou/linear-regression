library(ggplot2)
library(MASS)
dataframe = t(read.csv("C:/linear_model/data/3.15.txt",header = FALSE,sep = " "))
colnames(dataframe) = c("X","y")
row.names(dataframe) = c(1:nrow(dataframe))
dataframe = as.data.frame(dataframe)
head(dataframe,n = 3)

model=lm(y~X,data=dataframe)
summary(model)

qplot(predict(model),resid(model),size=20,xlab = expression(hat(y)),ylab = expression(hat(e)))

dataframe$u = sqrt(dataframe$y)
model = lm(u~X,data = dataframe)
summary(model)

qplot(predict(model),resid(model),size=20,xlab = expression(hat(u)),ylab = expression(hat(e)))

boxcox.model = boxcox(y~X,data=dataframe)
lambda <- boxcox.model$x[which.max(boxcox.model$y)]
lambda