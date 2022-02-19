# django 프로젝트에 html과 static(css+js+img) 연동하기

## API와 HTML 연결 및 설정
ui 앱 디렉토리에서 

```
def templatesAPI1(request):

    return render(request,'product-result.html')
```

config 디렉토리에서

 STATIC_URL = 'static/' 아래에 아래 추가
```
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'ui','static')
] #static 파일들이 어디에 있는지를 쓰는곳
```

그리고, 렌더링 하고자 하는 html 파일 상단에

{% load static %}


그리고 아래와 같은 추가 경로 삽입

<link rel="stylesheet" href="{% static 'css/product-result.css' %}">

<img src="{% static 'assets/img/prod1.jpg' %}">



## 참고자료
https://free-eunb.tistory.com/42