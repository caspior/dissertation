
## Preparing Austin's bikesahring trip logs for analysis


# Loading the data:

# The database is available to download from https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s

setwd("/Users/avital/Documents/GitHub/dissertation")

library(foreign)

bcycle <- read.csv("Austin_B-Cycle_Trips.csv")
total <- nrow(bcycle)


# Remove if exceeds 12 hours:

bcycle <- bcycle[c(which(bcycle$Trip.Duration.Minutes<=720)),]
bcycle <- bcycle[c(which(bcycle$Trip.Duration.Minutes>0)),]
N <- nrow(bcycle)
print(paste("Droped",total-N,"trips"))


#Generate dates:

bcycle$date <- as.character(bcycle$Checkout.Date)
bcycle$date <- substr(bcycle$date, 1, 10)
bcycle$date <- as.Date(bcycle$date, "%m/%d/%Y")


#Day names:

bcycle$dayname <- weekdays(bcycle$date)
bcycle$Day.of.Week <- 9
n <- nrow(bcycle)

bcycle[which(bcycle$dayname=="Sunday"),15] <- 0
bcycle[which(bcycle$dayname=="Monday"),15] <- 1
bcycle[which(bcycle$dayname=="Tuesday"),15] <- 2
bcycle[which(bcycle$dayname=="Wednesday"),15] <- 3
bcycle[which(bcycle$dayname=="Thursday"),15] <- 4
bcycle[which(bcycle$dayname=="Friday"),15] <- 5
bcycle[which(bcycle$dayname=="Saturday"),15] <- 6


#Holidays:

bcycle$holiday <- 0

bcycle[c(which(bcycle$date=="2017-09-04")),16] <- 1 #Labor Day
bcycle[c(which(bcycle$date=="2017-11-23")),16] <- 1 #Thanksgiving Day
bcycle[c(which(bcycle$date=="2017-11-24")),16] <- 1 #Day After Thanksgivig
bcycle[c(which(bcycle$date=="2017-12-24")),16] <- 1 #Christmas Eve Day
bcycle[c(which(bcycle$date=="2017-12-25")),16] <- 1 #Christmas Day
bcycle[c(which(bcycle$date=="2017-12-26")),16] <- 1 #Day After Christmas
bcycle[c(which(bcycle$date=="2017-01-01")),16] <- 1 #New Year's Day
bcycle[c(which(bcycle$date=="2018-01-16")),16] <- 1 #Martin Luther King, Jr. Day
bcycle[c(which(bcycle$date=="2018-02-20")),16] <- 1 #Presidents' Day

bcycle[c(which(bcycle$date=="2018-08-27")),16] <- 1 #Lyndon Baines Johnson Day
bcycle[c(which(bcycle$date=="2018-09-03")),16] <- 1 #Labor Day
bcycle[c(which(bcycle$date=="2018-11-22")),16] <- 1 #Thanksgiving Day
bcycle[c(which(bcycle$date=="2018-11-23")),16] <- 1 #Day After Thanksgivig
bcycle[c(which(bcycle$date=="2018-12-24")),16] <- 1 #Christmas Eve Day
bcycle[c(which(bcycle$date=="2018-12-25")),16] <- 1 #Christmas Day
bcycle[c(which(bcycle$date=="2018-12-26")),16] <- 1 #Day After Christmas
bcycle[c(which(bcycle$date=="2019-01-01")),16] <- 1 #New Year's Day
bcycle[c(which(bcycle$date=="2019-01-21")),16] <- 1 #Martin Luther King, Jr. Day
bcycle[c(which(bcycle$date=="2019-02-18")),16] <- 1 #Presidents' Day


#Weekends:

bcycle$weekend <- 0
bcycle[c(which(bcycle$dayname=="Saturday")),17] <- 1
bcycle[c(which(bcycle$dayname=="Sunday")),17] <- 1
bcycle[c(which(bcycle$holiday==1)),17] <- 1


#Export database:

saveRDS(bcycle, "bcycle.rds")
write.csv(bcycle, "bcycle.csv")

