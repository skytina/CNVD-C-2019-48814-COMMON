# CNVD-C-2019-48814 work on linux and windows
WebLogic wls9-async反序列化远程命令执行漏洞

# 说明
基于[jas502n](https://github.com/jas502n/CNVD-C-2019-48814/blob/master/cve-2017-10271/async\_command\_favicon.py)的脚本修改而成

# 使用
python async_command_favicon_all.py http://127.0.0.1:7001

# 漏洞复现

## 1. Windows Server 2012
  - servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/favicon.ico

![](images/win_server_2012_adminserver.png)


## 2. Windows Server 2012
  - servers/myserver/tmp/_WL_internal/bea_wls_internal/uwyp3r/war/favicon.ico
    - when you create WLS domain **with terminal**, it will create **myserver** instead of **AdminServer** which create WLS domain by invoking the GUI configurationwizard.

![](images/win_server_2012_myserver.png)

## 3. Linux
  - servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/favicon.ico
  
![](images/linux.png)
  