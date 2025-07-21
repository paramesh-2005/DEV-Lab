# Load required libraries
library(ggplot2)

# Create the dataset
set.seed(123)  # For reproducibility
df <- data.frame(
  ID = 1:10,
  Age = sample(18:64, 10, replace = TRUE),
  Income = sample(30000:90000, 10, replace = TRUE),
  Gender = c('Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male'),
  Education = c('High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'Bachelor', 'PhD', 'High School', 'Master')
)

# View first few rows
cat("First 5 rows:\n")
print(head(df, 5))

# Summary statistics
cat("\nSummary:\n")
print(summary(df))

# Check for missing values
cat("\nMissing values in each column:\n")
print(colSums(is.na(df)))

# Unique values
cat("\nUnique Genders:\n")
print(unique(df$Gender))

cat("\nUnique Education Levels:\n")
print(unique(df$Education))

# Selected columns
selected_columns <- df[, c("Age", "Income")]
cat("\nSelected Columns (Age, Income):\n")

print(head(selected_columns))

# Filtered data
filtered_data <- subset(df, Age > 30)
cat("\nFiltered Data (Age > 30):\n")
print(head(filtered_data))

# Filtered rows
filtered_rows <- subset(df, Gender == 'Male' & Education == 'Master')
cat("\nFiltered Rows (Male with Master’s):\n")
print(head(filtered_rows))

# Show plots
# Age Histogram
dev.new()  # Opens a new plot window
hist(df$Age, breaks=5, col="lightblue", main="Age Distribution", xlab="Age", ylab="Frequency", border="black")

# Income Boxplot
dev.new()
boxplot(df$Income, main="Income Distribution", ylab="Income", col="orange")

# Gender Bar Chart
dev.new()
gender_counts <- table(df$Gender)
barplot(gender_counts, col="skyblue", main="Gender Distribution", xlab="Gender", ylab="Count")

# Education Pie Chart
dev.new()
education_counts <- table(df$Education)
pie(education_counts, main="Education Distribution", 
    col=c("gold", "lightcoral", "lightgreen", "lightskyblue"), 
    labels=paste(names(education_counts), round(100*education_counts/sum(education_counts), 1), "%"))
