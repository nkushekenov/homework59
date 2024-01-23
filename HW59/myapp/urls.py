from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import task_list, task_detail, task_create, task_edit, task_delete, task_toggle, RegView, HomePageView, LoginView


urlpatterns = [
    path('', HomePageView.as_view(template_name='base.html'), name='homepage'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasklist/', task_list, name='task_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegView.as_view(), name='register'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/<int:pk>/toggle/', task_toggle, name='task_toggle'),
]