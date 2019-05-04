ENCODING = 'utf-8'

##########################
# 生产,测试库配置
##########################

# 运行环境[PRODUCT,TEST,LOCAL]
RUNTIME_ENVIRONMENT = 'LOCAL'

if RUNTIME_ENVIRONMENT == 'LOCAL':
    # 生产库外网
    LOCAL_DB_ADDR = '172.17.0.4'
    LOCAL_DB_USER = 'root'
    LOCAL_DB_PASSWD = '123456'
    LOCAL_ENGINE = 'mysql+pymysql://'+LOCAL_DB_USER+':'+LOCAL_DB_PASSWD+'@'+LOCAL_DB_ADDR+'/car?charset=utf8'