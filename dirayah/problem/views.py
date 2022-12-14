import json
import sys
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SubmitCodeForm, CommentForm
from home.models import Problem, Comment, UserProfile


# show the problem page
def problem(request, problem_id):
    if request.user.is_authenticated:
        form = SubmitCodeForm()
        comment = CommentForm()
        problem = Problem.objects.get(id=problem_id)
        return render(request, 'problem/problem.html', { 'problem': problem, 'form': form, 'comment': comment })
    else:
        return render(request, 'home/home.html', { 'message': "You must be logged in to view this page." })

def compile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                code = body["code"]
            except:
                code = request.POST.get('code')

            # execute the code and get the output
            try:
                or_stout = sys.stdout
                
                sys.stdout = open('output.txt', 'w')

                exec(code)

                sys.stdout.close()

                sys.stdout = or_stout

                output = open('output.txt', 'r').read()
            except Exception as e:
                sys.stdout = or_stout

                output = e.args[0]


            return JsonResponse({ "output": output })


def comment(request, problem_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                comment = body["comment"]
            except:
                comment = request.POST.get('comment')

            #create a comment object
            comm = Comment()
            comm.comment = comment
            comm.user = UserProfile.objects.get(user=request.user)
            comm.problem = Problem.objects.get(id=problem_id)
            comm.parent = None
            comm.save()

            # add the comment to the problem
            problem = Problem.objects.get(id=problem_id)
            problem.comments.add(comm)
            problem.save()

            return JsonResponse({ "comment": comment })

            

            