def cookieProcessor(url = "http://127.0.0.1:8000/"):
    from urllib.request import Request,HTTPCookieProcessor,build_opener

    url = url + "cookie/"
    # create cookie handler
    cookie_handler = HTTPCookieProcessor()
    opener = build_opener(cookie_handler)