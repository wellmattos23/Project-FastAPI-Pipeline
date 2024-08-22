## Construção de API utilizando FastAPI

### Configuração do ambiente

* *Versão do Python 3.12+ instalada*

### Instalando pyenv via PowerShell 
```
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

* *fechar e abrir novamente o terminal*

```
pip install pyenv 3.12.3
```
<br>

### Instalando do pipx

```
pip install pipx
```
<br>

### Instalando do poetry

```
pipx install poetry
```
```
pipx ensurepath
```
* *fechar e abrir o terminal novamente*
<br>

### Criando um novo projeto

```
poetry new api
cd api
```

* *para usaremos exatamente a versão 3.12 no projeto alteramos o arquivo de configuração do projeto o pyproject.toml na raiz do projeto:*

```
[tool.poetry.dependencies]
python = "3.12.*"
```
<br>

### Criando ambiente virtual com poetry e instalando o FastAPI
* *execultar o código dentro da pasta do projeto*
```
poetry install 
poetry add fastapi
```
<br>

### Criando o código Python
* *crie o arquivo app.py dento da pasta do projeto*

```
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World!'}
```
<br>

### Ativando o ambiente virtual e rodando o servidor Uvicorn

```
poetry shell
install poetry[standard]
fastapi dev api/app.py
```
<br>

### O terminal retornara a seguinte mensagem:

<img src="/img/Screenshot_37.png">

### Agora, com o servidor inicializado, podemos usar um cliente para acessar o endereço http://127.0.0.1:8000

<img src="/img/Screenshot_38.png">

