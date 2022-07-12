from xml.dom.minidom import Document
from django.shortcuts import render

# Create your views here.
def index(req) :
    context = {
        
    }
    
    return render(req, 'ITSAC_WEB/index.html', context=context)