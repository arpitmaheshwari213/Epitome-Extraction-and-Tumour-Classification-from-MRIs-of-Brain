from django.conf.urls import url
from . import views
app_name='brain_cancer'

urlpatterns = [
    #/brain_tumour/
    url(r'^$',views.index,name='index'),
    url(r'^result/$',views.result,name='result'),
    url(r'^process/$',views.process,name='process')
]