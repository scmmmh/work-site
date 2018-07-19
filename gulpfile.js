'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var clean_css = require('gulp-clean-css');
var babel = require('gulp-babel');
var uglify = require('gulp-uglify');
var pump = require('pump');

gulp.task('default', ['css']);

gulp.task('css', function(cb) {
    pump([
        gulp.src('theme/src/app.scss'),
        sass({
            includePaths: ['node_modules/foundation-sites/scss']
        }),
        clean_css(),
        gulp.dest('theme/static/css')
    ], cb);
});

gulp.task('watch', ['default'], function(cb) {
    gulp.watch('theme/src/**/*.scss', ['css']);
});
