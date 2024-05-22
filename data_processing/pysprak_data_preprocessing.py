from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark session
spark = SparkSession.builder.appName("AdTechPreprocessing").getOrCreate()

# Load ad impressions data from HDFS
ad_impressions_df = spark.read.json("hdfs://localhost:9000/path/to/ad_impressions")

# Load clicks and conversions data from HDFS
clicks_conversions_df = spark.read.csv("hdfs://localhost:9000/path/to/clicks_conversions", header=True)

# Load bid requests data from HDFS
bid_requests_df = spark.read.format("avro").load("hdfs://localhost:9000/path/to/bid_requests")

# Deduplicate data
ad_impressions_df = ad_impressions_df.dropDuplicates()
clicks_conversions_df = clicks_conversions_df.dropDuplicates()
bid_requests_df = bid_requests_df.dropDuplicates()

# Validate and filter data (example: filter out records with missing user ID)
ad_impressions_df = ad_impressions_df.filter(col("user_id").isNotNull())
clicks_conversions_df = clicks_conversions_df.filter(col("user_id").isNotNull())
bid_requests_df = bid_requests_df.filter(col("user_id").isNotNull())


# Correlate ad impressions with clicks and conversions
correlated_df = ad_impressions_df.join(clicks_conversions_df, "user_id").join(bid_requests_df, "user_id")

# Perform necessary aggregations or transformations
clicks_per_campaign = correlated_df.groupBy("ad_campaign_id").agg(count("clicks").alias("click_count"))

# Dump preprocessed data into HDFS
ad_impressions_df.write.mode("overwrite").parquet("hdfs://localhost:9000/path/to/processed_ad_impressions")
clicks_conversions_df.write.mode("overwrite").parquet("hdfs://localhost:9000/path/to/processed_clicks_conversions")
bid_requests_df.write.mode("overwrite").parquet("hdfs://localhost:9000/path/to/processed_bid_requests")

# Dump correlated data into HDFS
correlated_df.write.mode("overwrite").parquet("hdfs://localhost:9000/path/to/correlated_data")


# Show results
clicks_per_campaign.show()
