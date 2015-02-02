import  scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy import log
import urllib
from scrapy.conf import settings
import os

curpath=os.path.dirname(os.path.abspath(__file__))

class RobotSpider(scrapy.Spider):
	name ="robot"
	allowed_domains = ["zhihu.com"]
	start_urls =('http://www.zhihu.com',
		)

	robot_name ="wanghj_1990@126.com"
	robot_pwd = "623deyingxiong"


	sama_last_answer_id_path=curpath+'/last_answer_id'
	sama_last_answer_id = eval(open(sama_last_answer_id_path).read())

	def __init__(self):
		super(RobotSpider,self).__init__()

	def parse(self,response):
		#settings = Settings()
		self.refreshXsrf(response)
		#Login.
		return scrapy.FormRequest.from_response(
            response,
            formdata={'email': self.robot_name, 'password': self.robot_pwd,'_xsrf':self.xsrf,'rememberme':'y'},
            callback=self.sama_answer_page,
        )

	def sama_answer_page(self,response):
		#TODO if login success.
		self.temp={}
		for (k,v) in self.sama_last_answer_id.items():
			self.temp[k]={'last_answer_id':v,'currPage':1,'new_answer_ids':[]}
			#Get sama's Main page.
			yield Request("http://www.zhihu.com/people/{}/answers".format(k),
	                      callback=self.parse_answers_page)


	def parse_answers_page(self,response):
		sama_un = response.url.split('/')[-2]
		print 'serve ',sama_un

		sels = response.xpath("//div[@id='zh-profile-answer-list']/div[@class='zm-item']/div[@data-aid]")
		next_page = True

		for sel in sels:
			answer_id =  int(sel.xpath("@data-aid").extract()[0])

			if answer_id <= self.temp[sama_un]['last_answer_id']:
				next_page = False

			else:
				self.temp[sama_un]['new_answer_ids'].append(answer_id)

		sels=[]
		if next_page:
			self.temp[sama_un]['currPage']+=1
			sels = response.xpath("//div[@id='zh-profile-answer-list-outer']/div[@class='border-pager']/div[@class='zm-invite-pager']/span[{}]/a".
				format(self.temp[sama_un]['currPage']+1))

			#Next page.
		if len(sels) > 0:
			print 'go to next page.'
			next_page_href = sels[0].xpath("@href").extract()[0]
			yield Request("http://www.zhihu.com/people/{sama_un}/answers{next_page_href}".format(sama_un=sama_un,next_page_href=next_page_href),
				callback=self.parse_answers_page)
		else:
			#TODO Should be more elegant.

			if len(self.temp[sama_un]['new_answer_ids'])>0:
				#Update.
				self.sama_last_answer_id[sama_un] = self.temp[sama_un]['new_answer_ids'][0]
				self.update_sama_last_answer_id()

				print "new answer ids :" ,len(self.temp[sama_un]['new_answer_ids'])

				self.refreshXsrf(response)
				for new_answer_id in self.temp[sama_un]['new_answer_ids']:

					body_param = ['method='+'vote_up','params='+urllib.quote('{"answer_id":"%s"}' % new_answer_id),'_xsrf='+self.xsrf]
					body = '&'.join(body_param)

					#Upvote.
					yield Request("http://www.zhihu.com/node/AnswerVoteBarV2",
						method='POST',
		                body=body,
		                headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
		                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
		                'Origin': 'http://www.zhihu.com',
		                'X-Requested-With':'XMLHttpRequest',
		                'Accept': '*/*'},
		                callback=self.end,
		                dont_filter=True
		                )

	def end(self,response):
		print 'serve answer success....'

	def refreshXsrf(self,response):
		print 'refreshXsrf........................'
		sels = response.xpath("//input[@type='hidden' and @name='_xsrf']")
		self.xsrf = sels[0].xpath('./@value').extract()[0]

		assert self.xsrf != ''

	def update_sama_last_answer_id(self):
		with open(self.sama_last_answer_id_path,'w') as l:
			l.write(str(self.sama_last_answer_id))

