var xmlReq;
function loadXml() {
    if (window.XMLHttpRequest) {
        xmlReq = new XMLHttpRequest();
    }

    xmlReq.onreadystatechange = function() {
        if (isRequestReady()) {
            document.getElementById("content").innerHTML = xmlReq.responseText;
        }
    }

    xmlReq.open("GET", "k.txt", true);
    xmlReq.send();
}

function isRequestReady() {
    return xmlReq.readyState == 4 && xmlReq.status == 200;
}
