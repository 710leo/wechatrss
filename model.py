import web,datetime

db = web.database(dbn="mysql",db="wechat",user="...",pw="...")
#class model:
def get_wx():
    return db.select('account',order="id ASC")

def get_wx2():
    return db.select('account')

def add_account(wx_id,wx_name,author,pic,addr,filename):
    db.insert('account',account_id=wx_id,account_name=wx_name,author=author,pic_url=pic,account_addr=addr,date=datetime.datetime.utcnow(),account_pic=filename)

def det_account(id):
    db.delete('account',where="id=$id",vars=locals())

def show_account(id):
    db.update('account',where="id=$id",display=1,vars=locals())

def hide_account(id):
    db.update('account',where="id=$id",display=0,vars=locals())
    
def get_list(name,offset,perpage):
    return db.select('essay',what="account_id,essay_title,essay_date,essay_url",where="account_id = $name",vars = locals(),order="essay_id DESC",offset=offset,limit=perpage)

def get_list_num(name):
    return db.query("SELECT COUNT(*) AS count FROM essay where account_id=$name",vars=locals())[0]


def get_account(shu): 
    return db.select('account',what="id,account_id,account_addr,last_id",where="id = $shu",vars = locals())

def add_essay(name,title,url,essay_date):
    db.insert('essay',account_id=name,essay_title=title,essay_date=essay_date,essay_url=url,date=datetime.datetime.utcnow())

def update_account(name,last_num):
    db.update('account',where="account_id = $name",last_id=last_num,vars = locals())

def check_log(user):
    return db.select('account_admin',what="password",where="name=$user",vars = locals())
    
def get_sub():
    return db.select('submit')

def add_sub(id,name,desc):
    db.insert('submit',account_id=id,account_name=name,intr=desc)
