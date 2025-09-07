
from django.urls import path,include
from . import views
urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet_list'),
    path('',views.snippet_list,name='home'),
    path('snippet/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('snippet/<int:pk>/', views.snippet_detail, name='snippet_detail'),
    path('snippet/<int:pk>/edit/', views.snippet_update, name='snippet_update'),
    path('snippet/<int:pk>/delete/', views.snippet_delete, name='snippet_delete'),
    path('snippet/new/', views.snippet_create, name='snippet_create'),  # 👈 add this

    # path('add/',views.addsnippet,name='add'),
]