"""
URL configuration for blenicruise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect  # ✅ Import redirect function

def redirect_to_restaurant(request):
    return redirect('restaurant_app:home')  # ✅ Redirect to restaurant homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ Redirect '/' to 'restaurant/' homepage
    path('', redirect_to_restaurant, name='homepage_redirect'),

    path('restaurant/', include('restaurant_app.urls', namespace='restaurant_app')),
    path('logs/', include('logs_app.urls', namespace='logs_app')),
]

# ✅ Serve media files correctly
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

