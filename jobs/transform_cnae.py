from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .getOrCreate()
)

cnae_schema = StructType([
    StructField("CODIGO", LongType()),
    StructField("DESCRICAO", StringType())
])

cnae_df = (

    spark
    .read
    .option("sep", ";")
    .option("header", "false")
    .option('encoding', 'latin1')
    .schema(cnae_schema)
    .csv("gs://desafio-final-318823/raw/F.K03200$Z.D10710.CNAE.csv")
    
)


(
    cnae_df
    .write
    .format("parquet")
    .save("gs://desafio-final-318823/staging/cnae/")
)