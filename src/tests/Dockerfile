FROM python:alpine

WORKDIR /src/
RUN apk add --no-cache bash
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD ["bash", "-c", "coverage run -m pytest tests/test_*.py -vv -Wignore"]