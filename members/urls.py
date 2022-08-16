from django.urls import path
from.import views
app_name='members'

urlpatterns=[
    path('',views.index,name='index'),
    path('postlist/',views.PostListView.as_view(),name='postlist'),
    path('postdetail/<slug:post>/<int:pk>',views.postdetail,name='post_detail'),
    path('accountform/',views.UserAccount, name='account_form')
]