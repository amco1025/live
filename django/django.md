# Django

## 클라이언트와 서버
```
1. 클라이언트-서버 구조
 - 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
 - 클라이언트가 요청하면 서버가 반응하는 구조
```

## Django 사용
```
1. Django 설치
 - pip install django==3.2.18

2. 프로젝트 생성
 - django-admin startproject firstpjt

3. 서버 실행
 - python manage.py runserver
```

## 가상환경
```
1. 가상환경 생성
 - python -m venv venv

2. 가상환경 활성화
 - source venv/Scripts/activate

3. 가상환경 비활성화
 - deactivate
```

## 프로젝트와 앱
```
1. 프로젝트 구조
 (1) __init__.py
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드를 작성하지 않음
 (2) asgi.py
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정하지 않음
 (3) settings.py
  - Django 프로젝트 설정을 관리
 (4) urls.py
  - 사이트의 url과 적절한 views의 연결을 지정
 (5) wsgi.py
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정하지 않음
 (6) manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

2. 앱
 (1) 앱 생성
  - python manage.py startapp articles

 (2) 애플리케이션 등록
  - 프로젝트 -> settings -> INSTALLED_APPS 에 만든 애플리케이션 입력
  - 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야 함


3. 애플리케이션 구조
 (1) admin.py
  - 관리자용 페이지를 설정 하는 곳
 (2) apps.py
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않음
 (3) models.py
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
 (4) tests.py
  - 프로젝트의 테스트 코드를 작성하는 곳
 (5) views.py
  - view 함수들이 정의 되는 곳
  - MTV 패턴의 V에 해당

4. PROJECT & Applications
 (1) project
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음

 (2) Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
  - 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장
```

## 요청과 응답
```
1. Django의 세가지 구조
 (1) Model
 (2) View
 (3) Template

2. 데이터의 흐름
 URL -> VIEW -> TEMPLATE

3. 요청과 응답
 (1) URLs
  - form articles(앱 이름) import views
    
    urlpatterns = [
      path('articles/(주소창에 치는 것)', views.index),
    ]
  - 주소창에 articles를 치면 articles 앱에 views에 있는 index함수 실행

 (2) View
  - def index(request):
      context = {


      }
      return render(request, 'index.html', context) 

  - index 함수를 동작시킨 후 필요한 정보들을 context에 넣고 articles앱의 templates에 있는 index.html파일을 실행하는데 거기에 context를 같이 보낸다.

 (3) Templates
  - html 처럼 작성

 (4) render()
  - render(request, template_name, context)
   1) request
    - 응답을 생성하는데 사용되는 요청 객체
   2) template_name
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
   3) context
    - 템플릿에서 사용할 데이터
```

## 디자인 패턴
```
Django의 디자인 패턴은 MTV이다.

1. MTV
 (1) Model
  - 데이터와 관련된 로직을 관리
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
 (2) Template
  - 레이아웃과 화면을 처리
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
 (3) View
  - Model & Tempalte과 관련한 로직을 처리해서 응답을 반환
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
```

## DTL
```
HTML에 Python으로 처리한 여러가지 데이터를 넣기 위하여 사용

1. Variable {{variable}}
 - 변수명은 영어, 숫자와 밑줄의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
  - 공백이나 구두점 문자 또한 사용할 수 없음
 - dot(.)을 사용하여 변수 속성에 접근할 수 있음
 - render()의 세번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

2. Filters {{variable|filter}}
 - 표시할 변수를 수정할 떄 사용
 - ex) name의 변수를 모두 소문자로 출력 {{name|lower}}

3. Tags {% tag %}
 - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
 - 일부 태그는 시작과 종료 태그가 필요
  {% if 조건 %}{% endif %}

4. DTL 사용해보기 (variable)
 (1) URL
  - urlpatterns = [
    path('greeting/', views.greeting),
  ]

 (2) views
  - def greeting(request):
      return render(request, 'greeting.html', {'name':'Alice'})

 (3) templates
  - <body>
      <p>안녕하세요 저는 {{name}} 입니다.</p>
    </body>

 - 보낼 정보가 많을 때에는 context 딕셔너리로 묶어서 보냄

5. Dtl 사용 (Filter)
 (1) urls
   - urlpatterns = [
        path('dinner/', views.dinner),
   ]

 (2) views
   - def dinner(request):
      foods = ['A','B','C']
      pick = random.choice(foods)
      context = {
        'pick' : pick,
        'foods' ' foods,
      }

      return render(request, 'dinner.html', context)

 (3) Template
  - <body>
      <p>{{pick}}은 {{pick|length}}글자</p>
    </body>

```

