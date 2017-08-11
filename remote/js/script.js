$(document).ready(function () {

  var API_URL = 'https://fffc9d2160d9dc7a2e05df05317c0182.resindevice.io/';

  function getInfo() {
    $.get(API_URL + '/info', function (data) {
      console.log(data);
      if (data.status) {
        $('.cpu-temperature').text(data.status[0]);
        $('.cpu-usage').text(data.status[1]);
        $('.ram-usage').text(data.status[2]);
      }
    });
  }

  function getSensorsInfo() {
    $.get(API_URL + '/detect', function (data) {
      console.log(data);
      if (data.status) {
        $('.cpu-temperature').text(data.status[0]);
        $('.cpu-usage').text(data.status[1]);
        $('.ram-usage').text(data.status[2]);
      }
    });
  }

  function talk() {
    var text = $('#input-to-display').val();
    if (text && text.length) {
      $.post(API_URL + '/talk', {
        text: text,
      }, function (data) {
        console.log(data);
      });
    }
  }

  function print() {
    var text = $('#input-to-display').val();
    if (text && text.length) {
      $.post(API_URL + '/print', {
        text: text,
        line: 1,
      }, function (data) {
        console.log(data);
      });
    }
  }

  getInfo();
  setTimeout(function () {
    getInfo();
  }, 10000);

  getSensorsInfo();
  setTimeout(function () {
    getSensorsInfo();
  }, 10000);

});
