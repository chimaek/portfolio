from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.results, name='results'),
    path('<int:question_id>/detail/', views.detail, name="detail"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]
