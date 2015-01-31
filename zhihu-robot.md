##登出
GET /logout HTTP/1.1  
Host: www.zhihu.com  
Connection: keep-alive  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Referer: http://www.zhihu.com/question/27854894  
Accept-Encoding: gzip, deflate, sdch  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6  
Cookie: q_c1=ce7e42228fcb4d639d1206a8535b9a90|1421287567000|1421287567000;  **z_c0="QUFEQWxLc1pBQUFYQUFBQVlRSlZUWS10M2xTMGk4SmVLOFVIeS1kY05EdHdvSVg2UkFWX25RPT0=|1421287567|5fbdccfe2eb3e3df03af00d6d074d3ba8d212d42";** _xsrf=b63cacd4373600541fa59b6b8307311f;  

##登出后
GET / HTTP/1.1  
Host: www.zhihu.com  
Connection: keep-alive  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Referer: http://www.zhihu.com/question/27854894  
Accept-Encoding: gzip, deflate, sdch  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6  
Cookie: q_c1=ce7e42228fcb4d639d1206a8535b9a90|1421287567000|1421287567000;   _xsrf=b63cacd4373600541fa59b6b8307311f;  

---
##登陆
POST /login HTTP/1.1  
Host: www.zhihu.com  
Connection: keep-alive  
Content-Length: 103  
Accept: */*  
Origin: http://www.zhihu.com  
X-Requested-With: XMLHttpRequest  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Content-Type: application/x-www-form-urlencoded; charset=UTF-8  
Referer: http://www.zhihu.com/  
Accept-Encoding: gzip, deflate  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6  
Cookie: __utmt=1; __utma=51854390.146915523.1422589642.1422589642.1422589642.1; __utmb=51854390.2.10.1422589642; __utmc=51854390; __utmz=51854390.1422589642.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20150129=1   

_xsrf=0cb1c9fc6798226c71b000509604f259&email=wanghj_1990%40126.com&password=623deyingxiong&rememberme=y   

---
##登陆Response
HTTP/1.1 200 OK  
Server: zhihu_nginx  
Date: Fri, 30 Jan 2015 06:15:10 GMT  
Content-Type: application/json  
Content-Length: 38  
Connection: keep-alive  
Content-Security-Policy: default-src *; frame-src *.zhihu.com getpocket.com note.youdao.com; script-src *.zhihu.com *.google-analytics.com 'unsafe-eval'; style-src *.zhihu.com 'unsafe-inline'  
Content-Encoding: gzip  
Set-Cookie: c_c=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Set-Cookie: z_c0="QUxDQ1FuZEpqZ2NYQUFBQVlRSlZUVzZ1OGxUTzJaWlhOcXI3aEJlVl94ZndrYW1RZnloNklRPT0=|1422598510|df2cec0f371ee6527208e1a88b20dc5ffdc45c00"; Domain=zhihu.com; expires=Sun, 01 Mar 2015 06:15:10 GMT; httponly; Path=/  
Set-Cookie: sinaid=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Set-Cookie: qqconn_access_token=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Set-Cookie: qqconn_openid=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Set-Cookie: l_c=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Set-Cookie: sina_access_token=; Domain=zhihu.com; expires=Thu, 30 Jan 2014 06:15:10 GMT; Path=/  
Expires: Fri, 02 Jan 2000 00:00:00 GMT  
Vary: Accept-Encoding  
Pragma: no-cache  
Cache-Control: private, no-store, max-age=0, no-cache, must-revalidate, post-check=0, pre-check=0  
X-Frame-Options: DENY  
Access-Control-Allow-Origin: http://www.zhihu.com  
Access-Control-Allow-Credentials: true  
 
 ---
 
##登陆后Get主页

GET / HTTP/1.1  
Host: www.zhihu.com  
Connection: keep-alive  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Referer: http://www.zhihu.com/  
Accept-Encoding: gzip, deflate, sdch  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6    
Cookie:q_c1=ab2c942bea5a4985bcf41a9516034205|1422589755000|1422589755000; _xsrf=2d00bb8b65bc5635df7b7fb384e20ae6; r_c=1; __utmt=1; __utma=51854390.146915523.1422589642.1422591686.1422598473.3; __utmb=51854390.4.10.1422598473; __utmc=51854390; __utmz=51854390.1422589642.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20150130=1^3=entry_date=20150129=1; c_c=4ab55e9ea84711e4825e52540a3121f7; z_c0="QUxDQ1FuZEpqZ2NYQUFBQVlRSlZUVzZ1OGxUTzJaWlhOcXI3aEJlVl94ZndrYW1RZnloNklRPT0=|1422598510|df2cec0f371ee6527208e1a88b20dc5ffdc45c00"    
 
---

##Get Main Page
GET /people/wang-hao-jie-53 HTTP/1.1  
Host: www.zhihu.com  
Connection: keep-alive  
Cache-Control: max-age=0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Accept-Encoding: gzip, deflate, sdch  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6  
Cookie: q_c1=ab2c942bea5a4985bcf41a9516034205|1422589755000|1422589755000; _xsrf=2d00bb8b65bc5635df7b7fb384e20ae6; z_c0="QUxDQ1FuZEpqZ2NYQUFBQVlRSlZUVnF6OGxUcEpZcklpWUREQlkzVGFWQWZ1M2dNQVpGSlRnPT0=|1422599770|f4e54aef78c633fcf26a6256067510f64a7aab62"; r_c=1; __utmt=1; __utma=51854390.146915523.1422589642.1422601788.1422604402.5; __utmb=51854390.2.10.1422604402; __utmc=51854390; __utmz=51854390.1422589642.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20150130=1^3=entry_date=20150130=1  

---
##点赞

**get 403**

POST /node/AnswerVoteBarV2 HTTP/1.1  
Content-Length: 85  
Accept-Language: en  
Accept-Encoding: gzip,deflate  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
User-Agent: Scrapy/0.24.4 (+http://scrapy.org)  
Host: www.zhihu.com  
Referer: http://www.zhihu.com/people/wang-hao-jie-53/answers?page=4  
Cookie: _xsrf=2c8285ab9b4c6d5ff982cab082ec5d7f;   q_c1=b9bb602c1b4a4814bfbcbb1a948aec32|1422694086000|1422694086000;  z_c0="QUxDQ1FuZEpqZ2NYQUFBQVlRSlZUY1lqOUZRV1lsY3p3SW0xYnBWeU9qZWNERmdjbkVyUzNnPT0=|1422694086|944887f9bd5e61e39625c562eacfd7919c5f6e3d"  
Content-Type: application/json    

method=vote_up&params={"answer_id":"38368491"}&_xsrf=2c8285ab9b4c6d5ff982cab082ec5d7f  

**success**

POST /node/AnswerVoteBarV2 HTTP/1.1
Host: www.zhihu.com
Content-Length: 99
Accept: */*
Origin: http://www.zhihu.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://www.zhihu.com/people/ximuliujing/answers
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: q_c1=c03bc1c59b5a4be49901ff4b26c0891f|1422448083000|1419775951000; _xsrf=11e48085a2606ce68bf69e0cb3bb10b5; c_c=17f2d1a6a7db11e4945f52540a3121f7; z_c0="QUFEQWxLc1pBQUFYQUFBQVlRSlZUYkw4OFZSc2VWRXZUVmtHMkh5aF94TTFVT09QVGQ3Qjl3PT0=|1422553010|874f0ad16dbfbbf92bd0af4a85a88ec359691d19";

