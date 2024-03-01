from django.urls import path
from .views import (
    quiz_view,
    QuizList,
    quiz_data_view,
    save_quiz_view,
    leaderboard,
    reviewRating,
)

urlpatterns = [
    path("", QuizList, name="quiz"),
    path("category/<slug:category_slug>/", QuizList, name="cat_wise_post"),
    path("<pk>/", quiz_view, name="quizes"),
    path("<pk>/save/", save_quiz_view, name="save-view"),
    path("<pk>/data/", quiz_data_view, name="quiz_data_view"),
    path("reviewRating/<pk>/", reviewRating, name="reviewRating"),
    path("leadrrboard/<pk>/", leaderboard, name="lead_view"),
]
