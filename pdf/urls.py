from django.urls import path
from pdf.views.home_view import HomeView
from pdf.views.merge_view import MergeView
from pdf.views.split_view import SplitView
from pdf.views.lock_view import LockView
from pdf.views.unlock_view import UnlockView
from pdf.views.compress import CompressView

app_name = 'pdf'
urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('merge/', MergeView.as_view(), name='merge'),
    path('split/', SplitView.as_view(), name='split'),
    path('lock/', LockView.as_view(), name='lock'),
    path('unlock/', UnlockView.as_view(), name='unlock'),
    path('compress/', CompressView.as_view(), name='compress'),
]
