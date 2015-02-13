# ZHIHU-Robot
知乎点赞,评论机器人,基于[Scrapy][]构建.

**声明:机器人只是模拟一个正常用户的点赞评论等操作,没有做任何非法的事情.请使用此工具的朋友注意job执行的频率不要太过频繁,别给知乎的程序员们添麻烦.**
[Scrapy]:https://github.com/scrapy/scrapy

##功能##
* 自动点赞你的答案
* 自动感谢你的答案
* 自动评论你的答案.评论内容来自 <http://meiriyiwen.com>

##使用方法##
1. 需要首先pip install scrapy.建议在*nix环境中使用,Windows安装scrapy会很坑.安装方法见[Scrapy中文文档][]
[Scrapy中文文档]:https://scrapy-chs.readthedocs.org/zh_CN/0.24/

2. 为机器人注册一个帐号,它在知乎管理员眼里就是一个正常的用户.**记得激活邮箱**.

3. cd 到 `ZHIHU-Robot/robot/robot/spiders/`, 打开`RobotSpider.py`,找到代码

	``` python
	
		robot_name ="xxx@126.com"
		robot_pwd = "xxx"
	
	```
	把你刚注册的帐号和密码写进去.

4. 打开`last_answer_id`文件,里面以json对象的方式配置了机器人服务的**"用户主页地址的后缀名"**以及最新的答案ID,最开始的时候,答案ID写成0就行了.**"用户主页地址的后缀名"**,比如说我的主页地址是
<http://www.zhihu.com/people/wang-crazy-99>,那就写上{"wang-crazy-99":0}.当然,你也可以配置多个用户.

5. 运行机器人,需要cd 到Scrapy project的根目录`ZHIHU-Robot/robot/`执行命令`scrapy crawl robot`.如果一切顺利,命令会输出一堆http响应代码是200的日志,然后结束.

6. 根据你的需求,把它挂到crontab里.

##欢迎提交commits和issues##
开发比较仓促,而且是我写的第一个爬虫.希望懂爬虫的朋友多多提出意见,不胜感激.也欢迎提交代码丰富机器人的功能.



