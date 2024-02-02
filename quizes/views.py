from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView  # Create your views here.
from django.http import JsonResponse
from questions.models import Question, Answer
from result.models import Result


class QuizListView(ListView):
    model = Quiz
    template_name = "main.html"


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, "quiz.html", {"obj": quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse(
        {
            "data": questions,
            "time": quiz.time,
        }
    )


def save_quiz_view(request, pk):
    print("request.POST: ", request.POST)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        print("Data", data)
        data_.pop("csrfmiddlewaretoken")
        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        exam_name = Quiz.objects.get(pk=pk).topic
        print("Exam Name : ", exam_name)

        result = []
        correct_answer = None
        correct = 0
        wrong = 0
        notAnswered = 0
        score = 0
        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answer = Answer.objects.filter(question=q)
                for a in question_answer:
                    if a_selected == a.text:
                        if a.correct:
                            correct += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            wrong += 1
                            correct_answer = a.text
                result.append(
                    {str(q): {"correct_answer": correct_answer, "answered": a_selected}}
                )
            else:
                notAnswered += 1
                result.append({str(q): "not answered"})
        total_questions = quiz.number_of_Questions
        per_right_ans = quiz.marks_per_right_answer
        per_wrong_ans = quiz.deduct_marks_per_wrong_answer
        fullMarks = total_questions * per_right_ans
        add = correct * per_right_ans
        deduct = wrong * per_wrong_ans
        score = add - deduct
        score_ = score
        percent = (score / fullMarks) * 100
        percent_ = percent
        fullMarks = fullMarks
        Result.objects.create(
            quiz=quiz,
            user=user,
            score=score_,
            exam_name=exam_name,
            total_questions=total_questions,
            percent=percent_,
            fullMarks=fullMarks,
        )
        print(correct)

        if percent_ > quiz.required_to_pass:
            return JsonResponse({"passed": True, "score": score_, "result": result})

        else:
            return JsonResponse({"passed": False, "score": score_, "result": result})
