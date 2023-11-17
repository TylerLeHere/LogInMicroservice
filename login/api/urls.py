from django.urls import path
#from .views import UserView, UserDetail, HistoryView, UserHistory
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),


    # path('users/', UserView.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),
    # path('history/', HistoryView.as_view()),
    # path('user-history/<int:pk>/', UserHistory.as_view()),

]