from blog.urls import path
from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("about/", views.about, name ='about'),
  path("contact/", views.contact, name ='contact'),
  path("postspage/", views.postspage, name ='postspage'),
  path('postspage/post/<int:pk>/', views.post_detail, name='post_detail'),
]