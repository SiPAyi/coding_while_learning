let namasteBtn = document.querySelector('button');
namasteBtn.addEventListener(click,showMsg);

function showMsg(){
    alert("Namathe world!");
    namasteBtn.textContent = 'changed aa';
}