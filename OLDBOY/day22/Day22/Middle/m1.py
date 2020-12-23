__author__ = '秋轩'
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('广东')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('浙江')

    def process_response(self,request,response):
        print('广西')
        return  response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('江西')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('重庆')

    def process_response(self,request,response):
        print('福建')
        return response

    #views 中出现异常，则会返回这里的值
    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            return HttpResponse('出现异常》。。')

    def process_template_response(self, request, response):
        # 如果Views中的函数返回的对象中，具有render方法
        print('-----------------------')
        return response