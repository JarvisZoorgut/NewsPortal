from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, ArticleCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostList.as_view(), name='posts_list'),
   path('<int:pk>', PostDetail.as_view(), name='posts_detail'),
   path('search/', PostSearch.as_view(), name='posts_search'),
   path('create/', NewsCreate.as_view(), name='posts_create'),
   path('article/create/', ArticleCreate.as_view(), name='posts_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='posts_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='posts_delete'),
]