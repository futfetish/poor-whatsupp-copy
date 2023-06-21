function scrolltobot(elementId) {
  var element = document.getElementById(elementId);
  element.scrollTop = element.scrollHeight;
}





function open_panel_1(but, panel, text  , count) {
    var h =( count * 38 ) +  18;

    document.addEventListener('click', function(e) {
        var settingsBtn = document.getElementById(but);
        var panelEl = document.getElementById(panel);
        var settingsTexts = document.getElementsByClassName(text);

        if (e.target !== settingsBtn && !e.target.closest('#' + but) && e.target !== panelEl) {
            settingsBtn.style.background = 'rgba(255, 255, 255, 0)';
            panelEl.style.width = '0px';
            settingsBtn.classList.remove("main__util_act");
            panelEl.style.height = '0px';
            Array.from(settingsTexts).forEach(function(elem) {
                elem.style.fontSize = '0';
                elem.style.color = 'rgba(235, 235, 235, 0)';
            });
        } else if (e.target !== panelEl) {
            if (panelEl.style.width !== '0px') {
                settingsBtn.classList.remove("main__util_act");
                settingsBtn.style.background = 'rgba(255, 255, 255, 0)';
                panelEl.style.width = '0px';
                panelEl.style.height = '0px';
                Array.from(settingsTexts).forEach(function(elem) {
                    elem.style.fontSize = '0';
                    elem.style.color = 'rgba(235, 235, 235, 0)';
                });
            } else {
                setTimeout(function () {
                    Array.from(settingsTexts).forEach(function(elem) {
                        elem.style.color = 'rgba(235, 235, 235, 1)';
                    });
                }, 100);
                settingsBtn.style.background = 'rgba(255, 255, 255, 0.1)';
                settingsBtn.classList.add("main__util_act");
                panelEl.style.width = '250px';
                panelEl.style.height = h + 'px';
                Array.from(settingsTexts).forEach(function(elem) {
                    elem.style.fontSize = '16px';
                });
            }
        }
    });
}

function umsg(id) {
if (document.getElementById(`full_msg${id}`)){
  document.getElementById(`msg_text${id}`).addEventListener('mouseenter', function(event) {
    document.getElementById(`settings_ls${id}`).style.opacity = '1';
  });

  document.getElementById(`msg_text${id}`).addEventListener('mouseleave', function(event) {
    document.getElementById(`settings_ls${id}`).style.opacity = '0';
  });

  document.addEventListener('click', function(e) {
  if (document.getElementById(`full_msg${id}`)){
    if (
      e.target !== document.getElementById(`settings_ls${id}`) &&
      !e.target.closest(`#settings_ls${id}`) &&
      e.target !== document.getElementById(`panel_ls${id}`)
    ) {
      document.getElementById(`panel_ls${id}`).style.width = '0px';
      document.getElementById(`panel_ls${id}`).style.height = '0px';
      $(`.settings_text_ls${id}`).css('font-size', '0');
      $(`.settings_text_ls${id}`).css('color', 'rgba(235, 235, 235 , 0)');
    } else if (e.target !== document.getElementById(`panel_ls${id}`)) {
      if (document.getElementById(`panel_ls${id}`).style.width !== '0px') {
        document.getElementById(`panel_ls${id}`).style.width = '0px';
        document.getElementById(`panel_ls${id}`).style.height = '0px';
        $(`.settings_text_ls${id}`).css('font-size', '0');
        $(`.settings_text_ls${id}`).css('color', 'rgba(235, 235, 235 , 0)');
      } else {
        setTimeout(function() {
          $(`.settings_text_ls${id}`).css('color', 'rgba(235, 235, 235 , 1)');
        }, 100);
        document.getElementById(`panel_ls${id}`).style.width = '250px';
        document.getElementById(`panel_ls${id}`).style.height = '56px';
        $(`.settings_text_ls${id}`).css('font-size', '16px');
      }
    }
    }
  });

  document.addEventListener('contextmenu', function(event) {
   if (document.getElementById(`full_msg${id}`)){
    if (event.target !== document.getElementById(`full_msg${id}`) && !event.target.closest(`#full_msg${id}`)) {
      document.getElementById(`panel_ls${id}`).style.width = '0px';
      document.getElementById(`panel_ls${id}`).style.height = '0px';
      $(`.settings_text_ls${id}`).css('font-size', '0');
      $(`.settings_text_ls${id}`).css('color', 'rgba(235, 235, 235 , 0)');
    }
    }
  });

  document.getElementById(`full_msg${id}`).addEventListener('contextmenu', function(event) {
    event.preventDefault();
    setTimeout(function() {
      $(`.settings_text_ls${id}`).css('color', 'rgba(235, 235, 235 , 1)');
    }, 100);
    document.getElementById(`panel_ls${id}`).style.width = '250px';
    document.getElementById(`panel_ls${id}`).style.height = '56px';
    $(`.settings_text_ls${id}`).css('font-size', '16px');
  });
}
}

function selfmsg(id) {

  var deleteButton = document.getElementById('ls__del_msg' + id);
  var ls_chat = document.getElementById('ls_chat');
  var msg = document.getElementById('full_msg' + id);

  deleteButton.addEventListener('click', function(event) {

    event.preventDefault();


    $.ajax({
      url: '/delete/msg/' + id,
      type: 'GET',
      success: function(response) {


      },
      error: function(xhr, status, error) {

        console.error(error);
      }
    });
  ls_chat.removeChild(msg);
  });
}

