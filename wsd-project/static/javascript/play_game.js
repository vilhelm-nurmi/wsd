window.addEventListener('message',parse_message);

var csrftoken = $.cookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function parse_message(message){
  if (message.data.messageType == "SCORE"){
    var score = message.data.score;
    $.ajax({
    url : window.location.href,
    type : "POST",
    data : {
        'type':'highscore',
        'score':score,
    },
    success : function(result) {alert(result.msg);}
});
  }
  if (message.data.messageType=="SAVE"){
    var game_state=message.data.gameState;
    $.ajax({
    url : window.location.href,
    type : "POST",
    data :
    {
      'type':'save',
      'game_state': JSON.stringify(game_state)
    },
    success : function(result) {alert(result.msg);}
  });
}
  if (message.data.messageType =="LOAD_REQUEST"){
    $.ajax({
    url : window.location.href,
    type : "POST",
    data :
    {
      'type':'load',
    },
    success : function(result) {
      parsed = JSON.parse(result.msg)
      var sent_message =  {
        messageType: "LOAD",
        gameState: parsed,
      };
    message.source.postMessage(sent_message,'*');
    },
    error : function(result) {alert(result.msg);}
  });
}
  if (message.data.messageType == "SETTING"){
     document.getElementById("gamebox1").height = message.data.options.height;
     document.getElementById("gamebox1").width = message.data.options.width;

  }
}
