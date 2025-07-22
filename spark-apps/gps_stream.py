from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

schema = (
    StructType()
    .add("truck_id", StringType())
    .add("lat", DoubleType())
    .add("lon", DoubleType())
    .add("event_time", TimestampType())
)

spark = (
    SparkSession.builder
    .appName("GPSStream")
    .getOrCreate()
)

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "gps")
    .load()
)

json_df = (
    df.selectExpr("CAST(value AS STRING) as json")
    .select(from_json(col("json"), schema).alias("data"))
    .select("data.*")
)

(
    json_df.writeStream
    .format("jdbc")
    .outputMode("append")
    .option("url", "jdbc:postgresql://postgres:5432/lldl_ops")
    .option("dbtable", "truck_positions")
    .option("user", "lldl")
    .option("password", "lldl")
    .option("checkpointLocation", "/opt/spark-apps/checkpoints/gps")
    .start()
)

spark.streams.awaitAnyTermination()
