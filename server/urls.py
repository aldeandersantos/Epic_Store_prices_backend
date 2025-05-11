from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('epic_store.urls')),
    # Serve o frontend como página principal usando o template home.html
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# Serve arquivos estáticos do frontend
urlpatterns += static(
    settings.STATIC_URL,
    document_root=os.path.join(settings.BASE_DIR, 'frontend')
)
