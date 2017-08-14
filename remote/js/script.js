$(document).ready(function () {

  var API_URL = 'https://fffc9d2160d9dc7a2e05df05317c0182.resindevice.io';

  function getInfo() {
    $.get(API_URL + '/info', function (data) {
      console.log(data);
      if (data.status) {
        $('.cpu-temperature').text(data.status[0] + '˚C');
        $('.cpu-usage').text(data.status[1] + '%');
        $('.ram-usage').text(data.status[2] + '%');
      }
    });
  }

  function getSensorsInfo() {
    $.get(API_URL + '/detect', function (data) {
      console.log(data);
      $('.front-sensor').text(Math.round(data.front) + ' cm');
      $('.left-sensor').text(Math.round(data.left) + ' cm');
      $('.right-sensor').text(Math.round(data.right) + ' cm');
      $('.back-sensor').text(Math.round(data.back) + ' cm');
    });
  }


  talk = function () {
    var text = $('#input-to-display').val();
    if (text && text.length) {
      $.post(API_URL + '/talk', {
        text: text,
      }, function (data) {
        console.log(data);
        if (data == 'OK') {
          Materialize.toast('DONE', 2000);
        }
      });
    }
  }

  printOnScreen = function () {
    var text = $('#input-to-display').val();
    if (text && text.length) {
      $.post(API_URL + '/print', {
        text: text,
        line: 2,
      }, function (data) {
        console.log(data);
        if (data == 'OK') {
          Materialize.toast('DONE', 2000);
        }
      });
    }
  }

  move = function (direction) {
    $.post(API_URL + '/move', {
      direction: direction,
      speed: 1,
    }, function (data) {
      console.log(data);
    });
  }

  stop = function () {
    $.post(API_URL + '/stop', function (data) {
      console.log(data);
    });
  }

  getInfo();
  setInterval(function () {
    getInfo();
  }, 10000);

  getSensorsInfo();
  setInterval(function () {
    getSensorsInfo();
  }, 2000);

  $('.camera').attr('src', API_URL + '/camera');

});
