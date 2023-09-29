from apps.app01 import views
from apps.app02.views import views
from django.urls import path

urlpatterns = [
    path('son2/', views.son2, name="son2"),    # 主路由分发来的
]

app_name = "app02"