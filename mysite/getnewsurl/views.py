from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("")
    
def getUrl(request):
    pass

def viewNews(request, news_id):
    response = "Bạn đang xem tin tức số %s trong dữ liệu."
    return HttpResponse(response % news_id)

def viewNewsStance(request, news_stance_id):
    response = "Bạn đang xem lập trường của tin tức số %s trong dữ liệu."
    return HttpResponse(response % news_stance_id)