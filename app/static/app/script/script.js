
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

// FIXEDMENU
// =================================================
// Config
//      .header-menu .header_wrapper
// =================================================
//var $nav_header = $('.header-menu'),
//    header_menu_height = $('.header-menu').height(),
//    header_wrapper_height = $('.header_wrapper').height(),
//    offset_val     = header_wrapper_height - header_menu_height;
//// Method
//// =================================================
//function navSlide() {
//  var scroll_top = $(window).scrollTop();
//
//  $data_wrapper = $('.data-wrapper');
////  $product_menu = $('.product-menu')
//
////  $scroll_wrapper = $('.scroll-wrapper');
////  margin_property = header_menu_height + 'px';
////  $scroll_wrapper['margin-top'] = margin_property;
//
//  if (scroll_top >= offset_val) { // the detection!
//    $nav_header.addClass('is-sticky');
//    $data_wrapper.addClass('scroll-wrapper');
////    $nav_header.addClass('sticky-top');
//  } else {
//    $nav_header.removeClass('is-sticky');
//    $data_wrapper.removeClass('scroll-wrapper');
////    $nav_header.removeClass('sticky-top');
//  }
//}
//// Handler
//// =================================================
//$(window).scroll(navSlide);


//+++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++



// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var header_menu = document.getElementById("header-menu-id");
var data_wrapper = document.getElementById("content-id");

// Get the offset position of the navbar
var sticky = header_menu.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    header_menu.classList.add("is-sticky")
    data_wrapper.classList.add("content-wrapper")
  } else {
    header_menu.classList.remove("is-sticky");
    data_wrapper.classList.remove("content-wrapper")
  }
}


//+++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++

//// Create a clone of the menu, right next to original.
//$('.header-menu').addClass('original').clone().insertAfter('.header-menu').addClass('cloned').css('position','fixed').css('top','0').css('margin-top','0').css('z-index','500').removeClass('original').hide();
//
//scrollIntervalID = setInterval(stickIt, 10);
//
//
//function stickIt() {
//
//  var orgElementPos = $('.original').offset();
//  orgElementTop = orgElementPos.top;
//
//  if ($(window).scrollTop() >= (orgElementTop)) {
//    // scrolled past the original position; now only show the cloned, sticky element.
//
//    // Cloned element should always have same left position and width as original element.
//    orgElement = $('.original');
//    coordsOrgElement = orgElement.offset();
//    leftOrgElement = coordsOrgElement.left;
//    widthOrgElement = orgElement.css('width');
//    $('.cloned').css('left',leftOrgElement+'px').css('top',0).css('width',widthOrgElement).show();
//    $('.original').css('visibility','hidden');
//  } else {
//    // not scrolled past the menu; only show the original menu.
//    $('.cloned').hide();
//    $('.original').css('visibility','visible');
//  }
//}