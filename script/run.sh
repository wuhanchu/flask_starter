if [ ! -d "./log/" ];then
  mkdir ./log
fi

# celery
rm celery*
python3 run.py --celery >log/celery_work.log 2>&1  < /dev/null &
python3 run.py --celery --beat >log/celery_beat.log 2>&1  < /dev/null &

# app run
core_num=${CORE_NUM:-5}
time_out=${TIME_OUT:-600}
param_str=${PARAM_STR}

echo "core_num:$core_num"
echo "time_out:$time_out"
echo "param_str:$param_str"

gunicorn -w $core_num -t $time_out  --worker-class gevent --worker-connections 2000  $param_str -b 0.0.0.0:5000 run:app
