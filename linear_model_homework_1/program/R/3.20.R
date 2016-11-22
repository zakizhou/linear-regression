dataframe = t(read.csv("C:/linear_model/data/3.20.txt",header = FALSE,sep = " "))
colnames(dataframe) = c("X1","X2","X3","X4","y")
row.names(dataframe) = c(1:nrow(dataframe))
dataframe = as.data.frame(dataframe)
head(dataframe,n = 3)

model = lm(y~.,data = dataframe)
summary(model)

X_center = scale(dataframe[1:4],scale = FALSE)
matrix = t(X_center) %*% X_center
eigen.model = eigen(matrix)
eigen.values = eigen.model$values
eigen.values
sum(eigen.values[1:3]) / sum(eigen.values)
eigen.model$vectors

Z = X_center %*% eigen.model$vectors[,1:3]
Z = as.data.frame(Z,col.names=names(Z))
Z$y = dataframe$y
new.model = lm(y~.,data=Z)
summary(new.model)

eigen.model$vectors[,1:3] %*% coefficients(new.model)[2:4]

coefficients(new.model)[1] + attr(X_center,"scaled:center") %*% eigen.model$vectors[,1:3] %*% coefficients(new.model)[2:4]