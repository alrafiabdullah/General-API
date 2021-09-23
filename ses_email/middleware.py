from django.utils.deprecation import MiddlewareMixin


class XForwardedForMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     return self.get_response(request)

    def process_request(self, request):
        if "HTTP_X_FORWARDED_FOR" in request.META:
            request.META["REMOTE_ADDR"] = request.META["HTTP_X_FORWARDED_FOR"]
