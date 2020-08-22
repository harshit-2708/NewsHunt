from django.shortcuts import render 
from newsapi import NewsApiClient 
from django.conf import settings
  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key =settings.APIKEY) 
    top = newsapi.get_top_headlines(q='') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
  
    return render(request, 'index.html', context ={"mylist":mylist}) 


def search(request, *args, **kwargs):
    query = request.GET.get('query')
    newsapi = NewsApiClient(api_key ='14a8784f1b004543b177f19f18adba1d') 
    top = newsapi.get_top_headlines(q=query) 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
  
    return render(request, 'index.html', context ={"mylist":mylist})