method=vote_up&params=%7B%22answer_id%22%3A%2210740400%22%7D&_xsrf=11e48085a2606ce68bf69e0cb3bb10b5

**failed**

POST /node/AnswerVoteBarV2 HTTP/1.1
Connection: close
Content-Length: 98
Origin: http://www.zhihu.com
Cookie: _xsrf=5e06458bc1145d8e9ccb5ed2606613c1;   q_c1=656b893a417545bd8cbb965819607cfe|1422697462000|1422697462000;   z_c0="QUxDQ1FuZEpqZ2NYQUFBQVlRSlZUZmN3OUZSOGN5WWN3UXNIQ0Z3VEU5RGVGZUl0b2JqSWZ3PT0=|1422697463|782f4df9dd7c1d3af1b27df43d5d4aacc613a126"  
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6  
Accept-Encoding: gzip,deflate  
Accept: */*  
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36  
Host: www.zhihu.com  
Referer: http://www.zhihu.com/people/wang-hao-jie-53/answers?page=4  
X-Requested-With: XMLHttpRequest  
Content-Type: application/x-www-form-urlencoded; charset=UTF-8  

method=vote_up&params=%7B%22answer_id%22%3A%227415235%22%7D&_xsrf=5e06458bc1145d8e9ccb5ed2606613c1  

---
