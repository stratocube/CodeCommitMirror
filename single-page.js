var lastTab = 'puzzles'

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