from django.shortcuts import render, HttpResponse, redirect
from .models import *
import json


# Create your views here.


def HomePage(request):
    foods = Food.objects.all()
    return render(request, "index.html", {"food": foods if foods.exists() else False})


def ProdoctsPage(request):
    if request.GET:
        user_id = request.GET.get("user_id")
        if not user_id:
            return redirect("home")
        else:
            foods = UserFoodList.objects.filter(user_id=user_id)
            if foods.exists() == True:
                return render(
                    request, "products.html", {"status": True, "foods": foods}
                )
            else:
                return render(request, "products.html", {"status": False})


def ProductDeletePage(request, user, id):
    r = UserFoodList.objects.get(id=id)
    r.delete()
    return redirect(f"/products/?user_id={user}")


def UpdatePage(request):
    uid = request.GET.get("user_id")
    foods = Food.objects.all()
    userfood = UserFoodList.objects.filter(user_id=uid)
    return render(
        request,
        "edit.html",
        {
            "food": foods if foods.exists() else False,
            "user": userfood if userfood.exists() else False,
        },
    )

###

def RuHomePage(request):
    foods = Food.objects.all()
    return render(request, "ru/index.html", {"food": foods if foods.exists() else False})


def RuProdoctsPage(request):
    if request.GET:
        user_id = request.GET.get("user_id")
        if not user_id:
            return redirect("home")
        else:
            foods = UserFoodList.objects.filter(user_id=user_id)
            if foods.exists() == True:
                return render(
                    request, "ru/products.html", {"status": True, "foods": foods}
                )
            else:
                return render(request, "ru/products.html", {"status": False})


def RuProductDeletePage(request, user, id):
    r = UserFoodList.objects.get(id=id)
    r.delete()
    return redirect(f"/ru/products/?user_id={user}")


def RuUpdatePage(request):
    uid = request.GET.get("user_id")
    foods = Food.objects.all()
    userfood = UserFoodList.objects.filter(user_id=uid)
    return render(
        request,
        "ru/edit.html",
        {
            "food": foods if foods.exists() else False,
            "user": userfood if userfood.exists() else False,
        },
    )

def FoodAddApi(request):
    if request.GET:
        user_id = request.GET.get("user_id")
        code = request.GET.get("code")
        count = request.GET.get("count")
        if not user_id or not code or not count:
            json_code = json.dumps([{"status": "false"}], indent=4)
            return HttpResponse(json_code, content_type="application/json")
        else:
            if str(user_id).isdigit() and str(count).isdigit():
                try:
                    save = Food.objects.get(rand=code)
                    save1 = Food.objects.filter(rand=code)
                    if save1.exists():
                        r = False
                        try:
                            n = UserFoodList.objects.get(
                                user_id=user_id, nomi=save.nomi
                            )
                            n.soni = int(n.soni) + int(count)
                            n.save()
                            r = True
                        except UserFoodList.DoesNotExist:
                            UserFoodList.objects.create(
                                user_id=user_id,
                                nomi=save.nomi,
                                narxi=save.narxi,
                                rasm=save.rasm,
                                soni=count,
                                rand=save.rand,
                            )
                            r = True
                        except Exception as e:
                            print("Error: " + f"{e}")
                        if r:
                            json_code = json.dumps([{"status": "true"}], indent=4)
                            return HttpResponse(
                                json_code, content_type="application/json"
                            )
                        else:
                            json_code = json.dumps([{"status": "false"}], indent=4)
                            return HttpResponse(
                                json_code, content_type="application/json"
                            )
                    else:
                        json_code = json.dumps([{"status": "false"}], indent=4)
                        return HttpResponse(json_code, content_type="application/json")
                except Food.DoesNotExist:
                    json_code = json.dumps([{"status": "false"}], indent=4)
                    return HttpResponse(json_code, content_type="application/json")
            else:
                json_code = json.dumps([{"status": "false"}], indent=4)
                return HttpResponse(json_code, content_type="application/json")
    else:
        json_code = json.dumps([{"status": "false"}], indent=4)
        return HttpResponse(json_code, content_type="application/json")


def FoodUpdateApi(request):
    if request.GET:
        user_id = request.GET.get("user_id")
        code = request.GET.get("code")
        count = request.GET.get("count")
        if not user_id or not code or not count:
            json_code = json.dumps([{"status": "false"}], indent=4)
            return HttpResponse(json_code, content_type="application/json")
        else:
            if str(user_id).isdigit() and str(count).isdigit():
                try:
                    save = Food.objects.get(rand=code)
                    save1 = Food.objects.filter(rand=code)
                    if save1.exists():
                        r = False
                        if int(count) != 0:
                            try:
                                n = UserFoodList.objects.get(
                                    user_id=user_id, nomi=save.nomi
                                )
                                n.soni = int(count)
                                n.save()
                                r = True
                            except UserFoodList.DoesNotExist:
                                UserFoodList.objects.create(
                                    user_id=user_id,
                                    nomi=save.nomi,
                                    narxi=save.narxi,
                                    rasm=save.rasm,
                                    soni=count,
                                    rand=save.rand,
                                )
                                r = True

                            except Exception as e:
                                r = False
                                print("Error: " + f"{e}")
                        else:
                            m = UserFoodList.objects.get(
                                user_id=user_id, nomi=save.nomi
                            )
                            m.delete()
                            r = True
                        if r:
                            json_code = json.dumps([{"status": "true"}], indent=4)
                            return HttpResponse(
                                json_code, content_type="application/json"
                            )
                        else:
                            json_code = json.dumps([{"status": "false"}], indent=4)
                            return HttpResponse(
                                json_code, content_type="application/json"
                            )
                    else:
                        json_code = json.dumps([{"status": "false"}], indent=4)
                        return HttpResponse(json_code, content_type="application/json")
                except Food.DoesNotExist:
                    json_code = json.dumps([{"status": "false"}], indent=4)
                    return HttpResponse(json_code, content_type="application/json")
            else:
                json_code = json.dumps([{"status": "false"}], indent=4)
                return HttpResponse(json_code, content_type="application/json")
    else:
        json_code = json.dumps([{"status": "false"}], indent=4)
        return HttpResponse(json_code, content_type="application/json")


def FoodInfo(request):
    if request.GET:
        code = request.GET.get("code")
        if not code:
            json_code = json.dumps([{"status": "false"}], indent=4)
            return HttpResponse(json_code, content_type="application/json")
        else:
            save = Food.objects.filter(rand=code)
            if save.exists() != False:
                r = Food.objects.get(rand=code)
                json_code = json.dumps(
                    [
                        {
                            "status": "true",
                            "nomi": r.nomi,
                            "narxi": r.narxi,
                            "rasm": r.rasm.url,
                            "holati": r.holati,
                            "rand": r.rand,
                        }
                    ],
                    indent=4,
                )
                return HttpResponse(json_code, content_type="application/json")
            else:
                json_code = json.dumps([{"status": "false"}], indent=4)
                return HttpResponse(json_code, content_type="application/json")
    else:
        json_code = json.dumps([{"status": "false"}], indent=4)
        return HttpResponse(json_code, content_type="application/json")
