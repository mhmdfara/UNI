from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
debugMode = True

class NotImplementedYet:
  def show(self):
    print("Not implemented yet")

# Create the Spark session
spark: SparkSession = SparkSession.builder \
  .appName("ex3") \
  .config("spark.driver.host", "localhost") \
  .master("local") \
  .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
spark.conf.set("spark.sql.shuffle.partitions", "5")


df: DataFrame = spark.read\
  .option("header", True)\
  .csv("users.csv")


df.createOrReplaceTempView('users')

#####################
# ASSIGNMENTS BEGIN #
#####################

def assignment1() -> DataFrame:
  '''
  Get the columns name, age, and income for all users with an income greater than 63000.
  Return back the Spark dataframe.
  '''
  return df.select("name", "age", "income").filter(df["income"] > 63000)

def assignment2() -> DataFrame:
  '''
  Get all education levels and the number of users with that education level.
  Columns should be named as education and education_count.
  Hint: GROUP BY
  Sort the results by the count in descending order.
  Return back the Spark dataframe.
  '''
  return df.groupBy("education").count().withColumnRenamed("count", "education_count").orderBy("education_count", ascending=False)

def assignment3() -> DataFrame:
    return df.filter(col("location") == "NYC") \
             .agg(avg(col("income").cast("double")).alias("avg_income"),
                  avg(col("spending").cast("double")).alias("avg_spending"))

def assignment4(location: str) -> DataFrame:
    return df.filter(col("location") == location) \
             .agg(avg(col("income").cast("double")).alias("avg_income"),
                  avg(col("spending").cast("double")).alias("avg_spending"))

###################
# ASSIGNMENTS END #
###################

if debugMode:
  print("------")
  print("ASSIGNMENT 1 EXPECTED RESULT:")
  print("+--------+---+------+")
  print("|    name|age|income|")
  print("+--------+---+------+")
  print("|   David| 28| 85000|")
  print("| Michael| 56|120000|")
  print("|Samantha| 50|100000|")
  print("| Matthew| 32| 90000|")
  print("|  Ashley| 45| 80000|")
  print("|  Joshua| 22| 70000|")
  print("+--------+---+------+")
  print("ASSIGNMENT 1 RESULT:")
  assignment1().show()

  print("------")
  print("ASSIGNMENT 2 EXPECTED RESULT:")
  print("+-----------+---------------+")
  print("|  education|education_count|")
  print("+-----------+---------------+")
  print("|  Bachelors|             12|")
  print("|High school|             11|")
  print("|    Masters|              7|")
  print("+-----------+---------------+")
  print("ASSIGNMENT 2 RESULT:")
  assignment2().show()

  print("------")
  print("ASSIGNMENT 3 EXPECTED RESULT:")
  print("+----------+------------+")
  print("|avg_income|avg_spending|")
  print("+----------+------------+")
  print("|   20000.0|     10300.0|")
  print("+----------+------------+")
  print("ASSIGNMENT 3 RESULT:")
  assignment3().show()

  print("------")
  print("ASSIGNMENT 4 EXPECTED RESULT WITH PARAMETER 'Charlotte':")
  print("+----------+------------+")
  print("|avg_income|avg_spending|")
  print("+----------+------------+")
  print("|    3750.0|     12625.0|")
  print("+----------+------------+")
  print("ASSIGNMENT 4 RESULT:")
  assignment4("Charlotte").show()
