"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from ui import views

'''
#from ui import views

후 direct url 설정의 경우, 

앱단위 urls보다 config urls가 우선된다.
가령, 여기서 설정하면 바로 재부팅되지만, 앱 urls는 그렇지 않다.
그리고 localhost/ 가 기본이다. 그래서 /index로 하면 안된다.

한편 이 대신 개별 앱의 urls에 자동 연결하는 방법도 있다.
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    # direct url 설정
    # path('index/', views.index, name='index'),
    # 앱의 urls 파일 설정

    path('', include('ui.urls'))
]
