from django.http import HttpResponse

def home(request):

    text = """<h1>IPT Connect</h1>

              <a href="http://connect.iptnet.info/FPT2018">Results of FPT 2018</a>"""
    return HttpResponse(text)
