from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy, reverse
from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.db.models import Q
from django.views import View
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = "/tweets/create"
    # login_url = "/admin/"
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class =  TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweets/"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/tweet_confirm_delete.html"
    # print(reverse_lazy("home"))
    success_url = reverse_lazy("tweet:list") # tweet/list

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # print("*************Tweet.objects.get(pk=pk): ", Tweet.objects.get(pk=1))
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     print("*******************pk", pk )
    #     return Tweet.objects.get(pk=pk)
class TweetListView(ListView):
    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query)
                           | Q(user__username__icontains=query)
                           )
        return qs

    def get_context_data(self, *args, **kwargs):

        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["create_form"] =TweetModelForm
        context["create_url"] = reverse_lazy("tweet:create")
        return context



def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(id=id)
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object":obj
    }
    return render(request, "tweets/tweet_detail.html", context)
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/tweet_list.html", context)