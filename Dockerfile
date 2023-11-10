FROM python:3.9
WORKDIR /build
COPY ./requirements.txt /build/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt
ENV PYTHONPATH /build/app
COPY . /build/app
CMD ["uvicorn", "--host", "0.0.0.0", "--reload", "--reload-dir", "/app", "app.main:app"]