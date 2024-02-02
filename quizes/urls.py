from django.urls import path
from .views import quiz_view, QuizListView, quiz_data_view, save_quiz_view

urlpatterns = [
    path("", QuizListView.as_view(), name="quiz"),
    path("<pk>/", quiz_view, name="quizes"),
    path("<pk>/save/", save_quiz_view, name="save-view"),
    path("<pk>/data/", quiz_data_view, name="quiz_data_view"),
]
