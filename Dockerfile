FROM python:3.6
#创建工作目录
ENV APP_PATH="/app"
COPY . $APP_PATH
WORKDIR $APP_PATH
RUN cd $APP_PATH \
        && pip3 install -r requirements.txt
CMD scrapy crawl cdfangxie