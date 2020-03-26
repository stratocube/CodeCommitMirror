var lastTab;

function init() {
    animateBanner();

    var firstTab = $('#content-tab button:first-child');
    lastTab = firstTab.attr('id');
    firstTab.attr('class', 'active');
    loadTab(firstTab.attr('id'));
}

function animateBanner() {
    var banner = $('#banner');
    var speed = 400;
    var startcolor = '#EEEE00';
    banner
        .animate({ 'border-top-color': startcolor, 'border-bottom-color': startcolor }, speed)
        .animate({ 'border-top-color': 'black', 'border-bottom-color': 'black' }, speed,
            function() { animateBanner(); }
        ).delay(200);
}

function loadTab(tabId) {
    console.log(tabId);

    $('#tab-content').empty()
    $.get(tabId + '.html', (data) => {
        if (data) {
            $('#tab-content').load(tabId + '.html');
        }
    })
    .fail(() => {
        //$('#tab-content').empty();
    });

    $('#' + lastTab).attr('class', '');
    lastTab = tabId;
    $('#' + tabId).attr('class', 'active');

    setBackground(tabId);
}

function setBackground(tabId) {
    var url = 'css/' + tabId + '.css';

    $.get(url)
    .done(function() {
        document.getElementById("content-css").setAttribute('href', url)
    }).fail(function() {
        document.getElementById("content-css").setAttribute('href', '')
    });
}