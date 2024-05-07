FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install uvicorn
RUN pip install httpx
RUN pip install PyJWT
RUN pip install python-multipart

ENV PATH="/usr/local/bin:${PATH}"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
