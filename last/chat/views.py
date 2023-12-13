import json

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from chat.models import Message, ChatRoom
from chat.forms import MessageForm
import time



def index(request):
    c_i = 1
    c_i = request.GET.get('chat_id')
    chat = ChatRoom.objects.all()
    mess = Message.objects.filter(room=c_i)
    return render(request, 'main.html', {'chat': chat, 'messages': mess, 'form': MessageForm(), 'param': c_i})


def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        chat_id = request.GET.get('chat_id')

        if not chat_id:
            # Здесь вы можете решить, что делать, если chat_id отсутствует
            # Например, создать новую комнату или вернуть ошибку
            return HttpResponse("Chat ID is missing")

        room = get_object_or_404(ChatRoom, id=chat_id)
        user = request.user

        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.user = user
            message.save()
    c_i = request.GET.get('chat_id')
    chat = ChatRoom.objects.all()
    mess = Message.objects.filter(room=c_i)
    return render(request, 'main.html', {'chat': chat, 'messages': mess, 'form': MessageForm(), 'param': c_i})





def get_new_messages(request):
    # Логика для проверки новых сообщений
    new_messages = Message.objects.filter(room=1)
    messages = [
        {'content': message.content, 'user': message.user.first_name, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for message in new_messages
    ]

    # Формирование ответа в формате Server-Sent Events (SSE)
    response = HttpResponse(content_type='text/event-stream')
    for message in messages:
        response.write(f'data: {json.dumps(message)}\n\n')

    return response



