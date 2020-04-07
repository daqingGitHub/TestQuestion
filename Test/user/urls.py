from django.conf.urls import url, include

from user import views

urlpatterns = [
    url(r'^user/',views.uploadData),
    url(r'^query/',views.query)

]