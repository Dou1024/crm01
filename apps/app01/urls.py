from apps.app01 import views
from apps.app01.views import views
from django.urls import path

urlpatterns = [
    path('son/', views.son, name="son"),    # 主路由分发来的
]

app_name = "app01"