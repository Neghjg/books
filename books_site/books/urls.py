from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('adventures/', adventures, name= 'adventures'),
    path('detective/', detective, name= 'detective'),
    path('fantasy/', fantasy, name= 'fantasy'),
    path('classical_prose/', classical_prose, name= 'classical_prose'),
    path('modern_prose/', modern_prose, name= 'modern_prose'),
    path('search/', search, name='search'),
    path('book/<slug:post_slug>/', book, name='book'),
    path('author/<slug:post_slug>/', author, name='author'),
    
]