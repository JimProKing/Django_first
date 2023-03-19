# basic Auth Handle.
def authHander(url="http://127.0.0.1:8000/"):
    from urllib.request import HTTPBasicAuthHandler,build_opener

    auth_handler = HTTPBasicAuthHandler()
    auth_handler.add_password(realm='ksh',user='shkim',passwd='shkimadmin',
    url=url + "auth/")
    opener = build_opener(auth_handler)
    resp = opener.open(url + "auth/")

print(authHander)