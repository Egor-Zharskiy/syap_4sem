document.addEventListener('DOMContentLoaded', function() {
    const dartboard = document.getElementById('dartboard');
    const dart = document.getElementById('dart');

    // Установим начальные координаты в центре доски
    const initialX = dartboard.offsetWidth / 2 - dart.offsetWidth / 2;
    const initialY = dartboard.offsetHeight / 2 - dart.offsetHeight / 2;

    dart.style.left = `${initialX}px`;
    dart.style.top = `${initialY}px`;

    dartboard.addEventListener('click', function(event) {
        const x = event.clientX - dartboard.getBoundingClientRect().left;
        const y = event.clientY - dartboard.getBoundingClientRect().top;

        dart.style.left = `${x - dart.offsetWidth / 2}px`;
        dart.style.top = `${y - dart.offsetHeight / 2}px`;
    });
});
