## 📖 목차
- [📖 목차](#-목차)
- [🔥 스파르타 마켓](#-스파르타-마켓)
- [✨ 주요기능](#-주요기능)
- [📚️ 기술스택](#️-기술스택)
- [ERD](#erd)
- [프로젝트 파일 구조](#프로젝트-파일-구조)
- [Trouble Shooting](#trouble-shooting)
  - [로그인 에러](#로그인-에러)
    
## 🔥 스파르타 마켓
챕터 4
Django를 활용한 중고거래 웹사이트 제작

## ✨ 주요기능

- 🧑‍💻 **회원 기능**
  - 회원가입
  - 로그인
  - 로그아웃
  - 프로필 사진 기능
    - 기본 프로필
    - 프로필 등록
    - 프로필 수정

- 📋 **게시 기능**
  - 기본적인 상품 **CRUD** 기능
  - 개별 상품 상세 정보 기능
  - 물건 찜수 / 조회수

- 🔖 **해시태그 기능**
  - 띄어쓰기, 특수문자 허용 X
  - 고유성

## 📚️ 기술스택
<div align=center>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=greene">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white">
<br>
<img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">


</div>


## ERD
![](/image/CH4_ERD.png)

## 프로젝트 파일 구조


```
spartamarket
├── accounts/ : 계정 앱
├── products/ : 상품 앱
├── spartamarket/ : 프로젝트 앱
│
├── media/ : 동적 자원
├── static/ : 정적 자원
│
├── templates/ : 기본 템플릿
├── requirements.txt : 패키지 목록 파일
└── manage.py : 프로젝트 관리 수행 파일
```
## Trouble Shooting

### 로그인 에러
```
TypeError at /accounts/login/
login() takes 1 positional argument but 2 were given
```
![](/image/241226_type_error.png)

accounts 앱의 `views.py` 가 아래 코드처럼 작성되어있었는데,

**내가 임포트한 login** 과 **views 에서 작성한 login 함수가 이름이 같아서** 발생한 에러였다.

```py
from django.contrib.auth import login

@require_http_methods(["GET","POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("products:product_list")
    else:
        form = AuthenticationForm()
    
    context = {
        "form":form
    }
    return render(request, 'accounts/login.html', context)
```


`views.py` 의 login 함수 이름을 변경하거나 (`urls.py` 에서도 변경 필요),

**`views.py` 에서 임포트한 login 함수를 다른 이름으로 변경**하면 된다.

나는 두 번째 방법으로 해결해서 수정한 코드는 아래와 같다.

```py
@require_http_methods(["GET","POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("products:product_list")
    else:
        form = AuthenticationForm()
    
    context = {
        "form":form
    }
    return render(request, 'accounts/login.html', context)
```