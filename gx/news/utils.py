from rest_framework.response import Response


def cross_domain_helper(response):
    """
    跨域辅助
    """
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def CORSResponse(data, **kwargs):
    """
    跨域辅助
    """
    return cross_domain_helper(Response(data, **kwargs))