## 템플릿 상속
```
템플릿 최상단에 기본틀이 되는 템플릿을 만들어 넣고 불러다가 사용
templates 폴더 만들기 -> base.html 만들기
base.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  <title>MJ PJT</title>
</head>
<body>
  
  {% block content %}
  {% endblock content %}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>

사용할 떄는 사용할 애플리케이션의 templates에서
{% extends 'base.html' %}

{% block content %}
  <h1>여기는 Articles App의 hello입니다.</h1>
  <h2>안녕? {{ name }}</h2>
{% endblock content %}

base.html을 사용할 떄는
프로젝트의 settings -> 'DIRS': [BASE_DIR/'templates'], 로 변경
```
## Variable routing
```
1. 필요성
 - 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들어야 할까?

2. Variable routing 이란?
 - URL 주소를 변수로 사용하는 것을 의미
 - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
 - 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

3. Variable routing 작성
 - 변수는 "<>"에 정의하며  view 함수의 인자로 할당됨
 - 기본 타입은 string이며 5가지 타입으로 명시할 수 있음

  (1) str <str:name> (2) int <int:cnt>

4. view 함수 작성
 - variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음

 def hello(request, name):
  context = {
    'name' : name,
  }
  return render(request, 'hello.html', context)

5. templates
 {% block content %}
  <h1>만나서 반가워요 {{name}}님!</h1>
 {% endblock content %}  

```

## App URL mapping
```
1. App URL mapping
 - 앱이 많아졌을 떄 urls.py를 각 app에 매핑하는 방법을 이해하기
 - 두 번째 app인 apges를 생성 및 등록해보자

2. App URL mapping 해보기

 (1) 프로젝트 URL
  - from django.contrib import admin
    from django.urls import path, include
    from articles import views

    urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('artilces.urls')),
      path('pages/', include('pages.urls')),
    ]

 (2) articles의 url
  - from django.urls import path
    from . import views

    urlpatterns = [
       path('index/', views.index),
       path('greeting/', views.greeting),
       path('dinner/', views.dinner),
    ]


 (3) pages의 url
  - from django.urls import path
    from . import views

    ulpatterns = [
        path('index/', views.index),
        path('hello/<str:name>/', views.hello),
    ]

3. include()
 - 다른 URLconf(app/urls.py)들을 참조할 수 있도록 돕는 함수
 - 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
```

