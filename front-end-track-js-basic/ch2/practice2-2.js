// document.querySelector('#btn').addEventListener('click', function () {

// })



let num = 0;

document.querySelector('#plus').addEventListener('click', function () {
  num++;
  document.querySelector('#num').innerHTML = num;
});

document.querySelector('#minus').addEventListener('click', function () {
  num--;
  document.querySelector('#num').innerHTML = num;
});



// document.querySelector('.bar').addEventListener('click', function () {
//   document.querySelector('.bar').innerHTML = '눌렸어!';
//   document.querySelector('.newBar').classList.toggle('show');
// });








