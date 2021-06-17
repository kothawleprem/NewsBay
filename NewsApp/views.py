from django.shortcuts import render, HttpResponse
import requests
import re


def api(category,country):
    if len(country) == 0:
        myapi = f"https://newsapi.org/v2/top-headlines?country=in&language=en&category={category}&apiKey=14bf28b9914845dd91f04c6e0146f8ee"
    else:
        code = ""
        mylist = [["The United Arab Emirates","ae"],["United States", "us"],["Australia", "au"],  ["India", "in"],["Argentina","ar"], ["Austria","at"],["Belgium","be"], ["Bulgaria","bg"], ["Brazil","br"], ["Canada","ca"], ["China","cn"], ["Colombia","co"], ["Cuba","cu"], ["Czechia","cz"],["Egypt","eg"], ["France","fr"],["United Kingdom", "gb"], ["Greece","gr"], ["Hong Kong","hk"], ["Hungary","hu"], ["Indonesia","id"], ["Ireland","ie"], ["Israel","il"], ["Italy","it"], ["Japan","jp"], ["Republic of Korea","kr"], ["Lithuania","lt"], ["Latvia","lv"], ["Morocco","ma"], ["Mexico","mx"], ["Malaysia","my"], ["Nigeria","ng"], ["Netherlands","nl"], ["Norway","no"], ["New Zealand","nz"], ["Philippines","ph"], ["Poland","pl"], ["Portugal","pt"], ["Romania","ro"], ["rs"],  ["Russia","ru"], ["Saudi Arabia","sa"], ["Sweden","se"], ["Singapore","sg"], ["Slovenia","si"], ["Slovakia","sk"], ["Thailand","th"], ["Turkey","tr"], ["Taiwan","tw"], ["Ukraine","ua"], ["Venezuela","ve"], ["South Africa","za"]]


        for i in range(len(mylist)+1):
                # print(mylist[i][0])
                    if country == mylist[i][0]:
                        code = mylist[i][1]
                        print(code)
                        break
        if len(code) == 0:
            myapi = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&apiKey=14bf28b9914845dd91f04c6e0146f8ee"
        else:
            myapi = f"https://newsapi.org/v2/top-headlines?language=en&country={code}&category={category}&apiKey=14bf28b9914845dd91f04c6e0146f8ee"
    json_data = requests.get(myapi).json()
    articles = json_data["articles"]
    data_list = []
    for article in articles:
        data = []
        title = "->" + article['title']
        description = article['description']
        if description is None:
            description = "No Description Available."
        url = article['url']
        url_img = article['urlToImage']
        # print(type(url_img))
        # ext = re.findall('\.jpg',url_img)
        # print(ext)
        if url_img is None:
            url_img = "https://st.depositphotos.com/1006899/3776/i/950/depositphotos_37765339-stock-photo-news.jpg"
        elif re.search('\.jpg',url_img) or re.search('\.png',url_img) or re.search('\.jpeg',url_img):
            pass
        else:
            url_img = "https://st.depositphotos.com/1006899/3776/i/950/depositphotos_37765339-stock-photo-news.jpg"
    
        data.append(url_img)
        data.append(title)
        data.append(description)
        data.append(url)
        data_list.append(data)
    
    return data_list

def Home(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("general",country),
                'country' : country
    }
    return render(request,'NewsApp/index.html',context)

def Business(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("business",country),
                'country' : country
    }
    return render(request,'NewsApp/business.html',context)

def Sports(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("sports",country),
                'country' : country
    }
    return render(request,'NewsApp/sports.html',context)

def Science(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("science",country),
                'country' : country
    }
    return render(request,'NewsApp/science.html',context)

def Health(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("health",country),
                'country' : country
    }
    return render(request,'NewsApp/health.html',context)

def Technology(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("technology",country),
                'country' : country
    }
    return render(request,'NewsApp/technology.html',context)

def Entertainment(request):
    if 'country' in request.GET:
        country = request.GET.get('country')
    else:
        country = ""
    context = { 'data_list': api("entertainment",country),
                'country' : country
    }
    return render(request,'NewsApp/entertainment.html',context)


