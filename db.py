import pymysql
import cloudpickle
import os
import sys
import base64
import pickle
import copy

#profile : id / password / residence / hobby / age / nickname / gender / online


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
        elif data_list[0]=='new_profile':
            print('new_profile')
            self.new_profile(data_list)
        elif data_list[0]=='count_users':
            print('count_users')
            return
        elif data_list[0]=='initiate_match':
            print('initiate_match')
            self.get_match_info(data_list)
        else:
            return
        '''
        elif data_list[0]=='img_send':
        print('image send')
        self.img_recv(data_list,clntsock)
        '''

    def login(self,data_list):
        sql = 'select id,password,online from profile'
        self.curs.execute(sql)
        self.db.commit()
        result = self.curs.fetchall()
        print(1)
        for data in result:
            if data == (data_list[1], data_list[2], 0):
                data_list.insert(1, True)
                print(data_list)
                sql = "update profile set online=1 where id=%s"
                print(3)
                self.curs.execute(sql,(data_list[2],))
                print(4)
                self.db.commit()
                print(5)
                return
        data_list.insert(1, False)

    def join(self,data_list):
        sql = 'select id from profile'
        self.curs.execute(sql)
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
        if data_list[7] == '남성':
            sql = 'select id from profile where gender="여성"'
            self.curs.execute(sql)
            self.result = self.curs.fetchall()
            for i in self.result:
                sql = "insert into id_"+ data_list[1] +" values (%s ,0,0,0,0)"
                print(sql)
                self.curs.execute(sql,i[0])
            self.db.commit()
        else:
            sql = 'select id from profile where gender="남성"'
            self.curs.execute(sql)
            self.result = self.curs.fetchall()
            for i in self.result:
                sql = "insert into id_" + data_list[1] + " values (%s,0,0,0,0)"
                print(sql)
                self.curs.execute(sql,i[0])
            self.db.commit()

        sql = 'insert into profile values (%s, %s, %s, %s ,%s, %s, %s, 0)'
        self.curs.execute(sql, (data_list[1], data_list[2], data_list[3], data_list[4], data_list[5],data_list[6],data_list[7]))
        self.db.commit()
        data_list.insert(1, True)
        self.mkdir(data_list)
        f = open(self.my_dir + '/id_' + tmp_list[0] + '/my_profile.txt', 'wb')
        f.write(pickle.dumps(tmp_list))
        f.close()
        print('profile created')

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

    # 클라이언트로 보내는 msg_list = ['initiate_match', True, id ,[id, nickname , residence ,hobby , age , gender]] or ['initiate_match',False ,id]
    def get_match_info(self,data_list):
        sql = 'select gender from profile where id=%s'
        self.curs.execute(sql,(data_list[1],))
        gender = self.curs.fetchall()[0][0]

        sql = "select id from profile where gender!='"+gender+"' and id not in (select id from id_"+data_list[1]+")"
        print(sql)
        self.curs.execute(sql)
        new_id_list = self.curs.fetchall()

        if len(new_id_list):
            for i in new_id_list:
                sql = "insert into id_" + data_list[1] + " values ('"+ i[0] +"',0,0,0,0)"
                print(sql)
                self.curs.execute(sql)
                self.db.commit()

        sql = 'select id,nickname,residence,hobby,age,gender from profile where id in (select id from id_'+data_list[1]+' where is_match=0)'
        self.curs.execute(sql)
        match_list = self.curs.fetchall()
        print(match_list)
        if not len(match_list):
            data_list.insert(1,False)
            return

        # 매치될 수 있는 리스트중 아무나 한명 선택 ,리스트는 [ id, nickname , residence ,hobby , age ]
        print(match_list[0])
        data_list.insert(1,True)
        data_list.append(match_list[0])









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