## Form & Data
```
데이터를 보내고 가져오기
HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

1. HTML <form> element
 - 데이터가 전송되는 방법을 정의
 - 웹에서 사용자 정보를 입력하는 여러 방식(test, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
 - 데이터를 어디로 어떤 방식으로 보낼지
 - 핵심 속성
  - action 
  - method

2. action
 - 입력 데이터가 전송될 URL을 지정
 - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL 이어야 함
 - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

3. method 
 - 데이터를 어떻게 보낼 것인지 정의
 - 입력 데이터의 HTTP request methods를 지정
 - HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있는데 바로 GET 방식과 POST 방식

4. HTML <form> element 작성

 (1) urls
  - urlpatterns = [
    path('thorw/', views.throw),
  ]

 (2) views
  - def throw(request):
      return render(request, 'throw.html')

 (3) templates
  - {% extends 'base.html' %}

    {% block content %}
      <h1>Throw</h1>
      <form action="#" method="#">
      </form>
    {% endblock content %}

5. HTML <input> element
 - 사용자로부터 데이터를 입력 받기 위해 사용
 - type 속성에 따라 동작 방식이 달라진다.
  - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 mdn 문서에서 참고하여 사용핟로고 함
 - type을 지정하지 않은 경우 기본값은 text

 - 핵심 속성
  - name

6. HTML input's attribute
 - name
  - form을 통해 데이터를 제출 했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버느 ㄴname 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음.

  - 서버에 전달하는 파라미터로 매핑하는 것

7. HTML <input> element 작성
  {% extends 'base.html' %}

  {% block content %}
    <h1>Throw</h1>
    <form action="#" method="GET">
      <label for="message">보내고 싶은 데이터 적기</label>
      <input type="text" id="message" name="message">
      <input type="submit">
    </form>
  {% endblock content %}

  - 사용자가 주소/throw/에 들어가면 정보를 입력하는 칸이 나온다.

8. GET
 - 서버로부터 정보를 조회하는데 사용
  - 즉 서버에게 리소스를 요청하기 위해 사용
 - 데이터를 가져올 때만 사용해야 함
 - 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  - 데이터를 URL에 포함되어 서버로 보내짐

9. Query String Parameters
 - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
 - 이러한 문자열은 &로 연결된 key=value 쌍으로 구성되며 기본 URL과 물음표(?)로 구분됨
 - https://host:prot/path?key=value&key=value
 - Query String이라고도 함
 - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
 - "key=value"로 필요한 파라미터 값을 적음
  - "="로 key와 value가 구분됨
 - 파라미터가 여러 개일 경우 "&"를 붙여 여러 개의 파라미터를 넘길 수 있음
 - 그런데 아직 어디로 보내야(action) 할지 작성하지 않았다.

```

## Retrieving the data
```
- 데이터 가져오기
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름
- throw가 보낸 데이터를 catch에서 가져오기

1. catch 작성
 (1) urls
  - urlpatterns = [
    path('catch/', views.catch),
  ]

 (2) views
  - def catch(request):
      return render(request, 'catch.html')

 (3) template (catch)
  {% extends 'base.html' %}

  {% block content %}
    <h1>Catch</h1>
    <h2>보낸 데이터 : {{message}}</h2>
    <a href="{% url 'articles:throw' %}">다시 데이터 보내러가기</a>
  {% endblock content %}

  - throw의 url에서 데이터를 입력하면 catch에서 그 값을 받고 
     보낸 데이터 : ~~ 표시 
     다시 데이터 보내러가기 누르면 다시 throw url로 넘어가 다시 값을 입력할 수 있다.
 
  (4)
    {% extends 'base.html' %}

    {% block content %}
      <h1>Throw</h1>
      <form action="{% url 'articles:catch' %}" method="GET">
        <label for="message">보내고 싶은 데이터 적기</label>
        <input type="text" id="message" name="message">
        <input type="submit">
      </form>
    {% endblock content %}

2. Request and Response objects
 - 요청과 응답 객체 흐름
  (1) 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpsRequest object를 생성 
  (2) 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
  (3) 마지막으로 view 함수는 HttpResponse object를 반환
```

## Django Model
```
Mdeol(이하 모델)의 핵심 개념과 ORM을 통해 데이터베이스 조작 이해
Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층을 제공
```

## Database
```
1. 개념
 - 체계화된 데이터의 모임
 - 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화도니 데이터를 수집하는 저장 시스템

2. DB의 기본 구조
 - 스키마
 - 테이블

 (1) 스키마
  - 뼈대
  - 데이터베이스에서 자료의 구조,표현,방법,관계 등을 정의한 구조

 (2) 테이블
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - 관계라고도 부름

  1. 필드
   - 속성 , 컬럼
  2. 레코드
   - 튜플 , 행

  (3) 필드
   - 속성 혹은 컬럼
   - 각 필드에는 고유한 데이터 형식이 지정된
  
  (4) 레코드
   - 튜플 혹은 행
   - 테이블의 데이터는 레코드에 저장됨
  
  (5) PK
   - 기본 키
   - 각 레코드의 고유한 값
   - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값
   - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨
  
  (6) 쿼리
   - 데이터를 조회하기 위한 명렁어
   - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
   - Query를 날린다 = 데이터베이스를 조작한다.

```

