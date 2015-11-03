// TODO: this should be one file just with some distiction about how iframe look slike for 
function FileSubmit(ContentType, ObjectID, Link, Width, Height) {

    // var input_id=window.name.split("___").join(".");
    var input_id=window.name.replace(/____/g,'-').split("___").join(".");
    var preview_id = 'preview_' + input_id;
    var previewiframe_id = 'preview_iframe_' + input_id;
    input = opener.document.getElementById(input_id);
    preview = opener.document.getElementById(preview_id);
    previewiframe = opener.document.getElementById(previewiframe_id)

    // set new value for input field
    var object_identification = ContentType + ':' + ObjectID;
    input.value = object_identification;

    // display iframe, with youtube it might happend we only deliver
    // link + width + height and all other values
    // however for all other normal iframes we deliver entire iframe so we don't need to construct anything like that

    if (Link.indexOf("<iframe") == 0) {
        var iframe_code = Link;
        previewiframe.innerHTML = iframe_code;
        previewiframe.getElementsByTagName('iframe')[0].setAttribute('width', Width);
        previewiframe.getElementsByTagName('iframe')[0].setAttribute('height', Height);
    } else {
        var iframe_code = '<iframe width="{{ Width }}" height="{{ Height }}" src="{{ link }}" type="text/html" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen scrolling="no"></iframe>';
        iframe_code = iframe_code.replace('{{ link }}', Link);
        iframe_code = iframe_code.replace('{{ Width }}', Width);
        iframe_code = iframe_code.replace('{{ Height }}', Height);
        previewiframe.innerHTML = iframe_code;
    }

    preview.setAttribute("style", "display:none");
    previewiframe.setAttribute("style", "display:block");

    this.close();
}

