# django 프로젝트에서 DB 활용하기
기본 데이터베이스는 sqlite이고, runserver시 자동설치된다.

그리고 권장 DB 중 postgreSQL이 존재하며 이를 위한 설정 방법이 튜토리얼에 안내된다.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

https://docs.djangoproject.com/ko/4.0/ref/settings/#std:setting-DATABASES


## django 테이블 자동생성 기능
우선 기본 admin, auth 등의 기능을 위한 DB를 생성한다

python manage.py migrate

```
(터미널 창 내용 일부)

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
...

```

그 다음 아래 절차를 거쳐서 최종적으로 특정 앱 디렉토리의 models에 명시된 테이블을 자동생성한다.

#### 설정

django_prj 하위, config 하위, settings.py에서

INSTALLED_APPS 리스트에 새로 만든 앱 디렉토리의 apps.py의 UiConfig 클래스를 추가한다.

```
INSTALLED_APPS = [
    # added app
    'ui.apps.UiConfig',
    
    # basic
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### 모델 만들기

ui 디렉토리 하위 models 에서 만들고자 하는 테이블을 클래스로 선언한다.

```
from django.db import models

# Create your models here.
class t1(models.Model):
    col1 = models.IntegerField(default=0)
    col2 = models.CharField(max_length=200)
    col3 = models.DateTimeField('date published')

```

*필드=칼럼, 가령 id, text, pub_date

그리고 아래 명령어로 앱의 테이블 자동생성

python manage.py makemigrations ui


더 구체적으로 보고 싶으면

py manage.py sqlmigrate ui 0001


마지막으로 다시

py manage.py migrate

그러면 ui 앱의 migrations에 일종의 log가 남음.

## pycharm SQLITE DB 플러그인 설치(조회용...)
settings의 plugins에서 Database Navigator 설치 후 재시작

윈도우 좌측 얇은 공간에 세워진 'DB Browser' 확인 및 연결

연결 시 현재 프로젝트 디렉토리의 SQLITE3 경로를 정확히 설정해주자!

얼핏보면 자동 같은데 ... 눌러서 추가설정해야함

이를 통해 앞서서 만든 테이블 확인

=> DBeaver 등 별도 클라이언트 툴을 통해 추가 인서트 필요, 혹은 파이썬 단에서 추가

나의 경우 클라이언트 툴로 추가함

## 파이썬 함수를 통한 테이블 데이터 조회 API

```
...

import sqlite3

def index(request):
    res="Hello,i am index function of views.py of ui app of django_prj"

    # db access with sqlite3
    con = sqlite3.connect("db.sqlite3")

    cur=con.cursor()

    cur.execute("select * from ui_t1")

    rows=cur.fetchall()

    for row in rows:
        print(row) # row는 tuple
        res+= ', and after is comes from sqlite3'+' '.join(map(str,row))

    con.close()
	

    return HttpResponse(res)
```

## API와 HTML 연결 및 설정
config에서
```
urlpatterns = [
    path('admin/', admin.site.urls),

    # 앱의 urls 파일 설정
    path('', include('ui.urls'))
]
```

ui 앱 디렉토리에서 
```
def templatesAPI1(request):

    return render(request,'product-result.html')
```


## 참고자료
https://somjang.tistory.com/entry/Python-Python%EC%97%90%EC%84%9C-Sqlite3-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

https://docs.djangoproject.com/ko/4.0/intro/tutorial02/#writing-your-first-django-app-part-2