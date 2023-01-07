from django.shortcuts import render
from .models import playerdata
from .ELO import elo

def home(request):
    table=playerdata.objects.all()
    return render (request,'home.html',{'table':table})


def add(request):
    
    if (request.method == 'POST'):
        name=request.POST['some1']
        name=name.strip()
        new_player= playerdata(Name=name)
        
        if name =='':
            error ="Add a player"
            return render(request,'add_player.html',{'alert':error})
        
        try:
            playerdata.objects.get(Name=name)
        except Exception:
            new_player.save()
            return render(request,'add_player.html')
        
        error ="Player already added"
        return render(request,'add_player.html',{'alert':error})

        
    return render(request,'add_player.html')


def N_Game(request):
    if (request.method == 'POST'):
        p1name=request.POST['p1']
        p2name=request.POST['p2']
        p3name=request.POST['p3']
        p4name=request.POST['p4']
        
        if(p1name==p2name or p1name==p3name or p1name==p4name
           or p2name==p3name or p2name==p4name or p3name==p4name):
            error="player Repeated"
            return render(request, 'New_game.html',{'alert':error})
        try:
            p1=playerdata.objects.get(Name=p1name)
            p2=playerdata.objects.get(Name=p2name)
            p3=playerdata.objects.get(Name=p3name)
            p4=playerdata.objects.get(Name=p4name)
        except Exception:
            error ="player not added"
            return render(request, 'New_game.html',{'alert':error})
        
        N_Ratings = elo(p1.Rating,p2.Rating,p3.Rating,p4.Rating, p1.G_played,p2.G_played,p3.G_played,p4.G_played)
        p1.Rating = N_Ratings[0]; p2.Rating = N_Ratings[1]; 
        p3.Rating = N_Ratings[2]; p4.Rating = N_Ratings[3]
        
        p1.G_played = p1.G_played + 1
        p2.G_played = p2.G_played + 1
        p3.G_played = p3.G_played + 1
        p4.G_played = p4.G_played + 1
        
        p1.G_won = p1.G_won +1
        p2.G_won =p2.G_won +1
        p3.G_lost=p3.G_lost +1
        p4.G_lost=p4.G_lost+1
        
        p1.save()
        p2.save()
        p3.save()
        p4.save()
        
    option = playerdata.objects.raw("SELECT id,Name FROM myapp_playerdata")
    return render(request, 'New_game.html', {'option':option})