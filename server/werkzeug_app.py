# !/usr/bin/env  python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('i love you sana my love sharoh')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5700,
        application=application
    )
