from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import sqlite3
from django.template import RequestContext, loader
from Search import SemSearch
# Create your views here

def main(request):
	return render(request, "INDEX.html")

def search(request):
	Query =""
	if request.method == 'GET':
		Query = request.GET.get('query', '')
	else:
		Query = request.POST.get('query', '') 
	tree = SemSearch.rbt()
	tree.buildTree('/home/rarcher/SemanticWeb/dbs')
	result = tree.find(Query)
	if(result==None):
		return render(request, "pagenotfound.html")
	else:
		con = sqlite3.connect(result)
		c = con.cursor()
	        c.execute("select StringPredicate, StringObject from Strings")
	        data = c.fetchall()
	        c.execute("select StringObject, URIObject from URIs")
	        links = c.fetchall()
	        myData = []
	        myLinks=[]
	        for i in range(0,10):
                	d = data[i]
	                temp = [d[0],d[1]]
	                myData.append(temp)

	        for o in data:
        	        if(o[0]=="abstract"):
                	        if(o[1].find("English")>=0):
                        	        myData.append([o[0],o[1]])
	        for j in range(0,10):
	                l = links[j]
	                temp = [l[0],l[1]]
        	        myLinks.append(temp)
		InternalLinks = []
		it = tree.items()
		for x in range(0,10):
			try:
				itm = it.next()
				t = [itm[0],itm[0]]
				InternalLinks.append(t)
			except:
				t="nothing"
	        template = loader.get_template("InfoGraph1.html")
	        context = RequestContext(request, {
		'PageTitle': Query,
	        'MYDATA': myData,
	        'MYINLINKS': InternalLinks,
		'MYOUTLINKS': myLinks,
	        })
		return HttpResponse(template.render(context))
		#return HttpResponse(Query)

def basic(request):
	return HttpResponse("InfoGraph")

def index(request):
	con = sqlite3.connect('/home/rarcher/SemanticWeb/dbs/Nauru')
	c =con.cursor()
	c.execute("select StringPredicate, StringObject from Strings")
	data = c.fetchall()
	c.execute("select StringObject, URIObject from URIs")
	links = c.fetchall()
	myData = []
	myLinks=[]
	for i in range(0,10):
		d = data[i]
		temp = [d[0],d[1]]
		myData.append(temp)

        for o in data:
                if(o[0]=="abstract"):
                        if(o[1].find("English")>=0):
                                myData.append([o[0],o[1]])
	for j in range(0,10):
		l = links[j]
		temp = [l[0],l[1]]
		myLinks.append(temp)

        template = loader.get_template("InfoGraph1.html")
        context = RequestContext(request, {
        'MYDATA': myData,
	'MYLINKS': myLinks,
        })
        return HttpResponse(template.render(context))

