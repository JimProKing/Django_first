# url의 데이터 가져오는 코드
def geturl_a(url):
    from urllib.request import urlopen
    f = urlopen(url)
    return(f.read().decode('utf-8'))