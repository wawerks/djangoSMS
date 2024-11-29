from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('submit-score/', views.score_view, name='submit_score'),
    path('score/', views.score_view, name='score_view'),
    path('success/', views.success_view, name='success_view'),  # Success page
    path('logout/', LogoutView.as_view(), name='logout'),
]

