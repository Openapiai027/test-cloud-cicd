import functions_framework
import http


@functions_framework.http
def test_func(request):
    request_json = request.get_json()
    return {"response": "Hello test_func"}, http.HTTPStatus.OK
