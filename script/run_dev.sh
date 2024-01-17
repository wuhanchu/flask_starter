if [ ! -d "./log/" ];then
  mkdir ./log
fi

gunicorn -w 8 -b 0.0.0.0:5000 run:app
