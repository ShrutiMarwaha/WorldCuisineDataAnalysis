# Exploratory Data Analysis and Plotting Graphs for Cuisine data
# go to the folder where output files are stored. These files contain information about Frequency of Occurence of Ingredients. Load them in R for Exploratory Data Analysis and generating graphs
setwd("/Users/shruti/Desktop/WorkMiscellaneous/Fellowships//DataIncubator/")
Cuisines <- c("African","American","Asian","Europe","NonRegional")
filenames <- c("AfricanTopIngredients.csv","AmericanTopIngredients.csv","AsianTopIngredients.csv","EuropeTopIngredients.csv","NonRegionalTopIngredients.csv")
par(mfrow=c(3,2))
TopIngredients <- list()
for(i in seq_along(filenames))
{
  data <- read.csv(filenames[i],header=T,stringsAsFactors=F)
  barplot(data[,2],names.arg=data[,1],main=paste("Frequency of Occurence of Ingredients in ", Cuisines[i], "Recpies"),col=1:5)
  TopIngredients[[i]] <- data[,1]
}
# to find the ingredient common among the top-ingredients from different continents
Reduce(intersect,((TopIngredients)))
library(limma)
VennIntersection <- function(set1,set2,set3,set4,set5)
{
  # What are the possible letters in the universe?
  universe <- sort(unique(c(set1,set2,set3,set4,set5)))
  
  # Generate a matrix, with the sets in columns and possible letters on rows
  Counts <- matrix(0, nrow=length(universe), ncol=5)
  # Populate the said matrix
  for (i in 1:length(universe)) 
  {
    Counts[i,1] <- universe[i] %in% set1
    Counts[i,2] <- universe[i] %in% set2
    Counts[i,3] <- universe[i] %in% set3
    Counts[i,4] <- universe[i] %in% set4
    Counts[i,5] <- universe[i] %in% set5
  }
  # Name the columns with the sample names
  colnames(Counts) <- Cuisines
  rownames(Counts) <- universe
  vennDiagram(vennCounts(Counts), circle.col=c(1:5), main="Intersection of Ingredients (From TopHits) across Continents")
}
par(mfrow=c(1,1))
VennIntersection(TopIngredients[[1]],TopIngredients[[2]],TopIngredients[[3]],TopIngredients[[4]],TopIngredients[[5]])
