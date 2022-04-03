FROM python:3.8-slim-buster
WORKDIR /APP
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3" , "-m" , "../Future_Feature/app"]