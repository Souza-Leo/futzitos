# futzitos

## Criar ambiente virtual (Windows)
```shell
# Instalar python
python -m venv futzitos-env
```

## Instalar dependências

```shell
pip install -r requirements/dev.txt
```

## Rodar migrações
```shell
manage.py migrate
```


## Rodar projeto
```
manage.py runserver 8001
```