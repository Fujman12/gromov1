$(function() {
	$(".owl-carousel").owlCarousel({
		items:1,
		loop:true,
		nav:true,
		dot:true,
		autoplay:true,
		autoHeight:true
	});

	$(document).ready(function() {
		$('.test-popup').magnificPopup({
			delegate: 'a',
			type: 'image',
			tLoading: 'Loading image #%curr%...',
			mainClass: 'mfp-img-mobile',
			closeBtnInside: false,
			titleSrc: 'title',
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
				titleSrc: function(item) {
					return item.el.attr('title') + '<small>Gromov Model Management</small>';
				}
			}
		});
	});
	$(".test-popup a:first").addClass("test-popup-link-right").text('>');
	$(".test-popup a:last").addClass("test-popup-link-left").text('<');
});

