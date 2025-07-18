from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    #page_size = 4
    page_query_param = "p" #page
    page_size_query_param = "size"
    max_page_size = 5
    last_page_string = "end"

class ProductLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7
    limit_query_param = "records" #cuantos quiero que aparezcan por pagina
    offset_query_param = "start" #numero de pagina

class ProductCPagination(CursorPagination):
    page_size = 4