from django.shortcuts import render
from .models import Quiz
from category.models import Category
from quiz_taken.models import Quiz_Taken
from django.http import JsonResponse
from questions.models import Question, Answer
from result.models import Result


# class QuizListView(ListView):
#     model = Quiz
#     template_name = "main.html"
def QuizList(request, category_slug=None):
    object_list = Quiz.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        object_list = Quiz.objects.filter(category=category)

    category = Category.objects.all()
    return render(
        request, "main.html", {"object_list": object_list, "category": category}
    )


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
        data_.pop("csrfmiddlewaretoken")
        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        exam_name = Quiz.objects.get(pk=pk).topic

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

        if Result.objects.filter(user=user, exam_name=exam_name).exists():
            print("Exist")

        else:
            quiz_name = Quiz.objects.get(pk=pk)
            Quiz_Taken.objects.create(user=user, quiz_name=quiz_name, score=score)

        total_quizes = Quiz.objects.all().count()
        completed_quizes = Quiz_Taken.objects.filter(user=request.user).count()
        percent_of_attempts = (completed_quizes / total_quizes) * 100
        Result.objects.create(
            quiz=quiz,
            user=user,
            score=score_,
            exam_name=exam_name,
            total_questions=total_questions,
            percent=percent_,
            fullMarks=fullMarks,
            total_quizes=total_quizes,
            completed_quizes=completed_quizes,
            percent_of_attempts=percent_of_attempts,
        )
        if percent_ > quiz.required_to_pass:
            return JsonResponse({"passed": True, "score": score_, "result": result})

        else:
            return JsonResponse({"passed": False, "score": score_, "result": result})
