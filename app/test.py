# import pymysql
#
# db = pymysql.connect("localhost", "root", "1821400255", "myblog")
#
# cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
#
# cursor.execute('SELECT * FROM articles')
#
# data = cursor.fetchall()


def ss():
    from datetime import datetime
    from app.models import Articles
    a = Articles()
    a.title = 'testasdasdas'
    a.a_content = 'testdasdasas'
    a.body = 'testdasdasdasd'
    a.author_id = 6
    a.a_time = datetime.now()
    a.save()
    print(a.id)

ss()