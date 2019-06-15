var gulp        = require('gulp');
var bs          = require('browser-sync').create();

gulp.task('serve', [], () => {
        bs.init({
            server: {
               baseDir: "./",
            },
            port: 5000,
            reloadOnRestart: true,
            browser: "chrome"
        });
        gulp.watch('./**/*', ['', bs.reload]);
});