from django.shortcuts import render
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        Question.objects.create(
            title = request.POST.get('title'),
            issue_a = request.POST.get('issue_a'),
            issue_b = request.POST.get('issue_b'),
            image_a = request.POST.get('image_a'),
            image_b = request.POST.get('image_b'),
        )
        return redirect('eithers:index')

    else:
        return render(request, 'eithers/create.html')