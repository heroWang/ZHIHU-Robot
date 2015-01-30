import  scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy import log

class RobotSpider(scrapy.Spider):
	name ="robot"
	allowed_domains = ["zhihu.com"]
	start_urls =('http://www.zhihu.com',
		)

	robot_name ="wanghj_1990@126.com"
	robot_pwd = "623deyingxiong"
	sama_un ='wang-hao-jie-53'

	last_answer_url = ''
	
	xsrf = ""
	cookie={}  

	def __init__(self):
		super(RobotSpider,self).__init__()

	def parse(self,response):
		#Get xsrf token
		self.refreshXsrf(response)

		#Login.
		return scrapy.FormRequest.from_response(
            response,
            formdata={'email': self.robot_name, 'password': self.robot_pwd,'_xsrf':self.xsrf,'rememberme':'y'},
            callback=self.sama_answer_page,
        )

	def sama_answer_page(self,response):
		#TODO if login success.

		#Get xsrf token
		self.refreshXsrf(response)

		#Get sama's Main page.
		yield Request("http://www.zhihu.com/people/{}/answers".format(self.sama_un),
                      callback=self.serve_answers)

	def serve_answers(self,response):
		#print "enter mainpage",response.body
		#log.msg(response.body, spider=self, level=log.DEBUG)

		answer_urls=[]
		sels = response.xpath("//div[@id='zh-profile-answer-list']/div[@class='zm-item']/h2/a[@class='question_link']")
		for sel in sels:
			answer_urls += sel.xpath("@href").extract()

		stop = False
		#Turn to next page add answer if last_answer_url is not found.
		for answer_url in answer_urls:
			if answer_url == last_answer_url:
				stop = True
				break
			else:
				#Go for serve answer
				yield Request("http://www.zhihu.com{}".format(answer_url),
                      callback=self.serve_answer)


		#parse 


	def refreshXsrf(self,response):
		sels = response.xpath("//input[@type='hidden' and @name='_xsrf']")
		self.xsrf = sels[0].xpath('./@value').extract()[0]

		assert self.xsrf != ''

