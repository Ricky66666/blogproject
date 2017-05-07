开发文档
===============


####目录结构


    ├── README.md
    ├── apps
    │   ├── __init__.py
    │   └── blog
    ├── config
    │   └── gunicorn_start.sh
    ├── db.sqlite3
    ├── django_blog
    │   ├── __init__.py
    │   ├── db.sqlite3
    │   └── sitemaps.py
    ├── doc
    │   └── develop.md
    ├── manage.py
    ├── middleware
    │   ├── __init__.py
    │   └── profile.py
    ├── requirements
    │   ├── base.txt
    │   ├── dev.txt
    │   └── prod.txt
    ├── settings
    │   ├── __init__.py
    │   ├── base.py
    │   ├── dev.py
    │   └── prod.py
    ├── static
    │   ├── css
    │   ├── favicon.ico
    │   ├── fonts
    │   ├── img
    │   └── js
    ├── templates
    │   ├── 404.html
    │   ├── about.html
    │   ├── admin
    │   └── base.html
    ├── urls.py
    └── wsgi.py

####项目(Projects) vs 应用(apps)
一个应用(App)指的某个具体的子系统，比如博客系统，评论系统等等，而项目就是由这些子系统构成的一个完成系统，一个项目可有多个应用，一个应用可存在于多个项目中。

####开发---dev.py
开发环境数据库使用的是sqlite，详情可以查看settings/dev.py文件，项目运行时是如何指定该配置的呢？启动时在manage.py中指定具体使用哪个配置文件

    # manage.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")

####生产环境---prod.py



    DJANGO_SETTINGS_MODULE=django_blog.settings.prod
    
