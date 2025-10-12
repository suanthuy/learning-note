# 01-Installing a package
## Use install.packages() and give it the name of the package you want to install. 
## dplyr - data manipulation, particularly with data frames.
## tidyverse

# install.packages("tidyverse")
# install.packages("ggplot2")
# install.packages(c("ggplot2", "gcookbook", "MASS", "dplyr"))

# 02-Loading a package

library("ggplot2")

# 03-Update packages

update.packages()
update.packages(ask = FALSE)

# 04-Load data from a delimited text file
##  <- read_csv()
data <- read.csv("datafile.csv", header = FALSE, stringsAsFactors = FALSE)

# 05-Load data from excel file
library(readxl)
data <- read_excel("datafile.xlsx", 1)
data <- read_excel("datafile.xls", sheet = 2)
data <- read_excel("datafile.xls", sheet = "Revenues")
## Drop the first column, and specify the types of the next three columns
data <- read_excel("datafile.xls", col_types = c("blank", "text", "date", "numeric"))









