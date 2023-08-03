# Self-made site - Krupesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get input text
    txt = request.POST.get('rawTxt', 'default')
    print(txt)
    check = request.POST.get('removePunc', 'off')
    capFirst = request.POST.get('capitalizeFirst', 'off')
    cap = request.POST.get('capitalize', 'off')
    cnt = request.POST.get('charCount', 'off')

    # list of punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # list of things that are done on text
    purpose = ""

    # remove punctuations
    analyzed = ""
    if check == 'on':
        for char in txt:
            if char not in punctuations:
                analyzed += char
        purpose += 'Removed Punctuations'
    else:
        analyzed = txt

    # capitalize first letter
    if capFirst == 'on':
        for i in range(len(analyzed)):
            if analyzed[i] not in punctuations:
                analyzed = analyzed[:i] + \
                    analyzed[i].upper() + analyzed[i + 1:]
                break
        if not purpose:
            purpose += 'Capitalized First Letter'
        else:
            purpose += ' | Capitalized First Letter'

    # capitalize all letters
    if cap == 'on':
        analyzed = analyzed.upper()
        if not purpose:
            purpose += 'Capitalized All Letters'
        else:
            purpose += ' | Capitalized All Letters'

    # count characters
    cntWhole = len(txt)
    cntChar = len(analyzed)
    if cnt == 'on':
        if not purpose:
            purpose += 'Counted Characters'
        else:
            purpose += ' | Counted Characters'

    params = {'purpose': purpose, 'rawTxt': txt, 'analyzed_text': analyzed,
              'cntWhole': cntWhole, 'cntChar': cntChar}
    return render(request, 'analyze.html', params)
