window.onload = () => {
    document.getElementById("navBurger").addEventListener('click', () => {
        document.getElementById("navBurger").classList.toggle('is-active');
        document.getElementById("navMenu").classList.toggle('is-active');
    });
}