from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path("", views.index),
    path("create_event/", views.create_event)
    ]

# product_patterns = [
#     path("", views.products),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]
#
#
# urlpatterns = [
#     re_path(r'^about/contact/', views.contact),
#     re_path(r'^about', views.about, kwargs={"name":"Tom", "age": 38}),
#     # re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
#     # re_path(r"^user/(?P<name>\D+)", views.user),
#     # re_path(r"^user", views.user),
#     path("products/<int:id>/", include(product_patterns)),
#     path('userss/', views.userss),
#     path('', views.index),
# ]