## Model
```
- Django는 Model을 통해 데이터에 접근하고 조작
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑
 - 모델 클래스 1개 == 데이터베이스 테이블 1개

1. Model 작성하기 articles/models.py
 - 새 프로젝트(crud), 앱(articles) 작성 및 앱 등록
    class Article(models.Model): (1)
    title = models.CharField(max_length=20) (2)
    content = models.TextField() (3)

  
  (1) 각 모델은 django.models.Model 클래스의 서브 클래스
    - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
    - 클래스 상속 비나 형태의 Django 프레임워크 개발
     - 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것

  (2,3) models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
    - Article에는 어떤 데이터 구조가 필요한지 정의
    - 클래스 변수 title과 content는 DB 필드를 나타냄
    - title,content는 db필드의 이름
    - 뒤에 값 db 필드의 데이터 타입
```

## Migrations
```
- Django가 모델에 생긴 변화를 실제 DB에 반영하는 방법
- makemigrations
- migrate

1. makemigrations
 - 모델의 변경사항에 대한 새로운 migration을 만들 떄 사용
 - python manage.py makemigrations
 - 명령어 실행 후 migrations/0001_initial.py가 생성된 것을 확인
 - 파이썬으로 작성된 설계도

2. migrate
 - makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정
 - 결과적으로 모델에 변경사항과 데이터베이스를 동기화
 - python manage.py migrate
 - 설계도를 실제 db.sqlite3 DB 파일에 반영

3. 반드시 기억해야 할 migration 3단계
 (1) models.py에서 변경사항이 발생하면

 (2) migration 생성
  - makemigrations

 (3) DB 반영 (모델과 DB의 동기화)
  - migrate

4. 설계도는 누가 해석??
 - makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어있음
 - 그런데 SQL만 알아 들을 수 있다는 DB가 어떻게 이 설계도를 이해하고 동기화를 이룰 수 있을까?
 - 바로 이 과정에서 중간에 번역을 담당하는 것이 ORM
```

## ORM
```
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django<->DB)데이터를 변환하는 프로그래밍 기술
- 객체 지향 프로그래밍에서 데이터베이스를 연동할 떄, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용
- 한 마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

1. ORM 장단점
 - 장점
  - SQL을 잘 아지 못해도 객체지향 언어로 DB 조작이 가능
  - 객체 지향적 접근으로 인한 높은 생산성

 - 단점 
  - ORM 만으로 세밀한 데이터베이스 좆가을 구현하기 어려운 경우가 있음

2. ORM을 사용하는 이유
 - 생산성
 - Model 정리
  - 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
```

## QuerySet API
```
1. 사전 준비
 (1) vscode SQLite
  - vscode SQLite 확장프로그램을 통해 직접 테이블 데이터 확인하기
  - 좌측 하단 SQLITE EXPLOTER 확인
  - 테이블 선택 후 show table 버튼 클릭
 (2) 외부 라이브러리 설치 및 설정
  - 실습 편의를 위한 추가 라이브러리 설치 및 설정
  - pip install ipython
  - pip install dhango-extensions
  - settings.py -> INSTALLED_APPS에 django_extensions추가
  - pip freeze > requirments.txt

2. Django shell
 - ORM 관련 구문 연습을 위해 파이썬 쉘 환경 사용
 - django shell을 사용
 - python manage.py shell_plus
```

## QuerySet API
```
1. Database API
 - Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법
 - Model을 정의하면 데이터를 만들고 일고 수정하고 지울 수 있는 API를 제공

2. Database API 구문
 - Article.objects.all()

3. objects manager
 - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
 - Django는 기본적으로 모든 Django 모델 클래스에 대해 objects 라는 Manager 객체를 자동으로 추가
 - 이 Manager를 통해 특정 데이터를 조작할 수 있음
 - DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager
```

## QuerySet API 익히기



      