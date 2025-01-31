
# Dockerfile, Image, Container
FROM python:3.8.9
# Or any preferred Python version.
ADD main-basic.py .
RUN pip install requests python-dotenv
RUN pip install "fastapi[standard]"
# CMD [“fastapi”, "dev", “./main-basic.py”] 
EXPOSE 8000

COPY requirements.txt /app/requirements.txt
COPY main-basic.py /app/main-basic.py
COPY entrypoint.sh /app/entrypoint.sh 
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
# Or enter the name of your unique directory and parameter set.
