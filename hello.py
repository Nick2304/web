def app(environ, start_response):
        start_response('200 OK', [('Content-Type','text/plain')])
        qs = qs.replace('&','\n')
        return qs

