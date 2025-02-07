# Dockerfile, Image, Container
FROM python:3.13.1
# Or any preferred Python version.
ADD fastapi_invoices.py .
ADD invoice.py .
RUN pip install requests python-dotenv
RUN pip install "fastapi[standard]"
# CMD [“fastapi”, "dev", “./fastapi_invoices.py”] 
EXPOSE 8000

COPY requirements.txt /app/requirements.txt
COPY fastapi_invoices.py /app/fastapi_invoices.py
COPY invoice.py /app/invoice.py
COPY entrypoint.sh /app/entrypoint.sh 
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
# Or enter the name of your unique directory and parameter set.
