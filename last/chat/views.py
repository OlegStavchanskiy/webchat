import json
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from chat.models import Message, ChatRoom, User
from chat.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'auth.html')
    else:
        name = request.user.first_name
        usrs = len(User.objects.all())
        c_i = request.GET.get('chat_id', 1)
        chat = ChatRoom.objects.all()
        mess = Message.objects.filter(room=c_i)
        return render(request, 'main.html', {'chat': chat, 'messages': mess, 'param': c_i, 'name': name, 'usrs': usrs, 'ms': len(mess)})


def post_message(request):
    if request.method == 'POST':
        form = request.POST.get('mess')
        chat_id = request.GET.get('chat_id')

        if not chat_id:
            # Здесь вы можете решить, что делать, если chat_id отсутствует
            # Например, создать новую комнату или вернуть ошибку
            return HttpResponse("Chat ID is missing")

        room = get_object_or_404(ChatRoom, id=chat_id)
        user = request.user
        message = Message(content=form, room=room, user=user)
        message.save()
    c_i = request.GET.get('chat_id')
    chat = ChatRoom.objects.all()
    mess = Message.objects.filter(room=c_i)
    return render(request, 'main.html', {'chat': chat, 'messages': mess, 'param': c_i})


def get_messages(request):
    messages = Message.objects.filter(room=request.GET.get('chat_id'))
    messages = [
        {'content': message.content, 'user': message.user.first_name, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for message in messages
    ]
    messages = {
        'data': messages
    }
    messages = json.dumps(messages)
    return HttpResponse(messages)


def doLogout(request):
    logout(request)
    return redirect('index')


def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['nick']  # Populate the first_name field
            user.save()

            return redirect('index')
    return render(request, 'registration.html')
