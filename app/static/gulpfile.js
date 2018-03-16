var gulp = 			require('gulp'),
	sass =			require('gulp-sass'),
	browserSync =	require('browser-sync');


gulp.task('sass', function(){
	return gulp.src('src/sass/**/*.sass')
	.pipe(sass())
	.pipe(gulp.dest('app/css'))
	.pipe(browserSync.reload({stream: true}))
})

gulp.task('browser-sync', function(){
	browserSync({
		server:{
			baseDir: '../templates/app'
		},
		notify: false
	});
});

gulp.task('watch', ['sass'], function(){
	gulp.watch('src/sass/**/*.sass', ['sass']);
})

gulp.task('default', ['watch']);