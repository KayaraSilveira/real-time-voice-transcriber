$(document).ready(function() {
    var request_in_progress = false;
    const transcriptionBox = document.querySelector('#transcription-box');
    setInterval(function () {
            if (!request_in_progress) {
                request_in_progress = true;

            let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: 'GET',
                url: '/transcribe',
                dataType: 'json',
                beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrf_token);
                },
                success: function (data) {
                    transcriptionBox.querySelector('p').remove();
                    transcriptionBox.insertAdjacentHTML("beforeend", `<p>${data.transcription}</p>`); 
                    console.log(data)
                    request_in_progress = false;
                },
                error: function (xhr, status, error) {
                    console.error(error);
                    request_in_progress = false;
                }
            });
        }
    }, 100);    
  });
  