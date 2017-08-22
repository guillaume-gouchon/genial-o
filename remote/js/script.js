$(document).ready(function () {

  var API_URL = 'https://fffc9d2160d9dc7a2e05df05317c0182.resindevice.io';

  var loading = false;

  showLoading();
  window.socket = io.connect(API_URL);
  socket.on('connect', function() {
    console.log('connected to websockets server')
    hideLoading();
  });

  function showLoading() {
    loading = true;
    $('.loading').removeClass('hide');
  }

  function hideLoading() {
    loading = false;
    $('.loading').addClass('hide');
  }

  socket.on('info', function(data) {
    console.log('info response =', data);
    if (data.status) {
      $('.cpu-temperature').text(data.status[0] + '˚C');
      $('.cpu-usage').text(data.status[1] + '%');
      $('.ram-usage').text(data.status[2] + '%');

      $('.front-sensor').text(Math.round(data.front) + ' cm');
      $('.left-sensor').text(Math.round(data.left) + ' cm');
      $('.right-sensor').text(Math.round(data.right) + ' cm');
      $('.back-sensor').text(Math.round(data.back) + ' cm');
    }
  });

  socket.on('guess', function(data) {
    console.log('guess response =', data);
    Materialize.toast(data.guess, 5000);
  });

  move = function (direction) {
    $('#auto-pilot').prop('checked', false);
    socket.emit('move', {
      direction: direction,
      speed: 1,
    });
  };

  stop = function () {
    $('#auto-pilot').prop('checked', false);
    socket.emit('stop', {});
  };

  guess = function () {
    socket.emit('guess', {});
    Materialize.toast('Guessing...', 5000);
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

  setAutoPilot = function () {
    $.post(API_URL + '/pilot', {
      auto_pilot: $('#auto-pilot').prop('checked') ? 1 : 0
    }, function (data) {
      console.log(data);
      Materialize.toast('DONE', 2000);
    });
  };

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

});
