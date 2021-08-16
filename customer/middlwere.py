# from django.http import HttpResponse
# from datetime import datetime
#
#
# from customer.models import *
#
#
# class AddressMiddleware:
#     def __init__(self, get_response_func) -> None:
#         self.get_response = get_response_func
#
#     def __call__(self, request):
#
#         if request:
#             start = datetime.now()
#             response = self.get_response(request)
#             end = datetime.now()
#             result = end - start
#             loging.warning(f'log in : {result}')
#             return response