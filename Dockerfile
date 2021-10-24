FROM ubuntu:18.04

WORKDIR /mnt/c/Users/HP/Desktop/Tese/Tweet2Story_demo_final

RUN apt-get update && apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8888
COPY . .
CMD ["python", "backend.py"]