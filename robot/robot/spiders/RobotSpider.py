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

	new_answer_urls=[]
	currPage = 1
	
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
                      callback=self.parse_answers_page)

	def parse_answers_page(self,response):
		sels = response.xpath("//div[@id='zh-profile-answer-list']/div[@class='zm-item']/h2/a[@class='question_link']")
		stop = False
		for sel in sels:
			answer_url =  sel.xpath("@href").extract()
			if answer_url[0] == self.last_answer_url:
				stop = True
				return
			else:
				self.new_answer_urls += answer_url

		if not stop:
			self.currPage+=1
			sels = response.xpath("//div[@id='zh-profile-answer-list-outer']/div[@class='border-pager']/div[@class='zm-invite-pager']/span[{}]/a".
				format(self.currPage+1))

			print 'len(sels) of next page',len(sels)
			if len(sels) > 0:
				next_page_href = sels[0].xpath("@href").extract()[0]
				yield Request("http://www.zhihu.com/people/{sama_un}/answers{next_page_href}".format(sama_un=self.sama_un,next_page_href=next_page_href),
					callback=self.parse_answers_page)
			else:
				#TODO Should be more elegant.

				if len(self.new_answer_urls)>0: 
					#Update.
					self.last_answer_url = self.new_answer_urls[0]

					print "new answer urls :" ,len(self.new_answer_urls)

					for new_answer_url in self.new_answer_urls:
						yield Request("http://www.zhihu.com{}".format(new_answer_url),
					          callback=self.serve_answer)

	def serve_answer(self,response):
		print response.url

	def refreshXsrf(self,response):
		print 'refreshXsrf........................'
		sels = response.xpath("//input[@type='hidden' and @name='_xsrf']")
		self.xsrf = sels[0].xpath('./@value').extract()[0]

		assert self.xsrf != ''

