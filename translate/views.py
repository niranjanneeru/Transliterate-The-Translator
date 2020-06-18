from django.shortcuts import render
from transliterate import translit, slugify
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    language_packs = {"hy": "Armenian", "bg": "Bulgarian(beta)", "ka": "Georgian", "el": "Greek",
                      "mk": "Macedonian(alpha)", "mn": "Mongolian(alpha)", "ru": "Russian", "sr": "Serbian(alpha)",
                      "uk": "Ukrainian(beta)"}

    try:
        text = request.POST.get("textbox")
        code = request.POST.get("spinner")
        data = translit(text, code)
    except:
        data = ''

    try:
        text = request.POST.get("textbox1")
        data_1 = " ".join(slugify(text).split("-"))
    except:
        data_1 = ""

    context = {
        'languages': language_packs,
        'data': data,
        'data_1':data_1
    }
    return render(request, 'translate/index.html', context)
