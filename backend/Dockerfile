FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV OPENAI_API_KEY="your_openai_api_key"
ENV MONGO_URI="your_mongodb_connection_string"

CMD ["python", "app.py"]
