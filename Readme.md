## Carga de dados CNPJ no bigquery utilizando spark

### Passo a passo

* Instale o sdk google cloud (https://cloud.google.com/sdk/docs/install)

* Faça a cópia dos dados para seu bucket google utilizando o script da pasta shell/transfer_data.sh

* Dentro da pasta infrastructure, repita os seguintes comandos
    * terraform init
    * terraform validate
    * terraform apply


Verifique o nome dos buckets utilizados e substitua nos arquivos.


Os scripts spark estão na pasta jobs