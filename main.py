from flask_script import Manager, Command
from flask_migrate import MigrateCommand, Migrate
from app import make_app
from app.models import db

# app命令启动
class OurRun(Command):
    def run(self):
        app.run(debug=True)


# 获取app对象
app = make_app()

# 绑定app与数据库
migrate =Migrate(app, db)

# 命令行绑定应用
manage =Manager(app)

# 安装命令
manage.add_command('run', OurRun)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()