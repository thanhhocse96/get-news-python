from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import News

# Create your views here.
def index(request):
    lastest_news_list = News.objects.order_by('-news_time_publish')[:5]
    template = loader.get_template('getnewsurl/index.html')
    context = {
        'lastest_news_list': lastest_news_list,
    }
    return HttpResponse(template.render(context, request))
    
def getUrl(request):
    response = "Trang lấy tin tức theo URL"
    return HttpResponse(response)

def viewNews(request, news_id):
    try:
        news_details = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("Chưa tồn tại tin tức cần duyệt")
    return render(request,'getnewsurl/news_content.html', {'content': news_details})
    # response = "Bạn đang xem tin tức số %s trong dữ liệu."
    # return HttpResponse(response % news_id)

def viewNewsStance(request, news_id):
    response = "Bạn đang xem lập trường của tin tức số %s trong dữ liệu."
    return HttpResponse(response % news_id)

