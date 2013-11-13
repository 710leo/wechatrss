#coding:utf-8
import datetime
import sys,os
import md5
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web
import model
cache = False
web.config.debug = False

render = web.template.render('/var/www/wechat/templates/',base='base')

urls = (
    '/','Index',
    '/add','Add',
    '/account/(\d+)/(\d+)','Account',
    '/rss/(\d+)','Rss',
    '/login','Login',
    '/logout','Logout',
    '/admin','Admin',
    '/submit','Submit',
    '/acc_set','Acc_set',
    '/sub_set','Sub_set',
    '/show/(\d+)','Show',
    '/hide/(\d+)','Hide',
    '/delete','Delete',
    '/about','About'
)
app = web.application(urls,globals())
session = web.session.Session(app,web.session.DiskStore(os.path.join(abspath,'sessions')),
initializer={'login':""})
application = app.wsgifunc()

class Index:
    def GET(self):
	results = model.get_wx2()
	return render.index(results)

class Add:
    def GET(self):
	if session.login == True:
	    return render.add(title='add')
	raise web.seeother('/')
    def POST(self):
	form = web.input()		
	x = web.input(myfile={})
	if 'myfile' in x:
	    filepath = x.myfile.filename.replace('\\','/')
	    filename = filepath.split('/')[-1]
	    ext = filename.split('.',1)[1]
	    if ext == 'jpg':
		homedir = os.getcwd()
		filedir = '%s/static/upload' % homedir
		now = datetime.datetime.now()
		t = "%d%d%d%d%d%d" % (now.year,now.month,now.day,now.hour,now.minute,now.second)
		filename = t + '.' + ext
		fout = open(filedir + '/'+filename,'w')
		fout.write(x.myfile.file.read())
		fout.close()
		message = u'OK!'
		error = False
	    else:
		massage = u'please jpg'
		error = True
	    model.add_account(form.wx_id,form.wx_name,form.author,form.pic,form.addr,filename)
	raise web.seeother('/')

class Account:
    def GET(self,id,page=1):
	account_info = model.get_account(int(id))
	for info in account_info:
	    page = int(page)
	    perpage = 13
	    offset = (page -1) * perpage
	    posts = model.get_list(info.account_id,offset,perpage)
	    postcount = model.get_list_num(info.account_id)
	    pages= postcount.count / perpage
	    if postcount.count % perpage != 0:
		total = 1+pages
	    total = pages
	    lastpage = int(page)-1
	    nextpage = int(page)+1
	    page3=[]
	    total=pages
	    for p in range(0,6):
		page3.append(p+int(page))
	    if page > pages:
		raise web.seeother('/account/$id/$total')
	    return render.account(id,posts=posts,pages=page3,total=total,lastpage=lastpage,nextpage=nextpage)
class Delete:
    def GET(self,id):
	if session == True:
	    model.det_account(int(id))
	    raise web.seeother('/acc_set')
	raise web.seeother('/')

class Rss:
    def GET(self,id):
	account_info = model.get_account(int(id))
	for info in account_info:
	    list = model.get_list(info.account_id)
	    return render.rss(list)

class Login:
    def GET(self):
	return render.login()
    def POST(self):
	form = web.input()
	result = model.check_log(form.user)	
	pwd = md5.new(form.password)
	pwd.digest()
	if pwd.hexdigest() == result[0].password:
	    session.login = True
	    return web.seeother('/admin')
	raise web.seeother('/login')

class Admin:
    def GET(self):
	if session.login == True:
	    return render.admin()
	raise web.seeother('/')

class Submit:
    def GET(self):
	return render.submit()
    
    def POST(self):
	form = web.input()	
	model.add_sub(form.id,form.name,form.desc)
	raise web.seeother('/')

class About:
    def GET(self):
	return render.about()


class Logout:
    def GET(self):
	session.kill()
	raise web.seeother('/')
	
class Acc_set:
    def GET(self):
	if session.login == True:
	    result = model.get_wx()
	    return render.acc_set(result)
	raise web.seeother('/')

class Sub_set:
    def GET(self):
	if session.login == True:
	    result = model.get_sub()
	    return render.sub_set(result)
	raise web.seeother('/')

class Show:
    def GET(self,id):
	if session.login == True:
	    model.show_account(int(id))
	    raise web.seeother('/acc_set')	
	raise web.seeother('/')

class Hide:
    def GET(self,id):
	if session.login == True:
	    model.hide_account(int(id))
	    raise web.seeother('/acc_set')
	raise web.seeother('/')
	
if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
