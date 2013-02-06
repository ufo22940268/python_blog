var xmlReq;

function isRequestReady() {
    return xmlReq.status == 200 && xmlReq.readyState == 4;
}

function openBlog(blogUrl) {
    xmlReq.open("GET", blogUrl, true); }

function loadContent(type) {
    if (window.XMLHttpRequest) {
        xmlReq = new XMLHttpRequest();
    }

    xmlReq.onreadystatechange = function () {
        if (xmlReq.status == 200 && xmlReq.readyState == 4) {
            document.getElementById("content").innerHTML = xmlReq.responseText;
        }
    };

    if (type == "about") {
        xmlReq.open("GET", "static/about.html", true);
    } else if (type == "content") {
        xmlReq.open("GET", "content.html", true);
    } else if (type == "tags") {
        xmlReq.open("GET", "static/tags.html", true);
    } else {
        openBlog(type);
    }

    xmlReq.send();
}

function isBlogType(type) {
    return !isNaN(type);
}

window.onload = loadContent("content");
