from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .getOrCreate()
)
municipios_schema = StructType([
    StructField("CODIGO", LongType()),
    StructField("NOME", StringType())
])

# read data from raw
municipios_df = (
    
    spark
    .read
    .option("sep", ";")
    .option("header", "false")
    .option('encoding', 'latin1')
    .schema(municipios_schema)
    .csv("gs://desafio-final-318823/raw/F.K03200$Z.D10710.MUNIC.csv")

)

(
    municipios_df
    .write
    .format('bigquery')
    .option("temporaryGcsBucket", "desafio-final-318823-stage-dataproc")
    .option('table', 'modulo3.municipios')
    .save()
)