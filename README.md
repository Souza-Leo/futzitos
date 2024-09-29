# futzitos

### - Instalar Python

### - Criar ambiente virtual e executar (Windows)
```shell
python -m venv futzitos-env
```
```shell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

futzitos-env\Scripts\activate
```


### - Instalar dependências
```shell
pip install -r requirements/dev.txt
```

### - Rodar migrações
```shell
python manage.py migrate
```

### - Rodar projeto
```
python manage.py runserver 8001
```
