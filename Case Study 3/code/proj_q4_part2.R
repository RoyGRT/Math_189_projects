data <- read.table("hcmv.txt", header=TRUE)
head(data)

regionsplit <- function(num_interval, gene, site){
  count.int <- table(cut(site, breaks = seq(1, length(gene), length.out=num_interval+1), include.lowest=TRUE))
  count.vector <- as.vector(count.int)
  count.tab <- table(factor(count.vector,levels=0:max(count.vector)))
  df = data.frame(counts = as.numeric(count.tab))
  return (df)
}


for (i in c(30,50,70,100,150,200,500,1000,2000,3000)){
  biggest_cluster = max(regionsplit(i, c(1:229354), data$location)$counts)
  result = c()
  for(j in c(1:2000)){
    sample = data.frame(location = sort(sample(1:229354, size = 296, replace=FALSE)))
    result[j] = max(regionsplit(i, c(1:229354), sample$location)$counts)
  }
  print(sum(biggest_cluster <= result) / 2000)
}



