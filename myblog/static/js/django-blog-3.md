---
title: Django로 블로그 제작하기(2) - 정적파일 사용하기, 템플릿 확장하기, 글읽기
date: 2016-12-27 23:31:11
categories:
- web
- django
tags:
- python
- django
---
# 1. 정적 파일 사용하기
``myblog``에 ``static`` 폴더를 만들고 그 안에 js폴더를 만듭니다.
jQuery홈페이지에서 jquery를 받습니다.
``내려받은 jquery-3.1.1.min.js``를 ``myblog\static\js`` 폴더에 넣습니다. 그 후 ``myblog\static\js\``에 a.j파일을 생성하고 다음과 같이 작성합니다.
```javascript
$(function(){
	alert("jQuery 적용 됨");
});
```
postList.html파일을 열고 다음과 같이 스크립트 파일을 포함시킵니다.
```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
		<script src="{% static 'js/jquery-3.1.1.min.js' %}  "></script>
		<script src= "{% static 'js/a.js' %}  "></script>
	</head>
	<!-- 이하생략-->
	</body>
</html>
```
{% asset_img jquery.PNG %}
jQuery가 적용되었음을 알 수 있습니다. css나 image파일도 같은 방식으로 사용할 수 있습니다.

# 2. 템플릿 확장하기
장고는 템플릿 확장 기능을 제공합니다. 웹사이트 안의 서로 다른 페이지에서 HTML의 일부를 동일하게 재사용 할 수 있다는 뜻입니다.
``myblog\templates\blog``에 `postlayout.html`파일을 만들고 다음과 같이 작성합니다.
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
	</head>
	<body>
		{% block content %}
		{% endblock %}
	</body>
</html>
```
``postList.html`` 파일 맨 윗줄에 ``{% extends 'blog/postlayout.html' %}``을 추가하고 다음과 같이 작성합니다.
```html
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.content|linebreaks }}</p>
        </div>
    {% endfor %}
{% endblock content %}
```
# 3. 게시글 읽기
### 3-1 urls.py
``myblog\urls.py``에 ``url(r'^readpost/(?P<id>\d+)/$',views.readPost, name='readPost'),``을 추가합니다.
+ url에서 ``(?P<id>\d+)``는  \d+에 해당하는 표현을 id라는 파라미터에 넣어 뷰로 전송하라는 뜻입니다.

### 3-2 views.py
``views.py`` 맨 윗부분에 ``from django.shortcuts import render, get_object_or_404, redirect``를 추가하고 다음과 같이 뷰 함수를 추가합니다.
```python
def readPost(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/readpost.html', {'post': post})
```

``post = get_object_or_404(Post, id=id)``는 변수 id를 이용하여 해당 게시글을 불러옵니다.

### 3-3 템플릿 작성
``myblog\templates\blog``에 ``readPost.html``이란 파일을 만들고 다음과 같이 작성합니다.
```html
{% extends 'blog/postlayout.html' %}
{% block content 3}
				<h1>제목 : {{ post.title }}</h1>
				<p>{{ post.content|linebreaks }}</p>
{% endblock content %}
```

### 3-4 postList.html에 링크 만들기

postList.html을 열고 ``<h1><a href="">``부분을 다음과 같이 바꿉니다.
``<h1><a href="{% url 'readPost' id=post.id %}"></a></h1>``
postList.html의 a 태그를 통해 readPost를 들어가면 다음과 같은 화면이 나올 것입니다.
{% asset_img readPost.PNG %}
