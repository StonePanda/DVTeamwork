from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from lxml import etree
import json
import pymysql
from screenone import models
import random

dbconn=pymysql.connect(
  host="127.0.0.1",
  database="dbdb",
  user="root",
  password="123456",
  port=3306,
  charset='utf8'
 )

my_headers = [
	'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
	'Opera/9.25 (Windows NT 5.1; U; en)',
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
	'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
	'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
	'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
	'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'
]

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		return None

header = {
	'User-Agent': random.choice(my_headers)#随机选择一个header
}

def index(request):
	return render(request,'index.html')
def search(request):
	return render(request,'searchsuggest.html')
def dvresult(request):
	return render(request,'mainui.html')

# Create your views here.
#第一个界面，接受keyword
@csrf_exempt
def keyword(request):
	if request.method == 'POST':
		try:
			keyword=request.POST.get('keyword','')
			request.session['keyword']=keyword
			#return redirect("http://127.0.0.1:8000/search/")#,permanent=True
			return HttpResponse(json.dumps("传递搜索关键词成功", ensure_ascii=False),content_type="application/json.charset=utf-8")
		except:
			return HttpResponse(json.dumps("传递搜索关键词失败", ensure_ascii=False),content_type="application/json.charset=utf-8")

'''
@csrf_exempt
def searchsuggest(request):
	if(request.method == 'POST'):
		try:
			url='https://movie.douban.com/j/subject_suggest?q='+request.session['keyword']
			#随机选择一个header
			header = {'User-Agent':random.choice(my_headers)}
			proxy={'http':'http://'+"".join(get_proxy())}
			datar=requests.get(url=url,headers=header,proxies=proxy)
			status=datar.status_code
			searchtext=datar.text
			#searchresult=json.dumps(searchtext)
			return HttpResponse(json.dumps(searchtext, ensure_ascii=False),content_type="application/json.charset=utf-8")#在跳转到下一界面的同时传递参数过去
		except:
			return HttpResponse(json.dumps("没有爬到", ensure_ascii=False),content_type="application/json.charset=utf-8") 
'''
#后期有时间应该更改为调用数据库查询
@csrf_exempt
def searchsuggest(request):
	if(request.method == 'POST'):
		try:
			searchresultlist=models.Rankmovies.objects.filter(title__contains=request.session['keyword'])
			dictjson=[]
			for searchresult in searchresultlist:
				mvjson={'episode':'','img':searchresult.cover_url,'title':searchresult.title,'url':searchresult.url,'type':'movie','year':searchresult.release_date,'sub_title':searchresult.regions,'id':searchresult.mvid}
				dictjson.append(mvjson)
			#dictjson.append({'搜索结果长度':len(searchresultlist)})
			#searchresult=json.dumps(searchtext)
			return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")#在跳转到下一界面的同时传递参数过去
		except:
			return HttpResponse(json.dumps("数据库中没有找到", ensure_ascii=False),content_type="application/json.charset=utf-8")


@csrf_exempt
def getchosedid(request):
	if request.method == 'POST':
		getid=request.POST.get('id','')#获取了用户点击的id
		request.session['geiid']=getid
		return HttpResponse(json.dumps("传递id成功", ensure_ascii=False),content_type="application/json.charset=utf-8")
	else:
		return HttpResponse(json.dumps("传递id失败", ensure_ascii=False),content_type="application/json.charset=utf-8")
	#view1需要返回的数值，需要先查询该电影的类型
	#可以在跳转过去的同时传递给下一个界面参数,单纯的返回数据可以用Httpresponse

