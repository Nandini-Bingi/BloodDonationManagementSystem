const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function(){

    if(window.scrollY > 80){

        navbar.style.background="#8b0000";

    }

    else{

        navbar.style.background="rgba(0,0,0,.35)";

    }

});