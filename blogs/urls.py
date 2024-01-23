from django.urls import path
from .views import post_list,post_detail,post_new,post_edit,post_draft,post_publish,post_remove,add_comment_to_post,comment_approve,comment_remove
urlpatterns = [
    path('',post_list,name='post_list'),
    path('post/<int:pk>/',post_detail,name='post_detail'),
    path('post/new/',post_new,name='post_new'),
    path('post/edit/<int:pk>/',post_edit,name='post_edit'),
    path('draft/',post_draft,name='post_draft_list'),
    path('post/publish/<int:pk>',post_publish,name='post_publish'),
    path('post/remove/<int:pk>',post_remove,name='post_remove'),
    path('post/comment/<int:pk>', add_comment_to_post, name='add_comment_to_post'),

    path('comment/approve/<int:pk>', comment_approve, name='comment_approve'),
    path('comment/remove/<int:pk>', comment_remove, name='comment_remove'),
]
