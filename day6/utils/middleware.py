from django.utils.deprecation import MiddlewareMixin#有些版本需要导入


class Test1Middleware(MiddlewareMixin):
    def process_request(self,request):
        print('process_request')

        return None

    def process_response(self,request,response):
        print('response')
        return response


class Test2Middleware(MiddlewareMixin):
    def process_request(self,request):
        print('process_request2')

        return None

    def process_response(self,request,response):
        print('response2')
        return response