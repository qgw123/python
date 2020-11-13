__author__ = 'qgw'

from wsgiref.simple_server import make_server

from Controller import controller

# def haddle_index():
#     f = open('web/View/index.html' , 'rb')
#     data = f.read()
#     f.close()
#     return [data,]
#     # return ['<h1> Hello Index! </h1>'.encode('utf-8'), ]
#
# def haddle_data():
#     return ['<h1> Hello Data! </h1>'.encode('utf-8'), ]

Url_list = {
    '/index': controller.haddle_index,
    '/data': controller.haddle_data,
}

def RunServer(environ,start_response):
    start_response('200 OK' , [('Content-Type', 'text/html')])
    cuttent_url = environ['PATH_INFO']

    func = None
    if cuttent_url in Url_list:
        func =  Url_list[cuttent_url]

    if func:
        return func()
    else:
        return ['<h1> 404 </h1>'.encode('utf-8'), ]
    # if cuttent_url == '/index':
    #     return haddle_index()
    # elif cuttent_url == '/data':
    #     return haddle_data()
    # else:
    #     return ['<h1> 404 </h1>'.encode('utf-8'), ]




if __name__ == '__main__':
    httpd = make_server('', 8000 , RunServer)
    print('Service HTTP on port 8000... ')
    httpd.serve_forever()