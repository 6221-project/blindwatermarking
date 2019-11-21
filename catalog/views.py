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


def ed_image(request):
    return render(
        request,
        'EDimage.html',
        context={'test_text': 'welcome to blind water marking index2'},
    )


def s_graphic(request):
    return render(
        request,
        'Sgraphic.html',
        context={'test_text': 'welcome to blind water marking index2'},
    )


def upload_image(request):
    image = request.FILES.get('image')
    image_name = image.name
    image_type = request.POST.get('image_type', None)
    models.image.objects.create(image_name=image_name, image_type=image_type, image=image)
    data = {
        "image_name": image_name,
        "src": "/catalog/media/"+image_name
    }
    return JsonResponse(data)


def encode_image(request):

    o_image_name = request.POST.get('o_image_name', None)
    wm_image_name = request.POST.get('wm_image_name', None)
    seed = request.POST.get('seed', None)
    image_name = ''
    path = ''
    if seed is None:
        image_name, path = image_deal.encode(o_image_name, wm_image_name)
    else:
        image_name, path = image_deal.encode_with_seed(o_image_name, wm_image_name, int(seed))
    data = {
        "image_name": image_name,
        'src': path
    }
    return JsonResponse(data)


def decode_image(request):

    o_image_name = request.POST.get('o_image_name', None)
    bwm_image_name = request.POST.get('bwm_image_name', None)
    is_align = request.POST.get('is_align', None)
    seed = request.POST.get('seed', None)
    image_name = ''
    path = ''
    if is_align == 'true':
        is_align = True
    else:
        is_align = False
    if seed is None:
        image_name, path = image_deal.decode(o_image_name, bwm_image_name, is_align)
    else:
        image_name, path = image_deal.decode_with_seed(o_image_name, bwm_image_name, int(seed), is_align)
    data = {
        "image_name": image_name,
        'src': path
    }
    return JsonResponse(data)


