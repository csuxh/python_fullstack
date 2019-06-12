#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import re
#from loggingMgr import *
import pymysql
        
def select_mysql(db, sql):
    filter = 'insert|update|create|delete'
    m = re.search(filter, sql.lower())
    #log_mgr.warning('call select_sqlserver')
    #logging.warning('call select_sqlserver')
    if m is not None:
        return  -1
    
    if db == 'US':
        conn= pymysql.connect(host='64.60.13.218',user='apexusa',password='Apexusa2015',db ='apexusa',port = 3306)
    elif db == 'SHA':
        conn= pymysql.connect(host='apexglobe.com.cn',user='view',password='@Pex2018View',db ='apexgsha',port =49999)
    elif db == 'SZ':
        conn= pymysql.connect(host='103.232.90.154',user='view',password='@Pex2018vi3w',db ='hkg_szx_prod',port = 3306)
    elif db == 'GZ':
        return None
        #conn = pymysql.connect(host='apexglobe.com.cn', user='view', password='@Pex2018View', db='apexgsha', port=49999)
    elif db == 'TSN':
        return None
        #conn = pymysql.connect(host='apexglobe.com.cn', user='view', password='@Pex2018View', db='apexgsha', port=49999)

    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def get_job_detail(job_no):
    col = ['JOB NO', 'OP', 'Company',  'MAWB NO', 'HAWB NO','CNEE', 'AGENT','PRE_ALERT_DATE']
    flag = 1
    db_list = [('XQW', 'CKG', 'NIN', 'WUH', 'HGH'), ('ORD', 'LAX', 'SFO', 'CGO', 'DFW', 'JFK', 'MIA', 'SEA', )]
    if job_no[:2] == 'AE' or job_no[2:4] == 'AE':
        sql_tmp = '''SELECT A.JOB_NO, A.OP, A.OP_COMPANY, A.SALES_COMPANY, B.MAWB_NO, C.HAWB_NO, F.ACCOUNTS_SHORT_CODE CNEE , G.ACCOUNTS_SHORT_CODE AGENT,
  DATE_FORMAT(E.PRE_ALERT_DATE,'%Y-%m-%d') 
        FROM OP_JOB A  
        LEFT JOIN op_ae_job_booking B ON A.JOB_ID = B.JOB_ID
        LEFT JOIN OP_AE_JOB C ON C.JOB_ID = A.JOB_ID 
        LEFT JOIN S_USER D ON D.USER_CODE = A.OP
        LEFT JOIN OP_AE_JOB_GOODS_STATUS E ON E.JOB_ID = A.JOB_ID
        left join s_accounts F on B.CONSIGNEE = F.ACCOUNTS_CODE
        left join s_accounts G on A.SALES_AGENT = G.ACCOUNTS_CODE
        WHERE A.JOB_NO =  "condition" '''
        sql = sql_tmp.replace('condition', job_no)
        if job_no[-3:] in db_list[0]:
            db = 'SHA'
        elif job_no[-3:] == 'HKG' or job_no[-3:] == 'SZX':
            db = 'SZ'
        elif job_no[-3:] in db_list[1]:
            db = 'US'
        elif job_no[:2] == 'GZ':
            flag = 0
            db = 'GZ'
        elif job_no[-3:] == 'TSN':
            flag = 0
            db = 'TSN'
        else:
            flag = 0
            db = '-1'
            # db = job_no[-3:]

    elif job_no[:2] == 'OE' or job_no[2:4] == 'OE':
        sql_tmp = '''SELECT A.JOB_NO, A.OP, A.OP_COMPANY, A.SALES_COMPANY,B.MBL_NO  , C.HBL_NO ,F.ACCOUNTS_SHORT_CODE CNEE , G.ACCOUNTS_SHORT_CODE AGENT,
 DATE_FORMAT(E.PRE_ALERT_DATE,'%Y-%m-%d')
        FROM OP_JOB A  
        LEFT JOIN op_oe_job_booking B ON B.JOB_ID = A.JOB_ID 
        LEFT JOIN OP_OE_JOB C ON C.JOB_ID = A.JOB_ID 
        LEFT JOIN S_USER D ON D.USER_CODE = A.OP
        LEFT JOIN OP_OE_JOB_GOODS_STATUS E ON E.JOB_ID = A.JOB_ID
        left join s_accounts F on B.CONSIGNEE = F.ACCOUNTS_CODE
        left join s_accounts G on A.SALES_AGENT = G.ACCOUNTS_CODE
        WHERE A.JOB_NO = "condition" '''
        sql = sql_tmp.replace('condition', job_no)
        if job_no[-3:] == 'APX':
            db = 'SHA'        
        elif job_no[-3:] == 'HKG' or job_no[-3:] == 'SZX':
            db = 'SZ'
        elif job_no[-3:] in db_list[1]:
            db = 'US'
        elif job_no[:2] == 'GZ':
            flag = 0
            db = 'GZ'
        elif job_no[-3:] == 'TSN':
            flag = 0
            db = 'TSN'
        else:
            flag = 0
            db = '-1'
            # db = job_no[-3:]
    else:
        flag = 0
        db = "-1"
        print("not ae or oe")

    if flag:
        data =  select_mysql(db, sql)
        return data, db
    else:
        print('no this type of db: %s' %db)
        return (('','', '', '', '', '', ''),), db
    
if __name__ == '__main__':
    sql = "SELECT @@version"
    conn_sqlserver(sql)

    result = select_sqlserver(db['engine'], sql, db['host'], db['user'], db['passwd'], db['db'])
    #logging.warning('write_data:' + str(result))
    if result == -1 or result is None:
        logging.error('no result from %s' %sql_f)
        #print("no data")
    else:
        pass
