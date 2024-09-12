from django.contrib import admin
from django.urls import include, path
from products.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('api/', include('products.urls'), name='products'),
]
