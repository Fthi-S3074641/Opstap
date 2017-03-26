
function sendDataToServer(survey) {
    //send Ajax request to your web server.
    $.ajax({
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(survey.data),
            dataType: 'json',
            url: '/ajax',
            success: function (ret) {
            // var myModal = document.getElementById('myModal').innerHTML;
            // myModal.modal('hide');

            }
          });
      $('#myModal').modal('hide');
}


Survey.Survey.cssType = "bootstrap";

var surveyJSON = {locale:"en",  showProgressBar: "top", goNextPageAutomatic: true, pages:[{name:"page1",navigationButtonsVisibility:"hide",questions:[{type:"dropdown",choices:[{value:"1",text:"Guests"},{value:"2",text:"Volunteers"},{value:"3",text:"Family"},{value:"4",text:"mantelzorgers"},{value:"5",text:"Others"}],isRequired:true,name:"Your relationship with de Opstap",width:"300"}]},{name:"page2",questions:[{type:"comment",name:"Let us know the things you liked about De Opstap"}]},{name:"page3",navigationButtonsVisibility:"hide",questions:[{type:"rating",isRequired:true,name:"Rate de Opstap",rateValues:["3","4","5","6","7","8"]}]}]}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});


// ===========================


$('#in').keyup(function(e){
                if (e.keyCode == 13) {
                    $.post('/post', {'message': $(this).val()});
                    $(this).val('');
                }
            });

function sse() {
    var source = new EventSource('/stream');
    var out = document.getElementById('headerchange');
    
    source.onmessage = function(e) {
    // XSS in chat is fun

    // out.innerHTML =  e.data + '\n' + out.innerHTML;
   };
}

sse()

