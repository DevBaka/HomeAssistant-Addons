FROM python:3.12-slim
WORKDIR /app

RUN echo "from flask import Flask" > app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def hello():" >> app.py && \
    echo "    return 'Test addon is working!'" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=9999)" >> app.py

EXPOSE 9999

CMD ["python", "app.py"]
