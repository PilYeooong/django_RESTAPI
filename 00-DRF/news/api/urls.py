from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view
from news.api.views import ArticleListCreateAPIView, ArticleDetailAPIView
from news.api.views import JournalistListCreateAPIView
from news.api.views import JobOfferListCreateAPIView
from news.api.views import JobOfferDetailAPIView

urlpatterns = [
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article-detail")
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list"),
    path("joboffers/", JobOfferListCreateAPIView.as_view(), name="joboffer-list"),
    path("joboffers/<int:pk>", JobOfferDetailAPIView.as_view(), name="joboffer-detail"),
]