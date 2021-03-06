from crawl_guazi.db import *


def insert_car_source(data):
    """
    插入
    """
    engine = create_engine(gl.LOCAL_ENGINE, encoding=gl.ENCODING)

    data.to_sql(name='crawler_guazi_car_source', if_exists='append', con=engine, index=False)


# def insert_or_update_base_standard_open_model_detail(data):
#     """
#     插入或更新
#     """
#     engine = create_engine(gl.TEST_PINGJIA_ENGINE, encoding=gl.ENCODING)
#
#     columns_update = [column_name + '=' + 'VALUES(' + column_name + ')' for column_name in list(data.columns)]
#     columns_update = str(columns_update).replace('\'', '')
#     columns_update = columns_update[1:len(columns_update) - 1]
#
#     columns_name = str(list(data.columns)[1:])
#     columns_name = columns_name[1:len(columns_name) - 1]
#     columns_name = columns_name.replace('\'', '')
#     with engine.begin() as con:
#         for i in range(0, len(data)):
#             if str(data.loc[i, 'id']) == 'nan':
#                 value = str([v if str(v) != 'nan' else 'null' for v in list(data.loc[i, :].values)][1:])
#                 value = value[1:len(value) - 1]
#                 value = re.sub(r'\'null\'', 'null', value)
#                 sql = 'INSERT INTO china_used_car_estimate.base_standard_open_model_detail (' + columns_name + ') VALUES (' + value + ')'
#             else:
#                 value = str(list(data.loc[i, :].values))
#                 value = value[1:len(value) - 1]
#                 value = re.sub(r' nan', ' null', value)
#                 sql = 'INSERT INTO china_used_car_estimate.base_standard_open_model_detail VALUES (' + value + ') ON DUPLICATE KEY UPDATE ' + columns_update
#             con.execute(sql)
#     con.close()