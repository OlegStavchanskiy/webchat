////// static/channels/js/websocket.js
//
//const urlParams = new URLSearchParams(window.location.search);
//const chat_id = urlParams.get('chat_id');
//const chatSocket = new WebSocket("ws://localhost:8080/");
//console.log('1')
//
//chatSocket.addEventListener("open", (event) => {
//  socket.send("Hello Server!");
//});
//
////chatSocket.onmessage = function (e) {
////    var data = JSON.parse(e.data);
////    // Обработка нового сообщения и обновление интерфейса
////};

          // convert a JSON object in text format to js object that can be used
        const roomName=JSON.parse(document.getElementById('room-name'));
      //create websocket connection script
        const chatSocket=new WebSocket(
          'ws://' +
            window.location.host

        );

        //receive a massege
         chatSocket.onmessage=function(e){
            const data=JSON.parse(e.data)
            console.log(data);
            document.querySelector('#user-hello').innerHTML=(data.tester)
        }