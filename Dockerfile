FROM python
WORKDIR /app
COPY cicd .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python run.py
