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

    // selected file is an image and thumbnail is available:
    // display the preview-image (thumbnail)
    // link the preview-image to the original image

    var iframe_code = '<iframe width="{{ Width }}" height="{{ Height }}" src="{{ link }}" type="text/html" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen scrolling="no"></iframe>'
    iframe_code = iframe_code.replace('{{ link }}', Link)
    iframe_code = iframe_code.replace('{{ Width }}', Width)
    iframe_code = iframe_code.replace('{{ Height }}', Height)
    previewiframe.innerHTML = iframe_code;
    preview.setAttribute("style", "display:none");
    previewiframe.setAttribute("style", "display:block");

    this.close();
}

