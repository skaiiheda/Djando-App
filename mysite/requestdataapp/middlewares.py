from datetime import datetime, timedelta

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest


def set_useragent_on_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        print('Before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('After get response')
        return response
    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("requests_count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses_count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exceptions so far')


# class ThrottlingMiddleware:
#     """
#     Middleware to limit the processing of user requests if he makes requests too often
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.time_responses = []
#         self.ips = {}
#
#     def __call__(self, request: HttpRequest):
#         ip_address = request.META.get('REMOTE_ADDR')
#         print(self.ips)
#         print(ip_address)
#         if ip_address:
#             current_time = datetime.now()
#             if ip_address in self.ips:
#                 past_time = self.ips[ip_address]
#                 if current_time < past_time + timedelta(seconds=1):
#                     return HttpResponseBadRequest('Too many requests', status=429)
#             else:
#                 self.ips[ip_address] = current_time
#         response = self.get_response(request)
#         return response
