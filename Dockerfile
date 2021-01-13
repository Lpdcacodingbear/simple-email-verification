FROM  python3.8-alpine3.10

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip

ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY .env .env
COPY wait-for-it.sh wait-for-it.sh

RUN chmod a+x wait-for-it.sh
RUN chown -R someone:someone ./
USER someone

EXPOSE 5000
CMD ./wait-for-it.sh