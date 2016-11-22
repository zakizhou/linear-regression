library(latex2exp)
dataframe = t(read.csv("C:/linear_model/data/3.19.txt",header = FALSE,sep = " "))
colnames(dataframe) = c("y","X1","X2")
row.names(dataframe) = c(1:nrow(dataframe))
dataframe = as.data.frame(dataframe)
head(dataframe,n = 3)

X_scaled = scale.default(dataframe[2:3])
standard = cov(X_scaled)

eigen.model = eigen(standard)
max(eigen.model$values) / min(eigen.model$values)

lm.ridge(y ~ ., data = dataframe)
plot(lm.ridge(y ~ ., data = dataframe,lambda = seq(0,1,0.01)))