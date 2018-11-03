from django.conf.urls import url
from app import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cul', views.Cul)

urlpatterns = [
url(r'^index/', views.index,name='index'),
url(r'^share/', views.share,name='share'),
url(r'^list/', views.list,name='list'),
url(r'^about/', views.about,name='about'),
url(r'^gbook/', views.gbook,name='gbook'),
url(r'^info/', views.info,name='info'),
url(r'^infopic/', views.infopic,name='infopic'),
url(r'^login/', views.login, name='login'),
url(r'^backindex/', views.backindex,name='backindex'),
url(r'^back_article/', views.back_article, name='back_article'),
url(r'^back_category/', views.back_category, name='back_category'),
url(r'^back_notice/', views.back_notice, name='back_notice'),
url(r'^back_comment/', views.back_comment, name='back_comment'),
url(r'^back_article/', views.back_article, name='back_article'),
url(r'^add_article/', views.add_article,name='add_article'),
url(r'^update_article/', views.update_article,name='update_article'),
url(r'^add_notice/', views.add_notice, name='add_notice'),
]

urlpatterns += router.urls