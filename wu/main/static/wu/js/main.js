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


