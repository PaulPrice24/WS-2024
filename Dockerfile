#Deriving the latest base image
FROM python:latest
#Labels as key value pair
LABEL Maintainer="me"
WORKDIR /
RUN pip install flask
RUN pip install flask-restful
#to COPY the remote file at working directory in container
COPY sample_api.py ./
EXPOSE 5000
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD [ "python", "./sample_api.py"]