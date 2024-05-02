from django.contrib import admin
from django.urls import include, path

# Import the settings from Django to check if DEBUG is True
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),  # Assuming 'webapp' is your app's name
]

# Include Debug Toolbar URLs only if DEBUG is True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
