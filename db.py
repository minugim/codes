import pymysql
import cloudpickle
import os
import sys
import base64
import pickle
import copy
#profile : id / password / residence / hobby / age / nickname / gender


class database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='minu', db='project_db', charset='utf8')
        self.curs = self.db.cursor()
        self.result=()
        self.my_dir = os.getcwd()

    def get_data(self,data_list,clntsock):
        if data_list[0]=='login_info':
            print('login')
            self.login(data_list)
        elif data_list[0]=='join_info':
            print('join')
            self.join(data_list)
        elif data_list[0]=='img_send':
            print('image send')
            self.img_recv(data_list,clntsock)
        elif data_list[0]=='new_profile':
            print('new_profile')
            self.new_profile(data_list)
        elif data_list[0]=='count_users':
            print('count_users')
            return

    def login(self,data_list):
        sql = 'select id,password from profile'
        self.curs.execute(sql)
        self.db.commit()
        result = self.curs.fetchall()

        for data in result:
            if data == (data_list[1], data_list[2]):
                data_list.insert(1, True)
                return
        data_list.insert(1, False)

    def join(self,data_list):
        sql = 'select id from profile'
        self.curs.execute(sql)
        self.db.commit()
        result = self.curs.fetchall()

        for data in result:
            if data[0] == data_list[1]:
                data_list.insert(1, False)
                return

        tmp_list = copy.deepcopy(data_list)
        del(tmp_list[0])
        del(tmp_list[6])
        sql = 'CREATE TABLE id_' + data_list[1] + '( id varchar(50),is_match tinyint not null default 0,  pic1 tinyint not null default 0, pic2 tinyint not null default 0, pic3 tinyint not null default 0)'
        self.curs.execute(sql)
        self.db.commit()
        sql = 'insert into profile values (%s, %s, %s, %s ,%s, %s, %s)'
        self.curs.execute(sql, (data_list[1], data_list[2], data_list[3], data_list[4], data_list[5],data_list[6],data_list[7]))
        self.db.commit()
        data_list.insert(1, True)
        self.mkdir(data_list)
        f = open(self.my_dir + '/id_' + tmp_list[0] + '/my_profile.txt', 'wb')
        f.write(pickle.dumps(tmp_list))
        f.close()

    def new_profile(self,data_list):
        fwrite = open(self.my_dir +'/id_'+data_list[1][0]+'/my_profile.txt','wb')
        fwrite.write(pickle.dumps(data_list[1]))
        fwrite.close()
        sql='update profile set password=%s, residence=%s, hobby=%s, age=%s, nickname=%s  where id=%s'
        self.curs.execute(sql,(data_list[1][1],data_list[1][2],data_list[1][3],data_list[1][4],data_list[1][5],data_list[1][0]))
        self.db.commit()

    def mkdir(self,data_list):
        print(data_list)
        dir_path = self.my_dir + '/id_' + data_list[2]
        try:
            if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))
        except OSError:
            print('failed to mkdir' + data_list[1])


    def img_recv(self, data_list,clntsock):
        size=pickle.loads(clntsock.recv(1024))
        print(size)
        a=0
        print(data_list)
        f = open(self.my_dir+'/id_'+data_list[1]+'/me'+str(data_list[2])+'.jpg','wb')
        while size > a:
            data=clntsock.recv(10240)
            b=len(data)
            print(b)
            a=a+b
            f.write(data)
        f.close()








'''
if __name__=='__main__':
    d=database()
    sql='select id,password from profile'
    d.curs.execute(sql)
    print(d.curs.fetchall())
    a=('alsn',123)
    if a==('alsn',123):
        print(111)
'''