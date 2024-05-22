# Imports
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("HiveQueryExample") \
    .config("spark.sql.warehouse.dir", "hdfs://localhost:9000/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Create Hive table and load data if not already present
spark.sql("CREATE TABLE IF NOT EXISTS correlated_data (ad_campaign_id STRING, user_id STRING, clicks INT, conversions INT, bid_price DOUBLE) STORED AS PARQUET")

# Query to pull insights
result_df = spark.sql("""
    SELECT ad_campaign_id, COUNT(DISTINCT user_id) as unique_users, COUNT(clicks) as total_clicks
    FROM correlated_data
    GROUP BY ad_campaign_id
""")

# Show results
result_df.show()

# Stop Spark session
spark.stop()
