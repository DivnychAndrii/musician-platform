from rest_framework.pagination import PageNumberPagination


class ResultSetPagination(PageNumberPagination):
    page_size = 15
    max_page_size = 50
    page_size_query_param = 'page_size'
