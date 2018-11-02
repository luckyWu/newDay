import time
import logging
from django.utils.deprecation import MiddlewareMixin#有些版本需要导入


class LoggingMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 记录当前请求访问服务器的时间
        request.init_time = time.time()
        request.init_body = request.body

        return None

    def process_response(self,request,response):
        # 记录返回响应的时间和访问服务器的时间差
        try:
            times = time.time() - request.init_time
            code = response.status_code
            req_body = response.content
            res_body = request.init_body
            msg = '%s %s %s %s' % (time, code, res_body, req_body)
            logging.info(msg)
        except Exception as e:
            logging.critical('logs error,Exception: %s' % e)
        return response


class Test2Middleware(MiddlewareMixin):
    def process_request(self,request):
        print('process_request2')

        return None

    def process_response(self,request,response):
        print('response2')
        return response