dataframe = t(read.csv("C:/linear_model/data/3.5.txt",header = FALSE,sep = " "))
colnames(dataframe) = c("X","y")
row.names(dataframe) = c(1:nrow(dataframe))
dataframe = as.data.frame(dataframe)
head(dataframe,n = 3)

model=lm(y~X,data=dataframe)
summary(model)

qplot(dataframe$X, dataframe$y,size=20,color="r",xlab = expression(X),ylab = expression(y))

new.value = data.frame(15.3)
colnames(new.value) = "X"
predict(model, newdata = new.value)