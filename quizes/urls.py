from django.urls import path
from .views import quiz_view, QuizList, quiz_data_view, save_quiz_view, rating

urlpatterns = [
    path("", QuizList, name="quiz"),
    path("category/<slug:category_slug>/", QuizList, name="cat_wise_post"),
    path("<pk>/", quiz_view, name="quizes"),
    path("<pk>/save/", save_quiz_view, name="save-view"),
    path("<pk>/data/", quiz_data_view, name="quiz_data_view"),
    path("rating/<pk>/", rating, name="rating_view"),
]
