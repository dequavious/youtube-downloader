function disable() {
    document.getElementById('c_btn').disabled = true;
    document.getElementById("status").style.visibility = "visible";
}

function disable_downloads(itag) {
    document.getElementById("btn_" + itag).innerHTML =
    "<svg class=\"inline-block align-middle w-4 h-4 text-gray-100 animate-spin dark:text-gray-300 fill-gray-300 dark:fill-gray-200\" viewBox=\"0 0 100 101\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">\n" +
    "    <path d=\"M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z\" fill=\"currentColor\"/>\n" +
    "    <path d=\"M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z\" fill=\"currentFill\"/>\n" +
    "</svg>";
    $(':button').prop('disabled', true);
}

function enable_downloads(itag) {
    const btn_id = "btn_" + itag;
    const btn = document.getElementById(btn_id);
    btn.classList.add('downloaded');
    btn.classList.remove('hover:bg-slate-100');
    $(':button').prop('disabled', false);
    btn.innerHTML = "<svg class=\"inline-block align-middle h-4 w-4 text-green-400\"  viewBox=\"0 0 24 24\"  fill=\"none\"  stroke=\"currentColor\"  stroke-width=\"3\"  stroke-linecap=\"round\"  stroke-linejoin=\"round\">  <polyline points=\"20 6 9 17 4 12\" /></svg>";
    document.querySelectorAll('button.downloaded').forEach(elem => {
        elem.disabled = true;
    });
}

function error(itag) {
    const btn_id = "btn_" + itag;
    const btn = document.getElementById(btn_id);
    btn.classList.add('downloaded');
    btn.classList.remove('hover:bg-slate-100');
    $(':button').prop('disabled', false);
    btn.innerHTML = "<svg class=\"inline-block align-middle h-4 w-4 text-red-400\"  viewBox=\"0 0 24 24\"  fill=\"none\"  stroke=\"currentColor\"  stroke-width=\"2\"  stroke-linecap=\"round\"  stroke-linejoin=\"round\">  <line x1=\"18\" y1=\"6\" x2=\"6\" y2=\"18\" />  <line x1=\"6\" y1=\"6\" x2=\"18\" y2=\"18\" /></svg>";
    document.querySelectorAll('button.downloaded').forEach(elem => {
        elem.disabled = true;
    });
}

function start_download(url, filename, type, itag) {
    fetch(url)
    .then(response => {
        if (response.ok) {
            return response.blob();
        } else {
            return null;
        }
    }).then(data => {
        if (!data) {
            const error_div = document.getElementById('error_div');
            error_div.innerHTML =
                "<strong class=\"font-bold text-sm\">Error downloading stream.</strong>\n" +
                "   <span class=\"absolute top-0 bottom-0 right-0 px-4 py-3\">\n" +
                "   <svg onclick=\"hide()\" class=\"fill-current h-6 w-6 text-red-500\" role=\"button\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\"><title>Close</title><path d=\"M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z\"></path></svg>\n" +
                "</span>";
            error_div.style.visibility = 'visible';
            error(itag);
        } else {
            download(data, filename.replace(/[^a-zA-Z\d\s\\\[\]{}()<>?!|:;,/+=`~@#$%^&*'"._-]/g, ""), type);
            enable_downloads(itag);
        }
    }).catch(err => console.log(err));
}

function hide() {
    const error_div = document.getElementById('error_div');
    error_div.innerHTML = "";
    error_div.style.visibility = 'hidden';
    // setTimeout(function () {
    //     document.getElementById('error_div').style.visibility = 'hidden';
    // }, 3000);
}

