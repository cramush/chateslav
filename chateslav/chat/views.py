from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from random import randint


def home(request):
    return render(request, 'chat/home.html')


def room(request, room):
    username = request.GET.get('username')
    # print(type(username))

    vowels_ru = ["а", "у", "о", "ы", "и", "э", "ю", "ё", "е"]
    consonants_ru = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м",
                     "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
    vowels_en = ["a", "e", "i", "o", "u"]
    consonants_en = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                     "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    if username is not None:
        if username[-1] == "я":
            username = username[:-1] + "ислав"
        elif username[-1] in vowels_ru:
            username = username + "слав"
        elif username[-1] in consonants_ru:
            username = username + "ослав"

        elif username[-2:] == "ya":
            username = username[:-2] + "islav"
        elif username[-1] in vowels_en:
            username = username + "slav"
        elif username[-1] in consonants_en:
            username = username + "oslav"

    rand = randint(1, 10)
    if rand == 1:
        username = "Artem. Prosto Artem kotoryj zabludilsya i ne znaet kuda idti"

    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        room_details = None
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def check_view(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
