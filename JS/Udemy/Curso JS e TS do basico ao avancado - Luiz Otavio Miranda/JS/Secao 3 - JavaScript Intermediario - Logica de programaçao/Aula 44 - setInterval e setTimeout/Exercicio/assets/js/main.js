const timer = document.querySelector('.timer p');
let seconds = 0;
let time;

function getTimeFromSeconds(seconds) {
    const date = new Date(seconds * 1000)
    return date.toLocaleTimeString('pt-BR', {
        hour12: false,
        timeZone: 'GMT'
    });
}

function startCount() {
    if (timer.style.color === 'black') {
        seconds = 0;
        clearInterval(time);
    }
    time = setInterval(function () {
        timer.style.color = 'black';
        timer.innerHTML = getTimeFromSeconds(seconds);
        seconds++;
    }, 1000);
}

function pauseCount() {
    clearInterval(time);
    timer.style.color = 'red';
}

function stopCount() {
    clearInterval(time);
    timer.style.color = 'black';
    timer.innerHTML = getTimeFromSeconds(0)
    seconds = 0;
}

document.addEventListener('click', function(event) {
    const element = event.target;

    if(element.classList.contains('start')) {
        startCount();
    }

    if(element.classList.contains('pause')) {
        pauseCount();
    }

    if(element.classList.contains('stop')) {
        stopCount();
    }
})