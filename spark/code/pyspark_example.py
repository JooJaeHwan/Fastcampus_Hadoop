'''
[과제1] 
2008년 비행기록 데이터에서 월(month) 별 비행회수, 도착지연시간 총합/평균/최소/최대 값을 뽑아 주세요....

[과제2] 
과거 모든(1997년 ~ 2008년) 비행기록 데이터에서 연도(year)/월(month) 별 비행회수, 도착지연시간 총합/평균/최소/최대 값을 뽑아 주세요....
'''

# 과제 1 DataFrame API
# local 00:00:02
# yarn 00:00:03
import pyspark.sql.functions as fn
import time
start_time = time.time()
df = spark.read.option("header", True).option("inferSchema", False).csv("/jjwani/data/airline_on_time/2008.csv")
df.groupBy(df.Year, df.Month).agg(fn.count(df.FlightNum), fn.sum(df.ArrDelay), fn.avg(df.ArrDelay), fn.max(df.ArrDelay.cast("double")), fn.min(df.ArrDelay.cast("double"))).orderBy(df.Year.cast("integer").asc(), df.Month.cast("integer").asc()).toDF("Year", "Month", "FlightNum_Cnt", "ArrDelay_Sum", "ArrDelay_Avg", "ArrDelay_Max", "ArrDelay_Min").show(1000)
elapsed_time = time.time() - start_time
print (time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


# 과제 1 SQL문
# local 00:00:03
# yarn 00:00:04
import time
start_time = time.time()
df = spark.read.option("header", True).option("inferSchema", False).csv("/jjwani/data/airline_on_time/2008.csv")
df.createOrReplaceTempView("bigdata")
#df.printSchema()
sql("select Year, Month, count(FlightNum) as FlightNum_Cnt, sum(ArrDelay) as ArrDelay_Sum, avg(ArrDelay) as ArrDelay_Avg, max(CAST(ArrDelay AS DOUBLE)) as ArrDelay_Max, min(CAST(ArrDelay AS DOUBLE)) as ArrDelay_Min from bigdata where 1=1 group by Year, Month order by CAST(Year AS INTEGER), CAST(Month AS INTEGER)").show(1000)
elapsed_time = time.time() - start_time
print (time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


# 과제 2 DataFram API
# local 00:00:54
# yarn 00:00:59
import pyspark.sql.functions as fn
import time
start_time = time.time()
df = spark.read.option("header", True).option("inferSchema", False).csv("/jjwani/data/airline_on_time/*.csv")
df.groupBy(df.Year, df.Month).agg(fn.count(df.FlightNum), fn.sum(df.ArrDelay), fn.avg(df.ArrDelay), fn.max(df.ArrDelay.cast("double")), fn.min(df.ArrDelay.cast("double"))).orderBy(df.Year.cast("integer").asc(), df.Month.cast("integer").asc()).toDF("Year", "Month", "FlightNum_Cnt", "ArrDelay_Sum", "ArrDelay_Avg", "ArrDelay_Max", "ArrDelay_Min").show(1000)
elapsed_time = time.time() - start_time
print (time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


# 과제 2 SQL문
# local 00:00:51
# yarn 00:00:59
import time
start_time = time.time()
df = spark.read.option("header", True).option("inferSchema", False).csv("/jjwani/data/airline_on_time/*.csv")
df.createOrReplaceTempView("bigdata")
#df.printSchema()
sql("select Year, Month, count(FlightNum) as FlightNum_Cnt, sum(ArrDelay) as ArrDelay_Sum, avg(ArrDelay) as ArrDelay_Avg, max(CAST(ArrDelay AS DOUBLE)) as ArrDelay_Max, min(CAST(ArrDelay AS DOUBLE)) as ArrDelay_Min from bigdata where 1=1 group by Year, Month order by CAST(Year AS INTEGER), CAST(Month AS INTEGER)").show(1000)
elapsed_time = time.time() - start_time
print (time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))