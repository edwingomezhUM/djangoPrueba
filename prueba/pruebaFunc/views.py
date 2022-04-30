from unicodedata import name
from unittest import result
from django.shortcuts import render
from django.views import View
from .models import tracks, genres
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

#METODO PARA INSERTAR LA DATA DEL JSON DE LA PRUEBA
@api_view(['GET'])
def insertData(request):
    
    r = requests.get('https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json')

    jsonGet = r.json()

    results = jsonGet['feed']['results']

    for x in results:
        id = 0
        if 'id' in x:
            id = x['id']
        artistName = ''
        if 'artistName' in x:
            artistName = x['artistName']
        name = ''
        if 'name' in x:
            name = x['name']
        kind = ''
        if 'kind' in x:
            kind = x['kind']
        artistId = ''
        if 'artistId' in x:
            artistId = x['artistId']
        artistUrl = ''
        if 'artistUrl' in x:
            artistUrl = x['artistUrl']
        contentAdvisoryRating = ''
        if 'contentAdvisoryRating' in x:
            contentAdvisoryRating = x['contentAdvisoryRating']
        artworkUrl100 = ''
        if 'artworkUrl100' in x:
            artworkUrl100 = x['artworkUrl100']
        url = ''
        if 'url' in x:
            url = x['url']

        

        a = tracks(id = id, artistName = artistName, name = name, kind = kind, artistId = artistId, artistUrl = artistUrl,contentAdvisoryRating = contentAdvisoryRating,artworkUrl100 = artworkUrl100,url = url)

        a.save()

        for g in x['genres']:
            genreId = 0
            if 'genreId' in g:
                genreId = g['genreId']
            name = ''
            if 'name' in g:
                name = g['name']
            url2 = ''
            if 'url' in g:
                url2 = g['url']
            g = genres(genreId = genreId, name = name, url = url2)

            g.save()
            
    return JsonResponse({'data':'ok'})

# Un punto final para agregar nuevas pistas usando ORM.
@api_view(['GET'])
def insertTracks(request):
    args= dict(request.GET)
    
    listArtist =[]

    valueGet = dict(args.items())

    id = 0
    if 'id' in valueGet:
        id = int(valueGet['id'][0])
    artistName = ''
    if 'artistName' in valueGet:
        artistName = valueGet['artistName'][0]
    name = ''
    if 'name' in valueGet:
        name = valueGet['name'][0]
    kind = ''
    if 'kind' in valueGet:
        kind = valueGet['kind'][0]
    artistId = ''
    if 'artistId' in valueGet:
        artistId = valueGet['artistId'][0]
    artistUrl = ''
    if 'artistUrl' in valueGet:
        artistUrl = valueGet['artistUrl'][0]
    contentAdvisoryRating = ''
    if 'contentAdvisoryRating' in valueGet:
        contentAdvisoryRating = valueGet['contentAdvisoryRating'][0]
    artworkUrl100 = ''
    if 'artworkUrl100' in valueGet:
        artworkUrl100 = valueGet['artworkUrl100'][0]
    url = ''
    if 'url' in valueGet:
        url = valueGet['url'][0]


    a = tracks(id = id, artistName = artistName, name = name, kind = kind, artistId = artistId, artistUrl = artistUrl,contentAdvisoryRating = contentAdvisoryRating,artworkUrl100 = artworkUrl100,url = url)

    a.save()

    return JsonResponse({'data':'ok'})

####Un punto final para proporcionar una búsqueda dentro de las pistas (al menos por nombre, pero es abierto a cualquier sugerencia)
@api_view(['GET'])
def tracksName(request):

    args= dict(request.GET)
    
    listArtist =[]

    value = dict(args.items())

    nameValue = str(value['name'][0])
    
    listArtist = tracks.objects.filter(name = f"{nameValue}")

    if listArtist:
        return JsonResponse(list(listArtist.values())[0])
    else:
        return JsonResponse({'data':'no existe datos con ese nombre'})

####Un punto final para eliminar una pista, usando un identificador dado (definido por usted)
@api_view(['GET'])
def delTracks(request):

    args= dict(request.GET)
    
    listArtist =[]

    value = dict(args.items())

    idValue = value['id'][0]

    listArtist = tracks.objects.filter(id = int(idValue))

    if listArtist:
        listArtist.delete()

        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'result':'no data found'})

##Un punto final que permitiría obtener las 50 mejores pistas de popularidad. (SE MODIFICA POR QUE NO SE ENCUENTRAN DATOS PARA LA RELACIÓN DE POPULARIDAD DE LOS ARTISTAS) 
@api_view(['GET'])
def topTracks(request):

    lista = tracks.objects.all().order_by('artistId')[:50]

    # result = lista.values_list('artistId', 'artistName')
    # print(result.values())
    
    return JsonResponse(list(lista.values_list('artistId', 'artistName')), safe= False)
    
 
@api_view(['GET'])
def prueba_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = genres.objects.get(pk=pk) 
    except genres.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
  
    
        
