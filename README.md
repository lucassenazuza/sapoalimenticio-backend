# Sapo Alimentício

  O Projeto Sapo Alimentício é uma aplicação com backend desenvolvido em python e frontend desenvolvido em ReactJS https://github.com/lucassenazuza/sapoalimenticio-front
  
# Heroku
 O Projeto foi disponibilizado no Heroku, e está disponível pelo link:
 https://sapoalimenticio.herokuapp.com/
  
## Instalação
```
$ pip install -r requirements.txt
```
## Estrutura de arquivos
```
- sapoalimenticio
| - app
|  | - controllers
|  | - services
|  |  | - scripts
|  | - models
| - alimentos
| - logs
```

## Endpoints
```
### GET /populate
Faz a leitura dos arquivos texto disponibilizados na pasta **alimentos** e salva os mesmos em um banco de dados sqlite.

### GET /allproducts
Retorna todos produtos cadastrados no banco

### GET /listcarbo
Retorna os produtos com maior quantidade de carboidratos

### GET /listprotein
Retorna os produtos com maior quantidade de proteínas

### GET /listfat
Retorna os produtos com maior quantidade de gordura
