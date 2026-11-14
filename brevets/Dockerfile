FROM python:3.9-slim
MAINTAINER Willow Sack "willow0@uoregon.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]
