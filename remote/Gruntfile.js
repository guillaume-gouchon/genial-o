'use strict';

module.exports = function (grunt) {

  require('load-grunt-tasks')(grunt);

  grunt.initConfig({
    favicons: {
      options: {
        androidHomescreen: true,
        trueColor: true,
        precomposed: true,
        coast: true,
        windowsTile: true,
        tileBlackWhite: false,
        tileColor: 'auto',
        html: 'index.html',
        HTMLPrefix: 'images/icons/',
      },
      target: {
        src: 'images/icon.png',
        dest: 'images/icons'
      },
    },
  });

};
