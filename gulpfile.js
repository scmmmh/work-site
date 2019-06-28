'use strict';

const gulp = require('gulp'),
      sass = require('gulp-sass'),
      clean_css = require('gulp-clean-css'),
      pump = require('pump');

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

gulp.task('default', gulp.parallel('css'));

gulp.task('watch', gulp.series('default', function(cb) {
    gulp.watch('theme/src/**/*.scss', gulp.parallel('css'));
}));
