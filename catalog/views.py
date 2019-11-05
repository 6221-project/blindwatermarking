from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from catalog import models
from catalog import image_deal


def index(request):
    return render(
        request,
        'index.html',
        context={'test_text': 'welcome to blind water marking'},
    )


def upload_image(request):
    image = request.FILES.get('image')
    image_name = image.name
    image_type = request.POST.get('image_type', None)
    models.image.objects.create(image_name=image_name, image_type=image_type, image=image)
    data = {
        "image_name": image_name,
        "src": "media/"+image_name
    }
    return JsonResponse(data)


def encode_image(request):

    o_image_name = request.POST.get('o_image_name', None)
    wm_image_name = request.POST.get('wm_image_name', None)
    image_name, path = image_deal.encode(o_image_name, wm_image_name)
    data = {
        "image_name": image_name,
        'src': path
    }
    return JsonResponse(data)


def decode_image(request):

    o_image_name = request.POST.get('o_image_name', None)
    bwm_image_name = request.POST.get('bwm_image_name', None)
    print(111111)
    print(bwm_image_name)
    print(111111)
    image_name, path = image_deal.decode(o_image_name, bwm_image_name)
    data = {
        "image_name": image_name,
        'src': path
    }
    return JsonResponse(data)


