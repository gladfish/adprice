# -*- coding:utf8 -*-

import sqlite3


class Db:

    @staticmethod
    def get_conn():
        return sqlite3.connect("adprice.db")

    @staticmethod
    def execute(sql):
        conn = Db.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    @staticmethod
    def select(sql):
        conn = Db.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        description = cursor.description
        cursor.close()
        conn.close()
        return Db.__result_to_json(rows, description)

    # 结果集转list[dict]
    @staticmethod
    def __result_to_json(rows, descriptions):
        # 表列名
        names = []
        for d in descriptions:
            names.append(d[0])

        items = []
        for row in rows:
            item = {}
            items.append(item)

            for index in range(len(names)):
                val = row[index]
                if val is None:
                    continue

                name = names[index]
                item[name] = val

        return items

