from django.urls import path
from shop import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about',views.about,name="About-Us"),
    path('tracker',views.tracker,name="TrackingStaus"),
    path('login',views.login,name="Login"),
    path('contact',views.contact,name="Contact"),
    path('search',views.search,name="Search"),
    path('productView',views.prodView,name="ProductView"),
    path('checkout',views.checkout,name="Checkout")
]
