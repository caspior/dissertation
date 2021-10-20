
## Preparing Austin's dockless micromobility trip logs for analysis


# Loading the data:

# The database is available to download from https://drive.google.com/file/d/1uHDza25XWuaCml3jeToR6JMtOgbNwScx/view?usp=sharing

library(foreign)

micromobility <- read.csv("Dockless_Vehicle_Trips 3-27.csv")
N <- nrow(micromobility)


# Generate dates:

micromobility$date <- as.character(micromobility$Start.Time)
micromobility$date <- substr(micromobility$date, 1, 10)
micromobility$date <- as.Date(micromobility$date, "%m/%d/%Y")


# Slicing the examined period and counting scooters and e-bike trips (before cleaning):

dockless <- micromobility[which(micromobility$date>='2018-08-16' & micromobility$date<'2019-03-01'),]
S <- nrow(dockless[which(dockless$Vehicle.Type=='scooter'),])
B <- nrow(dockless[which(dockless$Vehicle.Type=='bicycle'),])
print(paste("Scooter trips:",S))
print(paste("Bicycle trips:",B))


# Day names:

dockless$dayname <- weekdays(dockless$date)


# Generate times:

library(lubridate)

dockless$time_start <- as.character(dockless$Start.Time)
dockless$time_start <- substr(dockless$time_start, 1, 23)
dockless$time_start <- parse_date_time(dockless$time_start, '%m/%d/%Y %I:%M:%S %p')
dockless$numeric_stime <- hour(dockless$time_start) + minute(dockless$time_start)/60
dockless$time_end <- as.character(dockless$End.Time)
dockless$time_end <- substr(dockless$time_end, 1, 23)
dockless$time_end <- parse_date_time(dockless$time_end, '%m/%d/%Y %I:%M:%S %p')


# Flag holidays:

dockless$holiday <- 0

# Source - https://comptroller.texas.gov/about/holidays.php

dockless[c(which(dockless$date=="2018-08-27")),"holiday"] <- 1 #Lyndon Baines Johnson Day
dockless[c(which(dockless$date=="2018-09-03")),"holiday"] <- 1 #Labor Day
dockless[c(which(dockless$date=="2018-11-22")),"holiday"] <- 1 #Thanksgiving Day
dockless[c(which(dockless$date=="2018-11-23")),"holiday"] <- 1 #Day After Thanksgivig
dockless[c(which(dockless$date=="2018-12-24")),"holiday"] <- 1 #Christmas Eve Day
dockless[c(which(dockless$date=="2018-12-25")),"holiday"] <- 1 #Christmas Day
dockless[c(which(dockless$date=="2018-12-26")),"holiday"] <- 1 #Day After Christmas
dockless[c(which(dockless$date=="2019-01-01")),"holiday"] <- 1 #New Year's Day
dockless[c(which(dockless$date=="2019-01-21")),"holiday"] <- 1 #Martin Luther King, Jr. Day
dockless[c(which(dockless$date=="2019-02-18")),"holiday"] <- 1 #Presidents' Day


# Flag weekends:

dockless$weekend <- 0
dockless[c(which(dockless$Day.of.Week==0)),"weekend"] <- 1
dockless[c(which(dockless$Day.of.Week==6)),"weekend"] <- 1
dockless[c(which(dockless$holiday==1)),"weekend"] <- 1


## Cleaning


# If exceeds 50 miles:

dockless <- dockless[c(which(dockless$Trip.Distance<=80000)),]
dockless <- dockless[c(which(dockless$Trip.Distance>0)),]
s <- nrow(dockless[which(dockless$Vehicle.Type=='scooter'),])
b <- nrow(dockless[which(dockless$Vehicle.Type=='bicycle'),])
n <- nrow(dockless)
print(paste("Dropped",N-n,"trips"))
print(paste(S-s,"scooter trips"))
print(paste(B-b,"e-bike trips"))
N <- n
S <- s
B <- b


# If exceeds 12 hours:

dockless <- dockless[c(which(dockless$Trip.Duration<=43200)),]
dockless <- dockless[c(which(dockless$Trip.Duration>0)),]
s <- nrow(dockless[which(dockless$Vehicle.Type=='scooter'),])
b <- nrow(dockless[which(dockless$Vehicle.Type=='bicycle'),])
n <- nrow(dockless)
print(paste("Dropped",N-n,"trips"))
print(paste(S-s,"scooter trips"))
print(paste(B-b,"e-bike trips"))
N <- n
S <- s
B <- b


# If exceeds 50 km/h:

dockless$speed <- dockless$Trip.Distance/dockless$Trip.Duration*3.6
dockless <- dockless[c(which(dockless$speed<=50)),]
s <- nrow(dockless[which(dockless$Vehicle.Type=='scooter'),])
b <- nrow(dockless[which(dockless$Vehicle.Type=='bicycle'),])
n <- nrow(dockless)
print(paste("Dropped",N-n,"trips"))
print(paste(S-s,"scooter trips"))
print(paste(B-b,"e-bike trips"))
N <- n
S <- s
B <- b


# If out of bounds:

dockless <- dockless[c(which(dockless$Origin.Cell.ID!="OUT_OF_BOUNDS")),]
dockless <- dockless[c(which(dockless$Destination.Cell.ID!="OUT_OF_BOUNDS")),]
dockless <- dockless[c(which(dockless$End.Latitude>29.2)),]
dockless <- dockless[c(which(dockless$End.Latitude<30.9)),]
dockless <- dockless[c(which(dockless$Start.Latitude>29.2)),]
dockless <- dockless[c(which(dockless$Start.Latitude<30.9)),]
dockless <- dockless[c(which(dockless$End.Longitude<(-97.2))),]
dockless <- dockless[c(which(dockless$End.Longitude>(-98.3))),]
dockless <- dockless[c(which(dockless$Start.Longitude<(-97.2))),]
dockless <- dockless[c(which(dockless$Start.Longitude>(-98.3))),]
s <- nrow(dockless[which(dockless$Vehicle.Type=='scooter'),])
b <- nrow(dockless[which(dockless$Vehicle.Type=='bicycle'),])
n <- nrow(dockless)
print(paste("Dropped",N-n,"trips"))
print(paste(S-s,"scooter trips"))
print(paste(B-b,"e-bike trips"))
N <- n
S <- s
B <- b


# Export database:

saveRDS(dockless, "DocklessAF.rds")

