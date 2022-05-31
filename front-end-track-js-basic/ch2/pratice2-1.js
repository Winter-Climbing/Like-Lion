const animal = document.getElementsByTagName('li');

animal.lion.style.color = 'red'; // ||
document.getElementsByTagName('li')[0].style.color = 'red';

document.getElementsByClassName('animal')[2].style.color = 'green';

document.querySelectorAll('.animal').style.color = 'blue';

document.querySelectorAll('.animal')[2].innerHTML = 'dog';

document.querySelectorAll('.box')[0].classList.add('purple');
document.querySelectorAll('.box')[0].classList.remove('purple');

document.querySelectorAll('.box')[0].classList.toggle('yellow');