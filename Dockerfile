FROM python
WORKDIR /app
COPY flask_test .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python run.py