#柱状图
@csrf_exempt
def view1(request):
	mv_msg = models.Rankmovies.objects.get(mvid=request.session['geiid'])
	type1=mv_msg.types1
	type2=mv_msg.types2
	jsontype1={'type':type1,'moviename':[],'data':[]}
	jsontype2={'type':type2,'moviename':[],'data':[]}
	if(type1 in ['传记','剧情','动作','历史','喜剧','悬疑','情色','歌舞','犯罪','纪录片']):
		type1_list=models.View1.objects.filter(type=type1)
	elif(types1 in ['冒险','动画','同性','奇幻','家庭','恐怖','惊悚','战争','武侠','灾难','爱情','短片','科幻','西部','运动','音乐','黑色电影']):
		type1_list=models.View11.objects.filter(type=type1)
	else:
		type1_list=models.View12.objects.filter(type=type1)
	mvtype1=[]
	for mv in type1_list:
		mvtype1.append((mv.score.replace('.',''),mv.name))
	mvtype1_list=sorted(mvtype1,reverse=True) #对电影按照分数排序
	for mvt1 in mvtype1_list:
		jsontype1['moviename'].append(mvt1[1])
		jsontype1['data'].append(mvt1[0])

	if(type2 in ['传记','剧情','动作','历史','喜剧','悬疑','情色','歌舞','犯罪','纪录片']):
		type2_list=models.View1.objects.filter(type=type2)
	elif(type2 in ['冒险','动画','同性','奇幻','家庭','恐怖','惊悚','战争','武侠','灾难','爱情','短片','科幻','西部','运动','音乐','黑色电影']):
		type2_list=models.View11.objects.filter(type=type2)
	else:
		type2_list=models.View12.objects.filter(type=type2)
	mvtype2=[]
	for mv in type2_list:
		mvtype2.append((mv.score.replace('.',''),mv.name))
	mvtype2_list=sorted(mvtype2,reverse=True) #对电影按照分数排序
	for mvt2 in mvtype2_list:
		jsontype2['moviename'].append(mvt2[1])
		jsontype2['data'].append(mvt2[0])
	dictjson={'mark':[[mv_msg.title,int(mv_msg.score.replace('.',''))],[mv_msg.title,int(mv_msg.score.replace('.',''))]],'data':[]}
	dictjson['data'].append(jsontype1)
	dictjson['data'].append(jsontype2)
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

