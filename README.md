# 掌数AI能力治理

1、当项目启动时，会自动监控把docker服务状态存入数据库中
2、完成重启，关机，开机接口化
    访问方式:
        GET:
            127.0.0.1:5000/container  获取所有容器的状态
        POST:
            127.0.0.1:5000/container  传入指定参数开启不同的服务
        参数类型：json
        参数：container_name   容器名字
              is_on           开启
              is_off          关闭
              is_restart        重启


## AI标准能力

我们目前会有一个标准扩展(ai_frame)，和各自能力范畴的能力模块。
1. ai_frame 是ai的实现规范，语音或者ocr的实现需要遵循统一个接口和规范。
    1. ClientType 客户端类型/服务厂商。
    2. AIResponse 调用返回对象。
        - code 标准返回代码，需要在表*dict*中登记有的代码，然后在各自模块进行标准化。
2. audio 语音能力模块
    - asr
    - tts
    - 声纹识别
    - 性别识别
3. ocr 图片识别能力模块

不通能力各自的*标准客户端*需要在能力模块中定义，不通的厂商单独使用文件实现接口来完成。
extension供给内部代码使用，对外提供接口的时候，需要在实现功能模块（module）来显示API接口。API接口参考*标准客户端*来实现功能，根据需求，最简单的方式就是作为一个代理调用完直接返回。   

标准调用如下
```
from extension.ai_frame import *
client = create_client(ClientType.TC,AiType.AUDIO)
response = client.asr("test.wav")
print(response.data)
```
              
## 性能测试
### locust 执行
```
env service_id=505 test_unit_id=2 locust -f ./module/report/service/performance.py --no-web -c 1 -r 1 --run-time 1h30m
```

## 运行测试用例
``` python -m pytest ./test ```
