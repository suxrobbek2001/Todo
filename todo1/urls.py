
from django.contrib import admin
from django.urls import path
from todo_app.views import todo,todo1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo),
    path('<int:son>', todo1,name='todo1'),
]
