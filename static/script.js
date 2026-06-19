function toggleDarkMode(){

document.body.classList.toggle("dark");

}

let time = 15;

let timer = setInterval(function(){

document.getElementById("timer").innerHTML = time;

time--;

if(time < 0){

clearInterval(timer);

alert("Time Up!");

}

},1000);