window.onload = function() {
    var ball = document.getElementById('ball');
    var footer = document.querySelector('.footer');
    var footerHeight = footer.offsetHeight;
    var ballWidth = ball.offsetWidth;
    var target = document.querySelector('.img');

    var isDragging = false;
    var isSecondClick = false;
    var offsetX, offsetY;

    var randomX = Math.random() * (window.innerWidth - ballWidth);

    ball.style.left = randomX + 'px';
    ball.style.bottom = footerHeight + 'px';

    ball.addEventListener('mousedown', function(event) {
        isDragging = true;
        offsetX = event.clientX - ball.offsetLeft;
        offsetY = event.clientY - ball.offsetTop;
    });

    document.addEventListener('mousemove', function(event) {
        if (isDragging && !isSecondClick) {
            var x = event.clientX - offsetX;
            var y = event.clientY - offsetY;
            y = Math.min(Math.max(y, 0), window.innerHeight);

            ball.style.left = x + 'px';
            ball.style.bottom = y + 'px';
        }
    });

    document.addEventListener('mouseup', function() {
        if (!isSecondClick) {
            isDragging = false;
            animate();
        }
    });

    function animate() {
        ball.classList.add('throw-animation');
        setTimeout(() => {
            checkHit();
            ball.classList.remove('throw-animation');
        }, 1000); // Увеличиваем время анимации, чтобы анимация была завершена, когда шарик достигнет верхней точки движения
    }


    function checkHit() {
        var ballRect = ball.getBoundingClientRect();
        var targetRect = target.getBoundingClientRect();

        var targetCenterX = targetRect.left + targetRect.width / 2;
        var targetCenterY = targetRect.top + targetRect.height / 2;

        var distance = Math.sqrt(Math.pow(ballRect.left + ballRect.width / 2 - targetCenterX, 2) +
            Math.pow(ballRect.top + ballRect.height / 2 - targetCenterY, 2));

        if (distance <= 200) {
            var randomNumber = Math.floor(Math.random() * 100);
            if (randomNumber <= 80) {
                alert("Попадание!");
            } else {
                alert("Промах!");
            }
        } else {
            alert("Промах!");
        }

        ball.style.left = randomX + 'px';
        ball.style.bottom = footerHeight + 'px';
    }
};
