def app(environ, start_response):
     start_response('200 OK', [('Content-Type','text/plain')])
     qs = environ['QUERY_STRING']
     qs = qs.replace('&','\n\r')
     return [qs]

