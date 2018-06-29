from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^add$', views.addTodo,name='add'),
    #Passing an id to the view
    url(r'^complete/(?P<todo_id>\d+)$', views.completeTodo,name='complete'),
    url(r'^deleteCompleted$', views.deleteCompletedTodo,name='deleteCompleted'),
    url(r'^deleteAll$', views.deleteAllTodo,name='deleteAll'),
]
