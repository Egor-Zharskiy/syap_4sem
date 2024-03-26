const circle = document.querySelector('.progress-ring__circle');
const r = circle.r.baseVal.value;
const circumference = 2 * Math.PI * r;
const input = document.querySelector('.percente');

circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = circumference;

function setProgress(percent) {
    const offset = circumference - percent / 100 * circumference;
    circle.style.strokeDashoffset = offset;
}

setProgress(20);

input.addEventListener('input', function () {
    setProgress(input.value);
});