$(document).ready(function () {

  var API_URL = 'https://fffc9d2160d9dc7a2e05df05317c0182.resindevice.io';

  var loading = false;

  function showLoading() {
    loading = true;
    $('.loading').removeClass('hide');
  }

  function hideLoading() {
    loading = false;
    $('.loading').addClass('hide');
  }

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

  guess = function () {
    if (!loading) {
      showLoading();
      $.get(API_URL + '/guess', function (data) {
        hideLoading();
        console.log(data);
        Materialize.toast(data.guess, 2000);
      });
    }
  };

  talk = function () {
    var text = $('#input-to-display').val();
    if (text && text.length && !loading) {
      showLoading();
      $.post(API_URL + '/talk', {
        text: text,
      }, function (data) {
        hideLoading();
        console.log(data);
        if (data == 'OK') {
          Materialize.toast('DONE', 2000);
        }
      });
    }
  };

  printOnScreen = function () {
    var text = $('#input-to-display').val();
    if (text && text.length && !loading) {
      showLoading();
      $.post(API_URL + '/print', {
        text: text,
        line: 1,
      }, function (data) {
        hideLoading();
        console.log(data);
        if (data == 'OK') {
          Materialize.toast('DONE', 2000);
        }
      });
    }
  };

  move = function (direction) {
    $('#auto-pilot').prop('checked', false);
    $.post(API_URL + '/move', {
      direction: direction,
      speed: 1,
    }, function (data) {
      console.log(data);
    });
  };

  stop = function () {
    $('#auto-pilot').prop('checked', false);
    $.post(API_URL + '/stop', {}, function (data) {
      console.log(data);
    });
  };

  setAutoPilot = function () {
    $.post(API_URL + '/pilot', {
      auto_pilot: $('#auto-pilot').prop('checked') ? 1 : 0
    }, function (data) {
      console.log(data);
    });
  };

  getInfo();
  setInterval(function () {
    getInfo();
  }, 10000);

  getSensorsInfo();
  setInterval(function () {
    getSensorsInfo();
  }, 5000);

  initTouchEvents = function (id, direction) {
    var el = document.getElementById(id);
    el.addEventListener("touchstart", function () {
      move(direction);
    }, false);
    el.addEventListener("touchend", function () {
      stop();
    }, false);
  }
  initTouchEvents('forward-btn', 'forward');
  initTouchEvents('rotate-left-btn', 'rotate_left');
  initTouchEvents('rotate-right-btn', 'rotate_right');
  initTouchEvents('backward-btn', 'backward');

  var socket = io.connect(API_URL + ':5000');
  socket.on('connect', function() {
    console.log('connected to websockets server')
    socket.emit('my event', {data: 'I\'m connected!'});
  });

});
