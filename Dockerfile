FROM python:3

ADD metrics.py /

RUN chmod a+x metrics.py
RUN pip install psutil

ENTRYPOINT ["python", "metrics.py"]
