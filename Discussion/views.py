from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from .models import Discussion,Comments
from .forms import DiscussionForm,CommentsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class DiscussionView(View):
    template_name='Discussion/discussion.html'

    def get(self,request):
        return render(request,self.template_name,{'discussion':Discussion.objects.all()})

class DiscussionDetailView(View):
    template_name='Discussion/discussion_detail.html'
    form_class=CommentsForm

    def get(self,request,slug):
        obj=Discussion.objects.get(slug=slug)
        return render(request,self.template_name,{'discussion':obj,'comments':obj.comments_set.all(),'form': self.form_class()})
    @method_decorator(login_required)
    def post(self,request,slug):
        obj=Discussion.objects.get(slug=slug)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form.instance.username=request.user.username
            new_comment=bound_form.save()
            obj.comments_set.add(new_comment)
            return render(request,self.template_name,{'discussion':obj,'comments':obj.comments_set.all(),'form': self.form_class()})
        else:
            return render(request,self.template_name,{'form': bound_form})

class NewDiscussionView(LoginRequiredMixin,View):
    template_name='Discussion/new_discussion.html'
    form_class= DiscussionForm
    def get(self,request):
        return render(request,self.template_name,{'form': self.form_class()})
    def post(self,request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form.instance.creator=request.user.username
            bound_form.save()
            return render(request,'Discussion/discussion.html',{'discussion':Discussion.objects.all()})
        else:
            return render(request,self.template_name,{'form': bound_form})
class CommentsView(LoginRequiredMixin,View):
    template_name='Discussion/'
