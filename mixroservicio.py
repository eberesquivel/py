
import json
from wsgiref.simple_server import make_server
from cgi import parse_qs

html = """
<html>
<body>
  <h1> Hola %(nombre)s </h1>
</body>
</html>
"""

def application(environ,start_response):

    valores = parse_qs(environ['QUERY_STRING'])
    nombre = valores.get('nombre', 'El nombre no existe')
    nombre = nombre [0]
    headers = [('Content-type', 'text/html')]
    response = html % {'nombre' : nombre }
    start_response('200 OK',headers )
    return[bytes(response)]

servidor = make_server('localhost',8000,application)
servidor.handle_request()