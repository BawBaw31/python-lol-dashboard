FROM python:3.8

RUN pip3 install streamlit && pip3 install pandas && pip3 install matplotlib

COPY test.py .

COPY groupStageAnalysis.py .

COPY knockoutStageAnalysis.py .

COPY images/ ./images

COPY datasets/ ./datasets

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "test.py" ]