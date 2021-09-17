from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .config("spark.debug.maxToStringFields", 200)
    .getOrCreate()
)

estabelecimentos_schema = StructType([
        StructField("CNPJ_BASICO", LongType()), 
        StructField("CNPJ_ORDEM", IntegerType()),
        StructField("CNPJ_DV", ShortType()),
        StructField("IDENTIFICADOR_MATRIZ_FILIAL", ShortType()),
        StructField("NOME_FANTASIA", StringType()),
        StructField("SITUACAO_CADASTRAL", StringType()),
        StructField("DATA_SITUACAO_CADASTRAL", StringType()),
        StructField("MOTIVO_SITUACAO_CADASTRAL", StringType()),
        StructField("NOME_DA_CIDADE_NO_EXTERIOR", StringType()),
        StructField("PAIS", StringType()),
        StructField("DATA_DE_INICIO_ATIVIDADE", StringType()),
        StructField("CNAE_FISCAL_PRINCIPAL", LongType()),
        StructField("CNAE_FISCAL_SECUNDARIA", LongType()),
        StructField("TIPO_DE_LOGRADOURO", StringType()),
        StructField("LOGRADOURO", StringType()),
        StructField("NUMERO", StringType()),
        StructField("COMPLEMENTO", StringType()),
        StructField("BAIRRO", StringType()),
        StructField("CEP", LongType()),
        StructField("UF", StringType()),
        StructField("MUNICIPIO", IntegerType()),
        StructField("DDD_1", StringType()),
        StructField("TELEFONE_1", StringType()),
        StructField("DDD_2", StringType()),
        StructField("TELEFONE_2", StringType()),
        StructField("DDD_DO_FAX", StringType()),
        StructField("FAX", StringType()),
        StructField("CORREIO_ELETRONICO", StringType()),
        StructField("SITUACAO_ESPECIAL", StringType()),
        StructField("DATA_DA_SITUACAO_ESPECIAL", StringType())])


options_dict = {

    'encoding': 'ISO-8859-1',
    'sep': ';',
    'escape': "\"",
    'format': 'csv',
    'header': 'false'
}

## read data from raw
estabelecimentos_df = (

    spark
    .read
    .options(**options_dict)
    .schema(estabelecimentos_schema)
    .csv("gs://desafio-final-318823/raw/estabelecimentos/")
    
)


(
    estabelecimentos_df
    .repartition(200)
    .write
    .format('bigquery')
    .mode("overwrite")
    .option("temporaryGcsBucket", "desafio-final-318823-stage-dataproc")
    .option('table', 'modulo3.estabelecimentos')
    .save()
)
# ## save data to parquet format
(
    estabelecimentos_df
    .write
    .partitionBy('MUNICIPIO')
    .format("parquet")
    .save("gs://desafio-final-318823/staging/estabelecimentos/")
)