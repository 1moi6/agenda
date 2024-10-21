# Usar a imagem oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /agenda

# Copiar o arquivo de dependências para o container
COPY requirements.txt /agenda/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o conteúdo do projeto para o container
COPY . /agenda/

# Expor a porta do Django
EXPOSE 8000

# Comando para rodar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
