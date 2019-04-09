from django.urls import path
from .views import PagesListView, PageDetailView,PagesCreate

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/',PagesCreate.as_view(),name='create'),
], 'pages') #ahora se las debe referenciar en los html  pages:subpagina