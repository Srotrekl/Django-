
from django.contrib import admin
from django.urls import path

import base.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', base.views.hello),
    path('search/', base.views.search, name="search"),
    path('room/<pk>', base.views.room, name='room'),
    path('', base.views.RoomsView.as_view(), name='rooms',),
    path('room_create/', base.views.room_create, name='room_create', )
]