#旭日图
@csrf_exempt
def view2(request):
	score=models.Rankmovies.objects.get(mvid=request.session['geiid']).score
	xingji=models.MvstarsCopy.objects.get(mvid=request.session['geiid'])
	totalxing=int(xingji.number_1num)+int(xingji.number_2num)+int(xingji.number_3num)+int(xingji.number_4num)+int(xingji.number_5num)
	dictjson=[{'name':score,'value':1,'children':[]}]

	wuxingjson={'name':'五星','value':round(int(xingji.number_5num)/totalxing,2),'children':[],'itemStyle':{'color': '#e65832'}}
	sixingjson={'name':'四星','value':round(int(xingji.number_4num)/totalxing,2),'children':[],'itemStyle':{'color': '#a87b64'}}
	saxingjson={'name':'三星','value':round(int(xingji.number_3num)/totalxing,2),'children':[],'itemStyle':{'color': '#ad213e'}}
	erxingjson={'name':'二星','value':round(int(xingji.number_2num)/totalxing,2),'children':[],'itemStyle':{'color': '#e65832'}}
	yixingjson={'name':'一星','value':round(1-round(int(xingji.number_5num)/totalxing,2)-round(int(xingji.number_4num)/totalxing,2)-round(int(xingji.number_3num)/totalxing,2)-round(int(xingji.number_2num)/totalxing,2),2),'children':[],'itemStyle':{'color': '#dd4c51'}}
	kw=models.Keywords5.objects.get(mvid=request.session['geiid'])
	#五星关键词
	wuxingkw=int(kw.star_5_1)+int(kw.star_5_2)+int(kw.star_5_3)+int(kw.star_5_4)+int(kw.star_5_5)
	if(wuxingkw==0):
		wuxingjsonkw1={'name':kw.star_5_1_name,'value':0,'itemStyle':{'color': '#d45a59'}}
		wuxingjsonkw2={'name':kw.star_5_2_name,'value':0,'itemStyle':{'color': '#f89a80'}}
		wuxingjsonkw3={'name':kw.star_5_3_name,'value':0,'itemStyle':{'color': '#f37674'}}
		wuxingjsonkw4={'name':kw.star_5_4_name,'value':0,'itemStyle':{'color': '#e75b68'}}
		wuxingjsonkw5={'name':kw.star_5_5_name,'value':0,'itemStyle':{'color': '#d0545f'}}
	else:
		wuxingjsonkw1={'name':kw.star_5_1_name,'value':round(int(kw.star_5_1)*int(xingji.number_5num)/wuxingkw/totalxing,2),'itemStyle':{'color': '#d45a59'}}
		wuxingjsonkw2={'name':kw.star_5_2_name,'value':round(int(kw.star_5_2)*int(xingji.number_5num)/wuxingkw/totalxing,2),'itemStyle':{'color': '#f89a80'}}
		wuxingjsonkw3={'name':kw.star_5_3_name,'value':round(int(kw.star_5_3)*int(xingji.number_5num)/wuxingkw/totalxing,2),'itemStyle':{'color': '#f37674'}}
		wuxingjsonkw4={'name':kw.star_5_4_name,'value':round(int(kw.star_5_4)*int(xingji.number_5num)/wuxingkw/totalxing,2),'itemStyle':{'color': '#e75b68'}}
		wuxingjsonkw5={'name':kw.star_5_5_name,'value':round(round(int(xingji.number_5num)/totalxing,2)-round(int(kw.star_5_1)*int(xingji.number_5num)/wuxingkw/totalxing,2)-round(int(kw.star_5_2)*int(xingji.number_5num)/wuxingkw/totalxing,2)-round(int(kw.star_5_3)*int(xingji.number_5num)/wuxingkw/totalxing,2)-round(int(kw.star_5_4)*int(xingji.number_5num)/wuxingkw/totalxing,2),2),'itemStyle':{'color': '#d45a59'}}
	wuxingjson['children'].append(wuxingjsonkw1)
	wuxingjson['children'].append(wuxingjsonkw2)
	wuxingjson['children'].append(wuxingjsonkw3)
	wuxingjson['children'].append(wuxingjsonkw4)
	wuxingjson['children'].append(wuxingjsonkw5)
	#四星关键词
	sixingkw=int(kw.star_4_1)+int(kw.star_4_2)+int(kw.star_4_3)+int(kw.star_4_4)+int(kw.star_4_5)
	if(sixingkw==0):
		sixingjsonkw1={'name':kw.star_4_1_name,'value':0,'itemStyle':{'color': '#c78869'}}
		sixingjsonkw2={'name':kw.star_4_2_name,'value':0,'itemStyle':{'color': '#d4ad12'}}
		sixingjsonkw3={'name':kw.star_4_3_name,'value':0,'itemStyle':{'color': '#9d5433'}}
		sixingjsonkw4={'name':kw.star_4_4_name,'value':0,'itemStyle':{'color': '#c94930'}}
		sixingjsonkw5={'name':kw.star_4_5_name,'value':0,'itemStyle':{'color': '#bb764c'}}
	else:
		sixingjsonkw1={'name':kw.star_4_1_name,'value':round(int(kw.star_4_1)*int(xingji.number_4num)/sixingkw/totalxing,2),'itemStyle':{'color': '#c78869'}}
		sixingjsonkw2={'name':kw.star_4_2_name,'value':round(int(kw.star_4_2)*int(xingji.number_4num)/sixingkw/totalxing,2),'itemStyle':{'color': '#d4ad12'}}
		sixingjsonkw3={'name':kw.star_4_3_name,'value':round(int(kw.star_4_3)*int(xingji.number_4num)/sixingkw/totalxing,2),'itemStyle':{'color': '#9d5433'}}
		sixingjsonkw4={'name':kw.star_4_4_name,'value':round(int(kw.star_4_4)*int(xingji.number_4num)/sixingkw/totalxing,2),'itemStyle':{'color': '#c89f83'}}
		sixingjsonkw5={'name':kw.star_4_5_name,'value':round(round(int(xingji.number_4num)/totalxing,2)-round(int(kw.star_4_1)*int(xingji.number_4num)/sixingkw/totalxing,2)-round(int(kw.star_4_2)*int(xingji.number_4num)/sixingkw/totalxing,2)-round(int(kw.star_4_3)*int(xingji.number_4num)/sixingkw/totalxing,2)-round(int(kw.star_4_4)*int(xingji.number_4num)/sixingkw/totalxing,2),2),'itemStyle':{'color': '#bb764c'}}
	sixingjson['children'].append(sixingjsonkw1)
	sixingjson['children'].append(sixingjsonkw2)
	sixingjson['children'].append(sixingjsonkw3)
	sixingjson['children'].append(sixingjsonkw4)
	sixingjson['children'].append(sixingjsonkw5)
	#三星关键词
	saxingkw=int(kw.star_3_1)+int(kw.star_3_2)+int(kw.star_3_3)+int(kw.star_3_4)+int(kw.star_3_5)
	if(saxingkw==0):
		saxingjsonkw1={'name':kw.star_3_1_name,'value':0,'itemStyle':{'color': '#794752'}}
		saxingjsonkw2={'name':kw.star_3_2_name,'value':0,'itemStyle':{'color': '#cc3d41'}}
		saxingjsonkw3={'name':kw.star_3_3_name,'value':0,'itemStyle':{'color': '#b14d57'}}
		saxingjsonkw4={'name':kw.star_3_4_name,'value':0,'itemStyle':{'color': '#c78936'}}
		saxingjsonkw5={'name':kw.star_3_5_name,'value':0,'itemStyle':{'color': '#8c292c'}}
	else:
		saxingjsonkw1={'name':kw.star_3_1_name,'value':round(int(kw.star_3_1)*int(xingji.number_3num)/saxingkw/totalxing,2),'itemStyle':{'color': '#794752'}}
		saxingjsonkw2={'name':kw.star_3_2_name,'value':round(int(kw.star_3_2)*int(xingji.number_3num)/saxingkw/totalxing,2),'itemStyle':{'color': '#cc3d41'}}
		saxingjsonkw3={'name':kw.star_3_3_name,'value':round(int(kw.star_3_3)*int(xingji.number_3num)/saxingkw/totalxing,2),'itemStyle':{'color': '#b14d57'}}
		saxingjsonkw4={'name':kw.star_3_4_name,'value':round(int(kw.star_3_4)*int(xingji.number_3num)/saxingkw/totalxing,2),'itemStyle':{'color': '#c78936'}}
		saxingjsonkw5={'name':kw.star_3_5_name,'value':round(round(int(xingji.number_3num)/totalxing,2)-round(int(kw.star_3_1)*int(xingji.number_3num)/saxingkw/totalxing,2)-round(int(kw.star_3_2)*int(xingji.number_3num)/saxingkw/totalxing,2)-round(int(kw.star_3_3)*int(xingji.number_3num)/saxingkw/totalxing,2)-round(int(kw.star_3_4)*int(xingji.number_3num)/saxingkw/totalxing,2),2),'itemStyle':{'color': '#8c292c'}}
	saxingjson['children'].append(saxingjsonkw1)
	saxingjson['children'].append(saxingjsonkw2)
	saxingjson['children'].append(saxingjsonkw3)
	saxingjson['children'].append(saxingjsonkw4)
	saxingjson['children'].append(saxingjsonkw5)
	#二星关键词
	erxingkw=int(kw.star_2_1)+int(kw.star_2_2)+int(kw.star_2_3)+int(kw.star_2_4)+int(kw.star_2_5)
	if(erxingkw==0):
		erxingjsonkw1={'name':kw.star_2_1_name,'value':0,'itemStyle':{'color': '#caa465'}}
		erxingjsonkw2={'name':kw.star_2_2_name,'value':0,'itemStyle':{'color': '#dfbd7e'}}
		erxingjsonkw3={'name':kw.star_2_3_name,'value':0,'itemStyle':{'color': '#be8663'}}
		erxingjsonkw4={'name':kw.star_2_4_name,'value':0,'itemStyle':{'color': '#b9a449'}}
		erxingjsonkw5={'name':kw.star_2_5_name,'value':0,'itemStyle':{'color': '#899893'}}
	else:
		erxingjsonkw1={'name':kw.star_2_1_name,'value':round(int(kw.star_2_1)*int(xingji.number_2num)/erxingkw/totalxing,2),'itemStyle':{'color': '#caa465'}}
		erxingjsonkw2={'name':kw.star_2_2_name,'value':round(int(kw.star_2_2)*int(xingji.number_2num)/erxingkw/totalxing,2),'itemStyle':{'color': '#dfbd7e'}}
		erxingjsonkw3={'name':kw.star_2_3_name,'value':round(int(kw.star_2_3)*int(xingji.number_2num)/erxingkw/totalxing,2),'itemStyle':{'color': '#be8663'}}
		erxingjsonkw4={'name':kw.star_2_4_name,'value':round(int(kw.star_2_4)*int(xingji.number_2num)/erxingkw/totalxing,2),'itemStyle':{'color': '#b9a449'}}
		erxingjsonkw5={'name':kw.star_2_5_name,'value':round(round(int(xingji.number_2num)/totalxing,2)-round(int(kw.star_2_1)*int(xingji.number_2num)/erxingkw/totalxing,2)-round(int(kw.star_2_2)*int(xingji.number_2num)/erxingkw/totalxing,2)-round(int(kw.star_2_3)*int(xingji.number_2num)/erxingkw/totalxing,2)-round(int(kw.star_2_4)*int(xingji.number_2num)/erxingkw/totalxing,2),2),'itemStyle':{'color': '#899893'}}
	erxingjson['children'].append(erxingjsonkw1)
	erxingjson['children'].append(erxingjsonkw2)
	erxingjson['children'].append(erxingjsonkw3)
	erxingjson['children'].append(erxingjsonkw4)
	erxingjson['children'].append(erxingjsonkw5)
	#一星关键词
	yixingkw=int(kw.star_1_1)+int(kw.star_1_2)+int(kw.star_1_3)+int(kw.star_1_4)+int(kw.star_1_5)
	if(yixingkw==0):
		yixingjsonkw1={'name':kw.star_1_1_name,'value':0,'itemStyle':{'color': '#f2684b'}}
		yixingjsonkw2={'name':kw.star_1_2_name,'value':0,'itemStyle':{'color': '#e73451'}}
		yixingjsonkw3={'name':kw.star_1_3_name,'value':0,'itemStyle':{'color': '#e65656'}}
		yixingjsonkw4={'name':kw.star_1_4_name,'value':0,'itemStyle':{'color': '#f89a1c'}}
		yixingjsonkw5={'name':kw.star_1_5_name,'value':0,'itemStyle':{'color': '#f68a5c'}}
	else:
		yixingjsonkw1={'name':kw.star_1_1_name,'value':round(int(kw.star_1_1)*int(xingji.number_1num)/yixingkw/totalxing,2),'itemStyle':{'color': '#f2684b'}}
		yixingjsonkw2={'name':kw.star_1_2_name,'value':round(int(kw.star_1_2)*int(xingji.number_1num)/yixingkw/totalxing,2),'itemStyle':{'color': '#e73451'}}
		yixingjsonkw3={'name':kw.star_1_3_name,'value':round(int(kw.star_1_3)*int(xingji.number_1num)/yixingkw/totalxing,2),'itemStyle':{'color': '#e65656'}}
		yixingjsonkw4={'name':kw.star_1_4_name,'value':round(int(kw.star_1_4)*int(xingji.number_1num)/yixingkw/totalxing,2),'itemStyle':{'color': '#f89a1c'}}
		yixingjsonkw5={'name':kw.star_1_5_name,'value':round(1-round(int(xingji.number_5num)/totalxing,2)-round(int(xingji.number_4num)/totalxing,2)-round(int(xingji.number_3num)/totalxing,2)-round(int(xingji.number_2num)/totalxing,2)-round(int(kw.star_1_1)*int(xingji.number_1num)/yixingkw/totalxing,2)-round(int(kw.star_1_2)*int(xingji.number_1num)/yixingkw/totalxing,2)-round(int(kw.star_1_3)*int(xingji.number_1num)/yixingkw/totalxing,2)-round(int(kw.star_1_4)*int(xingji.number_1num)/yixingkw/totalxing,2),2),'itemStyle':{'color': '#f68a5c'}}
	yixingjson['children'].append(yixingjsonkw1)
	yixingjson['children'].append(yixingjsonkw2)
	yixingjson['children'].append(yixingjsonkw3)
	yixingjson['children'].append(yixingjsonkw4)
	yixingjson['children'].append(yixingjsonkw5)

	dictjson[0]['children'].append(yixingjson)
	dictjson[0]['children'].append(erxingjson)
	dictjson[0]['children'].append(saxingjson)
	dictjson[0]['children'].append(sixingjson)
	dictjson[0]['children'].append(wuxingjson)
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")
'''
@csrf_exempt
def view2(request):
	score=models.rankmovies.objects.filter(mvid=request.session['geiid']).score
	xingji=models.mvstars_copy.filter(mvid=request.session['geiid'])
	totalxing=int(xingji.number_1num)+int(xingji.number_2num)+int(xingji.number_3num)+int(xingji.number_4num)+int(xingji.number_5num)
	dictjson={'name':score,'value':1,'children':[]}

	wuxingjson={'name':'五星','value':int(xingji.number_5num)/totalxing,'children':[],'itemStyle':{'color': '#e65832'}}
	sixingjson={'name':'四星','value':int(xingji.number_4num)/totalxing,'children':[],'itemStyle':{'color': '#e65832'}}
	saxingjson={'name':'三星','value':int(xingji.number_3num)/totalxing,'children':[],'itemStyle':{'color': '#e65832'}}
	erxingjson={'name':'二星','value':int(xingji.number_2num)/totalxing,'children':[],'itemStyle':{'color': '#e65832'}}
	yixingjson={'name':'一星','value':int(xingji.number_1num)/totalxing,'children':[],'itemStyle':{'color': '#e65832'}}
	kw=models.keywords5.filter(mvid=request.session['geiid'])
	#五星关键词
	wuxingkw=int(kw.star_5_1)+int(kw.star_5_2)+int(kw.star_5_3)+int(kw.star_5_4)+int(kw.star_5_5)
	wuxingjsonkw1={'name':kw.star_5_1_name,'value':int(kw.star_5_1)/wuxingkw,'itemStyle':{'color': '#d45a59'}}
	wuxingjsonkw2={'name':kw.star_5_2_name,'value':int(kw.star_5_2)/wuxingkw,'itemStyle':{'color': '#d45a59'}}
	wuxingjsonkw3={'name':kw.star_5_3_name,'value':int(kw.star_5_3)/wuxingkw,'itemStyle':{'color': '#d45a59'}}
	wuxingjsonkw4={'name':kw.star_5_4_name,'value':int(kw.star_5_4)/wuxingkw,'itemStyle':{'color': '#d45a59'}}
	wuxingjsonkw5={'name':kw.star_5_5_name,'value':int(kw.star_5_5)/wuxingkw,'itemStyle':{'color': '#d45a59'}}
	wuxingjson['children'].append(wuxingjsonkw1)
	wuxingjson['children'].append(wuxingjsonkw2)
	wuxingjson['children'].append(wuxingjsonkw3)
	wuxingjson['children'].append(wuxingjsonkw4)
	wuxingjson['children'].append(wuxingjsonkw5)
	#四星关键词
	sixingkw=int(kw.star_4_1)+int(kw.star_4_2)+int(kw.star_4_3)+int(kw.star_4_4)+int(kw.star_4_5)
	sixingjsonkw1={'name':kw.star_4_1_name,'value':int(kw.star_4_1)/sixingkw,'itemStyle':{'color': '#d45a59'}}
	sixingjsonkw2={'name':kw.star_4_2_name,'value':int(kw.star_4_2)/sixingkw,'itemStyle':{'color': '#d45a59'}}
	sixingjsonkw3={'name':kw.star_4_3_name,'value':int(kw.star_4_3)/sixingkw,'itemStyle':{'color': '#d45a59'}}
	sixingjsonkw4={'name':kw.star_4_4_name,'value':int(kw.star_4_4)/sixingkw,'itemStyle':{'color': '#d45a59'}}
	sixingjsonkw5={'name':kw.star_4_5_name,'value':int(kw.star_4_5)/sixingkw,'itemStyle':{'color': '#d45a59'}}
	sixingjson['children'].append(sixingjsonkw1)
	sixingjson['children'].append(sixingjsonkw2)
	sixingjson['children'].append(sixingjsonkw3)
	sixingjson['children'].append(sixingjsonkw4)
	sixingjson['children'].append(sixingjsonkw5)
	#三星关键词
	saxingkw=int(kw.star_3_1)+int(kw.star_3_2)+int(kw.star_3_3)+int(kw.star_3_4)+int(kw.star_3_5)
	saxingjsonkw1={'name':kw.star_3_1_name,'value':int(kw.star_3_1)/saxingkw,'itemStyle':{'color': '#d45a59'}}
	saxingjsonkw2={'name':kw.star_3_2_name,'value':int(kw.star_3_2)/saxingkw,'itemStyle':{'color': '#d45a59'}}
	saxingjsonkw3={'name':kw.star_3_3_name,'value':int(kw.star_3_3)/saxingkw,'itemStyle':{'color': '#d45a59'}}
	saxingjsonkw4={'name':kw.star_3_4_name,'value':int(kw.star_3_4)/saxingkw,'itemStyle':{'color': '#d45a59'}}
	saxingjsonkw5={'name':kw.star_3_5_name,'value':int(kw.star_3_5)/saxingkw,'itemStyle':{'color': '#d45a59'}}
	saxingjson['children'].append(saxingjsonkw1)
	saxingjson['children'].append(saxingjsonkw2)
	saxingjson['children'].append(saxingjsonkw3)
	saxingjson['children'].append(saxingjsonkw4)
	saxingjson['children'].append(saxingjsonkw5)
	#二星关键词
	erxingkw=int(kw.star_2_1)+int(kw.star_2_2)+int(kw.star_2_3)+int(kw.star_2_4)+int(kw.star_2_5)
	erxingjsonkw1={'name':kw.star_2_1_name,'value':int(kw.star_2_1)/erxingkw,'itemStyle':{'color': '#d45a59'}}
	erxingjsonkw2={'name':kw.star_2_2_name,'value':int(kw.star_2_2)/erxingkw,'itemStyle':{'color': '#d45a59'}}
	erxingjsonkw3={'name':kw.star_2_3_name,'value':int(kw.star_2_3)/erxingkw,'itemStyle':{'color': '#d45a59'}}
	erxingjsonkw4={'name':kw.star_2_4_name,'value':int(kw.star_2_4)/erxingkw,'itemStyle':{'color': '#d45a59'}}
	erxingjsonkw5={'name':kw.star_2_5_name,'value':int(kw.star_2_5)/erxingkw,'itemStyle':{'color': '#d45a59'}}
	erxingjson['children'].append(erxingjsonkw1)
	erxingjson['children'].append(erxingjsonkw2)
	erxingjson['children'].append(erxingjsonkw3)
	erxingjson['children'].append(erxingjsonkw4)
	erxingjson['children'].append(erxingjsonkw5)
	#一星关键词
	yixingkw=int(kw.star_1_1)+int(kw.star_1_2)+int(kw.star_1_3)+int(kw.star_1_4)+int(kw.star_1_5)
	yixingjsonkw1={'name':kw.star_1_1_name,'value':int(kw.star_1_1)/yixingkw,'itemStyle':{'color': '#d45a59'}}
	yixingjsonkw2={'name':kw.star_1_2_name,'value':int(kw.star_1_2)/yixingkw,'itemStyle':{'color': '#d45a59'}}
	yixingjsonkw3={'name':kw.star_1_3_name,'value':int(kw.star_1_3)/yixingkw,'itemStyle':{'color': '#d45a59'}}
	yixingjsonkw4={'name':kw.star_1_4_name,'value':int(kw.star_1_4)/yixingkw,'itemStyle':{'color': '#d45a59'}}
	yixingjsonkw5={'name':kw.star_1_5_name,'value':int(kw.star_1_5)/yixingkw,'itemStyle':{'color': '#d45a59'}}
	yixingjson['children'].append(yixingjsonkw1)
	yixingjson['children'].append(yixingjsonkw2)
	yixingjson['children'].append(yixingjsonkw3)
	yixingjson['children'].append(yixingjsonkw4)
	yixingjson['children'].append(yixingjsonkw5)

	dictjson['children'].append(yixingjson)
	dictjson['children'].append(erxingjson)
	dictjson['children'].append(saxingjson)
	dictjson['children'].append(sixingjson)
	dictjson['children'].append(wuxingjson)
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")
'''
#评论列表
@csrf_exempt
def view3(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'])
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view35(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'],value='5')
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view34(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'],value='4')
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view33(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'],value='3')
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view32(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'],value='2')
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view31(request):
	dictjson=[]
	comments=models.Comments.objects.filter(subject_id=request.session['geiid'],value='1')
	for comment in comments[0:7]:
		dictjson.append({'commenter':comment.authorname,'raty':comment.value,'comment':comment.content})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

#文字云
@csrf_exempt
def view4(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='0')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view45(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='5')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view44(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='4')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view43(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='3')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view42(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='2')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

@csrf_exempt
def view41(request):
	dictjson=[]
	kws=models.Keywords.objects.filter(mvid=request.session['geiid'],stars='1')
	for kw in kws[0:40]:
		dictjson.append({'name':kw.keyword,'value':int(kw.value)*100})
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")

#演员获奖
@csrf_exempt
def view5(request):
	dictjson={'price':[],'years':[],'name':[],'data':[]}
	yys=models.Yy.objects.filter(mvid=request.session['geiid'])
	yearys=[]
	name=[]
	urls=[]
	for yy in yys[0:8]:
		name.append(yy.name)
		urls.append(yy.url)
		gyaws=models.Yyaward.objects.filter(rurl=yy.url)
		for gyaw in gyaws:
			yearys.append(gyaw.year)
	years=sorted(set(yearys))
	price=[]
	dannianawards=[]#每一年
	for year in years:#每一年，price第一层
		dannianawards=[]
		for url in urls:#每个人，第一层里的第二层
			danniandanrenaward=[]
			if(len(models.Yyaward.objects.filter(rurl=url,year=year))!=0):
				dannianlist=models.Yyaward.objects.filter(rurl=url,year=year)
				for dannian in dannianlist:
					danniandanrenaward.append(dannian.award)
				dannianawards.append(danniandanrenaward)
			else:
				dannianawards.append(danniandanrenaward)
		price.append(dannianawards)
	data=[]
	for i in range(0,len(years)):
		for j in range(0,len(name)):
			data.append([i,j,len(price[i][j])])
	dictjson['price']=price
	dictjson['years']=years
	dictjson['name']=name
	dictjson['data']=data
	return HttpResponse(json.dumps(dictjson, ensure_ascii=False),content_type="application/json.charset=utf-8")
