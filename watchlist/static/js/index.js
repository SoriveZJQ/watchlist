function init() {
    var formfile = document.getElementsByClassName("file");
    var formfilename = document.getElementsByClassName("filename");
    var submit = document.getElementsByClassName("submit")[0];
    var result = document.getElementsByClassName("result")[0];
    formfile[0].addEventListener("change", function () {
        formfilename[0].value = formfile[0].files[0].name;
    });
    submit.addEventListener("click", function (event) {
        result.placeholder = "";
        Response.redirect('index');
    });
}

window.onload = init;
