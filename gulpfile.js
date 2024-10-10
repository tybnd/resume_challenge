const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass')); // For SCSS compilation

// Task to compile SCSS to CSS
gulp.task('sass', function() {
    return gulp.src('src/scss/**/*.scss') // Adjust the path as necessary
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('dist/css')); // Adjust the output directory as necessary
});

// Watch task
gulp.task('watch', function() {
    gulp.watch('src/scss/**/*.scss', gulp.series('sass')); // Adjust the path as necessary
});

// Default task
gulp.task('default', gulp.series('sass', 'watch'));
