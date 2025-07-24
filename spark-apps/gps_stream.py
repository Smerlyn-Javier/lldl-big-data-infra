from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import (
    StructType, StringType, DoubleType, TimestampType
)

schema = (StructType()
    .add("truck_id", StringType())
    .add("timestamp", StringType()) 
    .add("lat", DoubleType())
    .add("lon", DoubleType())
    .add("speed", DoubleType())
)

spark = (SparkSession.builder
         .appName("GPSStream")
         .getOrCreate())

kafka_df = (spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "truck-gps")
    .option("startingOffsets", "latest")
    .load())

json_df = (kafka_df
    .selectExpr("CAST(value AS STRING) AS json")
    .select(from_json(col("json"), schema).alias("d"))
    .select("d.*")
    .withColumn("timestamp",
                to_timestamp(col("timestamp"), "yyyy-MM-dd'T'HH:mm:ssX"))
)

def write_to_pg(batch_df, batch_id):
    (batch_df.write
        .mode("append")
        .format("jdbc")
        .option("url", "jdbc:postgresql://postgres:5432/lldl_ops_db")
        .option("dbtable", "truck_positions")
        .option("user", "admin")
        .option("password", "admin")
        .option("driver", "org.postgresql.Driver")
        .save())

(json_df.writeStream
    .foreachBatch(write_to_pg)
    .outputMode("append")
    .option("checkpointLocation", "/opt/spark-checkpoints/gps")
    .start()
    .awaitTermination())
