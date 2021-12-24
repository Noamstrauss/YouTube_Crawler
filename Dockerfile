FROM python:3.8-slim-buster
WORKDIR /APP
RUN pwd
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3" , "-m" , "User.USER_INTERFACE"]