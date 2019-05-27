# -*- coding:utf8 -*-

from db import Db
from string import Template


class Service:

    @staticmethod
    def select_category(type_, p_id):
        sql = "select * from category where p_id='%s' and type='%s' order by order_num,id" % (p_id, type_)
        return Db.select(sql)

    @staticmethod
    def select_price(c_id, length):
        sql = Template("select * from price "
                       "where category_id in (${c_id}) "
                       "and (min_length is null or min_length<=${length}) "
                       "and (max_length is null or max_length>${length}) order by category_id")
        return Db.select(sql.substitute(c_id=c_id, length=length))
