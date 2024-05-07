# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o contêiner
COPY . .

# Exponha a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
