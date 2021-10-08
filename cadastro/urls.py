from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('funcionario/', include('funcionario.urls', namespace='funcionario')),
    path('', include('core.urls', namespace='core')),

]
