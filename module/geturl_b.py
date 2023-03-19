# Django 실행중일때, 실행중인 서버 데이터 가져오는거
## default : http://127.0.0.1:8000/
def geturl_b(url="http://127.0.0.1:8000/"):
    ## Django 로컬 링크 url 열기
    from urllib.request import urlopen
    data = "language=python&framework=django"
    f = urlopen(url,bytes(data,encoding='utf-8'))
    return(f.read().decode('utf-8'))