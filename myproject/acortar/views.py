
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from acortar.models import ShortedUrl
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def redirigir(request, numero):
    try:
        url = ShortedUrl.objects.get(id=numero).urloriginal
        return HttpResponseRedirect(url)
    except ShortedUrl.DoesNotExist:
        resp = "Error"
        return HttpResponse(resp)

@csrf_exempt
def acortar(request):
    if request.method == "GET":
        listaUrls = ShortedUrl.objects.all()
        if ShortedUrl.objects.all().exists():
            resp = "<h2>Acortar URLs:</h2><br/>"
            for i in listaUrls:
                resp += "<a href=" + str(i.id) + ">" + "localhost:8000/" + str(i.id) + " </a>" + "  -->  " + "<a href=" + i.urloriginal + ">" + i.urloriginal + " </a> <br/>"
        else:
            
            resp = "<h2>Acortar URLs:</h2>"
            
        resp += "<form method='POST' action>" \
                " <br>URL: <input type='text' name='urloriginal'>" \
                "<input type='submit' value='Acortar'></form>"
        return HttpResponse(resp)

    elif request.method == "POST":
        acortada = False
        url = request.POST['urloriginal']
        if url.startswith('http://') or url.startswith('https://'):
            urlcompleta = url
        else:
            urlcompleta = "http://" + url
        listaUrls = ShortedUrl.objects.all()
        for i in listaUrls:
            if i.urloriginal == urlcompleta:
                urlacortada = ShortedUrl.objects.get(urloriginal = urlcompleta)
                urlacortada = urlacortada.id
                acortada = True
        if acortada == False:
            url_nueva = ShortedUrl(urloriginal = urlcompleta)
            url_nueva.save()
            urlacortada = url_nueva.id
        resp = "<a href=" + str(urlacortada) + ">" + "localhost:8000/" + str(urlacortada) + " </a>" + "  -->  " + "<a href=" + urlcompleta + ">" + urlcompleta + " </a> <br/>"
        return HttpResponse(resp)
    else:
        return HttpResponse('Method not allowed', status=405)

