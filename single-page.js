var lastTab = 'puzzles'

function init() {
    animateBanner();
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
    console.log('#' + tabId);

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
}

function gotoContent() {
    $('#content').load('content.html', () => {
        var firstTab = $('#content-tab button:first-child');
        firstTab.attr('class', 'active');
        loadTab(firstTab.attr('id'));
    });
}