# Django 시작


## Django install
> pip install django

## Django project 생성
> django-admin startproject web_study 




# 기본 개념(용어) 정리
## 1. 정적 페이지 vs 동적 페이지
- 정적 페이지 : 클라이언트 상관없이 항상 동일 내용 표시.
  - js + CSS로 이루어진 페이지

- 동적 페이지 : 클라이언트에 의해 화면이 바뀌는 페이지.

## 2. CGI 규격 (Common GateWay Interface)
- 프로그램과 웹 서버 사이 정보 주고받는 규칙.
    - 어떤 언어로도 프로그램 개발 가능.
      - [클라이언트 --상호작용-- 서버] --> 프로그램.
    - 단점 : 프로세스 많아지면 메모리 요구량 많아짐.
      - 그래서 여러 대안기술 생김.
      - 


# 자주 쓰이는 패키지
## 1. urllib
- 웹 작성시 자주 사용되는 모듈들 들어있음.
  - 고수준 API제공.
- urllib.parse 모듈
