# Use uma imagem base Python
FROM python:3.12.4-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do projeto para o diretório de trabalho no container
COPY . .

# Exponha a porta em que a aplicação vai rodar
EXPOSE 8000

# Comando para rodar a aplicação usando o Uvicorn
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]