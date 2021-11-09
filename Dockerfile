FROM python:3.8.11
COPY . ~/Fire_Exercise
WORKDIR ~/Fire_Exercise
RUN pip install -r requirements.txt
EXPOSE 5150
ENTRYPOINT ["python3"]
CMD [ "app.py" ]