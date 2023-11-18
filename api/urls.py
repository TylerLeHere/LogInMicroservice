from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, HistoryView, UserHistory, UserDetail

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('history/', HistoryView.as_view()),
    path('user-history/<int:pk>/', UserHistory.as_view()),

]