# Dockerfile, Image, Container
FROM python:3.13.1
# Or any preferred Python version.
ADD fastapi_customers.py .
RUN pip install requests python-dotenv
RUN pip install "fastapi[standard]"
# CMD [“fastapi”, "dev", “./fastapi_customers.py”] 
EXPOSE 8000

COPY requirements.txt /app/requirements.txt
COPY fastapi_customers.py /app/fastapi_customers.py
COPY entrypoint.sh /app/entrypoint.sh 
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
# Or enter the name of your unique directory and parameter set.
