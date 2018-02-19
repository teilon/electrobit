
$('.autoplay').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 3000,
});

$(document).on('ready', function() {
    $(".item-cards-slick__cards").slick({
      dots: true,
      infinite: true,
      centerMode: true,
      slidesToShow: 5,
      slidesToScroll: 3
    });
});

//$(window).load(function() {
//    $('.item-cards-slick__cards').on('setPosition', function () {
//      $(this).find('.slick-slide').height('auto');
//      var slickTrack = $(this).find('.slick-track');
//      var slickTrackHeight = $(slickTrack).height();
//
//      $(this).find('.slick-slide').css('height', slickTrackHeight + 'px');
//    });
//})