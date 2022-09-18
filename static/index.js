const but1 = document.getElementById("but1");
const but2 = document.getElementById("but2");

but1.addEventListener("mouseover",blue);
but1.addEventListener("mouseout",black);
but2.addEventListener("mouseover",blu);
but2.addEventListener("mouseout",blac);

function blue(){
    but1.style.backgroundColor = "aqua";
    but1.style.color = "white";
}
function black(){
    but1.style.backgroundColor = "white";
    but1.style.color = "black";
}

function blu(){
    but2.style.backgroundColor = "aqua";
    but2.style.color = "white";
}
function blac(){
    but2.style.backgroundColor = "white";
    but2.style.color = "black";
}
