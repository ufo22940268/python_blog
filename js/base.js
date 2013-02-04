var xmlReq;

function isRequestReady() {
    return xmlReq.status == 200 && xmlReq.readyState == 4;
}

function openBlog(blogName) {
    xmlReq.open("GET", "blog/" + blogName + ".html", true);
}

function loadContent(type) {
    if (window.XMLHttpRequest) {
        xmlReq = new XMLHttpRequest();
    }

    xmlReq.onreadystatechange = function () {
        if (xmlReq.status == 200 && xmlReq.readyState == 4) {
            document.getElementById("content").innerHTML = xmlReq.responseText;
        }
    };

    if (isBlogType(type)) {
        openBlog(type);
    } else {
        if (type == "about") {
            xmlReq.open("GET", "static/about.html", true);
        } else if (type == "content") {
            xmlReq.open("GET", "content.html", true);
        } else if (type == "tags") {
            xmlReq.open("GET", "static/tags.html", true);
        } else {
            alert("Invalid type.");
            return;
        }
    }
    xmlReq.send();
}

function isBlogType(type) {
    return !isNaN(type);
}

window.onload = loadContent("content");
