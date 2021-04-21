from django.urls import path, include

from .views import logout_view, login_view, signup, Login

urlpatterns = [
    # path('login/', Login.as_view(), name='login'),
    # path('signup/', SignUp.as_view(), name='signup'),
    # path('logout/', logout_view, name='logout'),
    # path('gher/', gher_umdan, name='gher-umadan'),

    path('login/', login_view, name='login'),
    path('login_class/', Login.as_view(), name='login-class'),
    path('signup/',signup, name='signup'),
    path('logout/', logout_view, name='logout'),
]