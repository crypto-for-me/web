window.addEventListener('load', function() {
    menu = document.getElementById('menu');
    links = document.getElementById('links');

    menu.onclick = function() {
        menu.classList.toggle('active');
        links.classList.toggle('open');
    }

    links.onclick = function() {
        menu.classList.remove('active');
        links.classList.remove('open');
    }
});
