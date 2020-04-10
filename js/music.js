var musicData = [
    ["WTC I Preludio", ""],
    ["WTC V Fuga", "audio/wtc-05-fugue.mp3"],
    ["WTC IX Preluio", "audio/wtc-09-prelude.mp3"],
    ["WTC XI Preludio", "audio/wtc-11-prelude.mp3"],
    ["WTC XIII Preludio", "audio/wtc-13-prelude.mp3"],
    ["WTC XVII Preludio", "audio/wtc-17-prelude.mp3"],
    ["WTC XIX Preludio", "audio/wtc-19-prelude.mp3"],
    ["", ""],

    ["English Suite 1 Courante I", "audio/es-1-courante-1.mp3"],
    ["English Suite I Bourree I", ""],
    ["English Suite IV Prelude (half)", "audio/es-4-prelude.mp3"],
    ["English Suite IV Allemande", "audio/es-4-allemande.mp3"],
    ["English Suite IV Courante", ""],
    ["English Suite IV Sarabande", "audio/es-4-sarabande.mp3"],
    ["English Suite IV Menuet I", ""],
    ["", ""],

    ["French Suite IV Sarabande", "audio/fs-4-sarabande.mp3"],
    ["French Suite V Sarabande", "audio/fs-5-sarabande.mp3"],
    ["French Suite VI Allemande", "audio/fs-6-allemande.mp3"],
    ["French Suite VI Sarabande", "audio/fs-6-sarabande.mp3"],
    ["French Suite VI Gavotte", "audio/fs-6-gavotte.mp3"],
    ["French Suite VI Polonaise", ""],
    ["French Suite VI Menuet", ""],
    ["French Suite VI Gigue", "audio/fs-6-gigue.mp3"],
    ["", ""],

    ["Two-Part Inventions 1", ""],
    ["Two-Part Inventions 8", ""]
]

function makeMusicTable() {
    var table = $("<table/>").addClass('CSSTableGenerator');
    $.each(musicData, function(rowIndex, r) {
        var row = $("<tr/>");
        row.append($("<td/>").text(r[0]));
        if (r[1] != "") {
            row.append($('<td><audio src="' + r[1] + '" controls></audio></td>'));
        }
       table.append(row);
    });
    $("#music-data-div").append(table);
}

makeMusicTable();