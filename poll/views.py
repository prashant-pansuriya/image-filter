from PIL.ImageDraw2 import Pen, Draw
from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse
from PIL import Image
import numpy as np
import random
from poll.utils import get_filter_image
from django.db.models import Q
from .documents import PostDocument
INK = "red", "blue", "green", "yellow"


# def image(request):
#
#     # ... create/load image here ...
#     #image = Image.new("RGB", (800, 600), random.choice(INK))
#     #
#     # # serialize to HTTP response
#     # response = HttpResponse(image, mimetype="image/png")
#     # response['Content-Disposition'] = 'inline;filename=test.png'
#     return HttpResponse(image, content_type="image/png")

def image(request):
    if request.method == "POST":

        my_uploaded_file = request.FILES['my_uploaded_file']
        action = request.POST["action"]
        pil_image = Image.open(my_uploaded_file)
        cv_image = np.array(pil_image)
        image = get_filter_image(cv_image, action)
        pil_image = Image.fromarray(image)
        response = HttpResponse(content_type="image/png")
        pil_image.save(response, "PNG")
        response['Content-Disposition'] = 'attachment; filename="test.png"'
        return response

    else:
        return render(request, "home.html")


def search(request):

    if request.method == "POST":
        result = request.POST.get("search", False)
        if result:
            result = PostDocument.search().query("match", title = result)
            #Q = PostDocument.search().query
            #result = Q("match", name=result) or Q("match", title=result)
            print("************** Get Method Run :")
            print(result)
            #query = Q(title__contains= result)
            #query.add(Q(name__contains=result), Q.OR)
            #result = Post.objects.filter(query)
            #print(result)
            return render(request, "dispaly.html", {"result": result})

        else:
            result = Post.objects.all()
            return render(request, "dispaly.html", {"result": result})



    return render(request, "dispaly.html")
