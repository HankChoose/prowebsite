from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect, reverse
from django.shortcuts import render
from . import util
from django import forms

from django.http import JsonResponse

def index(request):
    #if "entries" not in request.session:
        #request.session["entries"]=[]
    #my_list = util.list_entries()
    #search_string = ["h"]
    #new_list = [item for item in my_list if any(char.lower() in item.lower() for char in search_string)]
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        #"entries": request.session["entries"]
    
    })


class NewEentryForm(forms.Form):
    newEentryTitle = forms.CharField(label="New Entry Title:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    newEentryContent = forms.CharField(label="New Entry Content:", widget=forms.Textarea(attrs={'class': 'form-control'}))
    #priority = forms.IntegerField(label="Priorit",min_value=0 ,max_value=10)
    #newEentryTitle = forms.CharField(label="New Entry Title:")
    #newEentryContent = forms.CharField(label="New Entry Content:")
def entryadd(request):
    # Get the content of the requested entry
    
    if request.method == "POST":
        formPOST = NewEentryForm(request.POST)
        if formPOST.is_valid():
           newTitle = formPOST.cleaned_data["newEentryTitle"]
           newContent = formPOST.cleaned_data["newEentryContent"]
           #request.session["entries"] +=[newTitle]
           util.save_entry(newTitle,newContent)
           return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/entryadd.html", {
            "entryFrom":formPOST
        })

      

    return render(request, "encyclopedia/entryadd.html", {
        "entryFrom":NewEentryForm()
    })


#entries=["a","b","c",]
#cd C:\Users\Administrator\Desktop\WebUI\Project1\wiki
#python manage.py migrate


from .util import convert_markdown_to_html
from django.http import HttpResponseNotFound
from django.urls import reverse

def entry(request, title):
    # Get the content of the requested entry
    content = util.get_entry(title)
    content_html=util.convert_markdown_to_html(content)
    # If the entry does not exist, render an error page
    if content is None:
        #return HttpResponseNotFound(f"Page not found: {title}")
        return render(request, "encyclopedia/entrycontent.html", {
            "title": title.capitalize(),
            "content": f"Page not found: {title}",
        }) 
    
    # If the entry exists, render the entry page
    return render(request, "encyclopedia/entrycontent.html", {
        "title": title.capitalize(),
        "content": content_html,
    })

def hankview(request):
    # 创建HttpResponse对象
    response = HttpResponse('Hank say:Hello World!')

    # 打印响应内容
    print(response.content)

    # 返回HttpResponse对象
    return response


class EditEentryForm(forms.Form):
    editEentryTitle = forms.CharField(label="Entry Title:", widget=forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}))
    editEentryContent = forms.CharField(label="Entry Content:", widget=forms.Textarea(attrs={'class': 'form-control'}))
    #editEentryTitle = forms.CharField(label="Entry Title:")
    #editEentryContent = forms.CharField(label="Entry Content:")
    #my_param = forms.CharField(widget=forms.HiddenInput())

def entryedit(request, title):
    # Get the content of the requested entry
    content = util.get_entry(title)

    initial_data = {
        "editEentryTitle": title.capitalize(),
        "editEentryContent": content,
    }
    
    if request.method == "POST":
        formPOST = EditEentryForm(request.POST)
        if formPOST.is_valid():
            editTitle = formPOST.cleaned_data["editEentryTitle"]
            editContent = formPOST.cleaned_data["editEentryContent"]
            #my_param_value = formPOST.cleaned_data['my_param']

            #my_param = request.POST.get('my_param')

            #request.session["entries"] +=[newTitle]
            #print("editTitle :", editTitle ) 
            #print("editContent  :",editContent  ) 
            util.save_entry(editTitle,editContent)

            current_url = request.build_absolute_uri()

            # 编辑URL并去掉最后一部分
            parts = current_url.split('/')  # 拆分URL成多个部分
            edited_url = '/'.join(parts[:-2])  # 去掉最后一个部分并重新组合URL

            #return HttpResponse("parts: " + parts)
            #response_content = f"{value1} {value2}"

            #list_str = ', '.join(str(item) for item in parts)
            #return HttpResponse("List values: " + list_str + edited_url)

            # 重定向到编辑后的URL
            return HttpResponseRedirect(edited_url)
            #return HttpResponse("edited_url: " + edited_url)
            #return HttpResponseRedirect(reverse('encyclopedia:entry', title = editTitle))
 
        else:
            return render(request, "encyclopedia/entryedit.html", {
            "entryFrom":formPOST
        })
        
    return render(request, "encyclopedia/entryedit.html", {
        "entryEditFrom":EditEentryForm(initial=initial_data)
    })

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def search(request):
    
    json_str=request.body
    #if request.method == 'POST' and request.is_ajax():
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        content_type = request.META.get("CONTENT_TYPE")
        if content_type == "application/x-www-form-urlencoded; charset=UTF-8":
            query = request.POST.get("query", "")
            #password = request.POST.get("password", "")
            #data = json.dumps({"query": query, "password": password}) 
            #data = json.dumps({"query": "query1"})     
        else:
            #如果当前报错,请执行
            #json_str = json_str.decode()
            json_str =request.body.decode('utf-8')
            payload = json.loads(json_str)
            query = payload.get('query')
            #search_list=util.list_entries()
            #data = json.dumps({"uname": uname, "password": password})   
            data = json.dumps(query)
           
        data = json.dumps({"query": query})  
        my_list = util.list_entries()
        #search_string = query
        search_string = [query]
        #search_string = [query, 'p']
        #new_list = [item for item in my_list if characters in item]
        new_list = [item for item in my_list if any(char.lower() in item.lower() for char in search_string)]
        data = new_list 
        #return HttpResponse(data)
        return JsonResponse(data, safe=False)
    return render(request, "encyclopedia/index.html", {
        "entries": new_list
        #"entries": request.session["entries"]
    })

    #return JsonResponse({}, status=400)

def searchfrom(request):
    #if request.method == 'GET' and request.is_ajax():
        #query = request.POST.get('q', '')
        #query_str = json.dumps(query)
        #print(query_str)
    #return HttpResponse("query_str: " + query)
    q_value = request.GET.get('q')
    #print("q_value="+q_value)

    my_list = util.list_entries()
    search_string = [q_value]
    new_list = [item for item in my_list if any(char.lower() in item.lower() for char in search_string)]
    return render(request, "encyclopedia/index.html", {
        "entries": new_list
        #"entries": request.session["entries"]
    
    })

#from .util import convert_markdown_to_html

def entry_page(request, entry_id):
    # Retrieve the Markdown content for the entry
    markdown_content = util.get_entry(entry_id)
    
    # Convert Markdown to HTML
    html_content = convert_markdown_to_html(markdown_content)
    
    return render(request, 'entry_page.html', {'content': html_content})



import random
from django.shortcuts import redirect
from .models import Book
def random_page(request):
    #entries = Book.objects.all()
    random_entry = random.choice(util.list_entries())
    #return redirect('encyclopedia/entrycontent.html', slug=random_entry.slug)
   
    return render(request, "encyclopedia/entrycontent.html", {
        "title": random_entry,
        "content": util.get_entry(random_entry),
    })
