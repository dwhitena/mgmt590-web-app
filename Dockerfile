FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install requests streamlit

CMD ["streamlit", "run", "--server.port", "$PORT", "--server.enableCORS", "false", "app.py"]
