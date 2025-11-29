from django.urls import path
from pdf.views.home_view import HomeView
from pdf.views.merge_view import MergeView
from pdf.views.split_view import SplitView
from pdf.views.lock_view import LockView
from pdf.views.unlock_view import UnlockView
from pdf.views.compress import CompressView
from pdf.views.pdf_to_word_view import PdfToWord
from pdf.views.convert_to_powerpoint_view import PdfToPowerpoint

app_name = 'pdf'
urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('merge/', MergeView.as_view(), name='merge'),
    path('split/', SplitView.as_view(), name='split'),
    path('lock/', LockView.as_view(), name='lock'),
    path('unlock/', UnlockView.as_view(), name='unlock'),
    path('compress/', CompressView.as_view(), name='compress'),
    path('convert/', PdfToWord.as_view(), name='convert-to-word'),
    path('convert-to-powerpoint/', PdfToPowerpoint.as_view(), name='convert-to-powerpoint'),
]
