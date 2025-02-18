FROM python:3.9
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY src/ /src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
