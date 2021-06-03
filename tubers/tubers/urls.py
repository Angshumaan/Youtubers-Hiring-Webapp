"""tubers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # We have included an new app webpages now go ahead and check on urls of webpages
    path('', include('webpages.urls')),
    path('youtubers/', include('youtubers.urls')),  # new second app
    path('accounts/', include('accounts.urls')),  # new Third app
    path('hiretubers/', include('hiretubers.urls')),  # new fourth app
    path('contacttubers/', include('contacttubers.urls')),  # fifth app assignment
    path('information/', include('information.urls')),  # sixth app assignment
    path('socialaccounts/', include('allauth.urls')),  # from django all auth

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # We are connecting media root and media url patterns so that we can access our image through the url. So after adding this whenever you hit http://localhost:3000/media/example.jpg  It will show example.jpg which will be present in your Project dir/media/
