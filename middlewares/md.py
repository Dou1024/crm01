"""
    这是中间件的类
    需要去 setting 里进行注册
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MyMd1(MiddlewareMixin):

    # def __init__(self, get_response):
    #     self.get_response = get_response
    #
    # def __call__(self, request):
    #     # 进
    #     if hasattr(self, "process_request"):
    #         self.process_request(request)
    #
    #     response = self.get_response(request)
    #
    #     # 出
    #     if hasattr(self, "process_response"):
    #         self.process_response(request, response)
    #     return response

    # 请求，视图函数执行前执行的操作
    def process_request(self, request):
        print("md1  come")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request, view_func)

    # 返回，视图函数执行后执行的操作，必须要 return 一下，否则报错
    def process_response(self, request, response):
        print("md1  go")
        return response

    def process_exception(self, request, exception):
        print("process_exception throw a exception\n", exception)
        return HttpResponse(exception)

    def process_template_response(self, request, response):
        # 视图函数返回`TemplateResponse`对象  or  对象中含有.render方法
        pass

class MyMd2(MiddlewareMixin):
    # 请求，视图函数执行前执行的操作
    def process_request(self, request):
        print("md2  come")
        # process_request 如果有response 则直接跳过下一个类原地掉头
        # return HttpResponse("这是md2，终止！")

    # 返回，视图函数执行后执行的操作
    def process_response(self, request, response):
        print("md2  go")
        return response


class MyMd3(MiddlewareMixin):
    # 请求，视图函数执行前执行的操作
    def process_request(self, request):
        print("md3  come")

    # 返回，视图函数执行后执行的操作
    def process_response(self, request, response):
        print("md3  go")
        return response
