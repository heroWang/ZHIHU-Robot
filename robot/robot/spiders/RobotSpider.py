import  scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy import log
import urllib

class RobotSpider(scrapy.Spider):
	name ="robot"
	allowed_domains = ["zhihu.com"]
	start_urls =('http://www.zhihu.com',
		)

	robot_name ="wanghj_1990@126.com"
	robot_pwd = "623deyingxiong"
	sama_un ='long-min-92'

	last_answer_id = 0

	new_answer_ids=[]
	currPage = 1

	xsrf = ""
	cookie={}

	def __init__(self):
		super(RobotSpider,self).__init__()

	def parse(self,response):
		#Login.
		return scrapy.FormRequest.from_response(
            response,
            formdata={'email': self.robot_name, 'password': self.robot_pwd,'_xsrf':self.xsrf,'rememberme':'y'},
            callback=self.sama_answer_page,
        )

	def sama_answer_page(self,response):
		#TODO if login success.
		#Get sama's Main page.
		yield Request("http://www.zhihu.com/people/{}/answers".format(self.sama_un),
                      callback=self.parse_answers_page)

	def parse_answers_page(self,response):
		sels = response.xpath("//div[@id='zh-profile-answer-list']/div[@class='zm-item']/div[@data-aid]")
		stop = False
		for sel in sels:
			answer_id =  int(sel.xpath("@data-aid").extract()[0])
			if answer_id <= self.last_answer_id:
				stop = True
				return
			else:
				self.new_answer_ids.append(answer_id)

		if not stop:
			self.currPage+=1
			sels = response.xpath("//div[@id='zh-profile-answer-list-outer']/div[@class='border-pager']/div[@class='zm-invite-pager']/span[{}]/a".
				format(self.currPage+1))

			#Next page.
			if len(sels) > 0:
				next_page_href = sels[0].xpath("@href").extract()[0]
				yield Request("http://www.zhihu.com/people/{sama_un}/answers{next_page_href}".format(sama_un=self.sama_un,next_page_href=next_page_href),
					callback=self.parse_answers_page)
			else:
				#TODO Should be more elegant.

				if len(self.new_answer_ids)>0:
					#Update.
					self.last_answer_id = self.new_answer_ids

					print "new answer ids :" ,len(self.new_answer_ids)

					self.refreshXsrf(response)
					for new_answer_id in self.new_answer_ids:
						print 'answer_id ',new_answer_id

						body_param = [
													'method='+'vote_up',
													'params='+urllib.quote('{"answer_id":"%s"}' % new_answer_id),
													'_xsrf='+self.xsrf]
						body = '&'.join(body_param)

						#Upvote.
						yield Request("http://www.zhihu.com/node/AnswerVoteBarV2",method='POST',
	                  body=body,
	                  headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
	                  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	                  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
	                  'Origin': 'http://www.zhihu.com',
	                  'X-Requested-With':'XMLHttpRequest',
	                  'Accept': '*/*'
										},
	                  callback=self.after_serve_answer)
						#break


	def after_serve_answer(self,response):
		print response.url

	def refreshXsrf(self,response):
		print 'refreshXsrf........................'
		sels = response.xpath("//input[@type='hidden' and @name='_xsrf']")
		self.xsrf = sels[0].xpath('./@value').extract()[0]

		assert self.xsrf != ''

