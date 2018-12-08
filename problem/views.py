from django.shortcuts import render
from django.views.generic import View
from .forms import ProblemForm,AnswerForm
from .models import Problem
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class ProblemCreate(LoginRequiredMixin,View):
    form_class= ProblemForm
    template_name= 'problem/post_problem.html'

    def get(self, request):
        return render(request,self.template_name,{'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_problem=bound_form.save()
            return render(request,'problem/thankyou.html',{'thankyou':'Thank You For Your Contribution'})
        else:
            return render(request,self.template_name,{'form': bound_form})

class ProblemList(View):
    template_name='problem/problem_list.html'
    def get(self,request):
        return render(request,self.template_name,{'problems':Problem.objects.all()})


class ProblemDetail(View):
    template_name='problem/problem_detail.html'
    form_class=AnswerForm
    def get(self,request,slug):
        context={'problem':Problem.objects.get(slug=slug),'form':self.form_class()}
        return render(request,self.template_name,context)

    @method_decorator(login_required)
    def post(self,request,slug):
        bound_form=self.form_class(request.POST)
        obj=Problem.objects.get(slug=slug)
        real_answer=obj.answer
        if bound_form.is_valid():
            if bound_form.cleaned_data['answer'] == real_answer:
                return render(request,'problem/Answerstatus.html',{'message':'Correct !'})
            else:
                return render(request,'problem/Answerstatus.html',{'message':'Incorrect !'})
class About(View):
    template_name='problem/about.html'
    def get(self,request):
        return render(request,self.template_name)
