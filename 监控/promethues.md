# prometheus

## 简单安装

- server安装

```shell
# 下载 prometheus
https://prometheus.io/download/
#解压
tar xf  prometheus-2.18.1.linux-amd64 -C /opt
#运行
nohup ./prometheus >log 2>error.log &
#访问
http://192.168.135.129:9090/

#在配置文件里添加node节点
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090','node01:9100']
# 注意
# node01 这个必须要有解析（hosts/DNS）
```

- node安装

``` shell
# 下载node_exporter
https://prometheus.io/download/
#解压
tar xf node_exporter-1.0.0.linux-amd64.tar.gz -C /opt
# 运行
nohup ./node_exporter >log 2>error.log &
# 查看信息
curl 127.0.0.1:9100/metrics
```



