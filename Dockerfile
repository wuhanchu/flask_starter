FROM wuhanchu/python:3_alpine
COPY "./" "./"

RUN pip3 install  -r ./requirements.txt   -i https://mirrors.aliyun.com/pypi/simple/ --extra-index-url  https://pypi.org/simple/
RUN ln -sf /usr/bin/python3 /usr/bin/python

RUN chmod +x ./script/run.sh

CMD ./script/run.sh
