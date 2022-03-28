from zpage.models import SiteSettings

def sitesettings(request):
    context = dict()
    try:
        context['sitesetting'] = SiteSettings.objects.filter(status = 1).first()
    except:
        context['sitesetting'] = 'Site Ayarları Kaydedilmemis'
        
    # if not request.session.session_key:
    #     request.session.save()
    #     print('Yeni atanan: '+str(request.session.session_key))
    # print(request.session.session_key)
    # Middleware'de yaz

    return context