$(document).ready(function() {
    // Create a function to open and close navMenu on mobile
    $("#navMenu").on('click', function() {
        var navItems = $("#navItems");
        if (navItems.hasClass("hide-small")) {
            navItems.removeClass("hide-small");
            navItems.addClass("show").fadeIn(200);
        } else {
            navItems.removeClass("show");
            navItems.addClass("hide-small").fadeOut(200);
        }
    });

    // Change style of navbar on scroll
    window.onscroll = function() { navBar(); };
    function navBar() {
	    var navBar = document.getElementById("navBar");
	    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
		navBar.className = "bar" + " card" + " animate-top" + " stormy";
	    }
	    else {
		    navBar.className = navBar.className.replace(" card animate-top stormy", "");
	    }
    }

    // Change xdjskaly logo auto
    var myIndex = 0;
    carousel();
    function carousel() {
        var i;
        var x = document.getElementsByClassName("xdjLogo");
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        myIndex++;
        if (myIndex > x.length) {myIndex = 1}
        x[myIndex-1].style.display = "inline-block";
        setTimeout(carousel, 9000);
    }

    // Add smooth scroll to llinks
    $("a").on('click', function(event) {
	    if (this.hash !== "") {
		    event.preventDefault();
		    var hash = this.hash;
		    $('html, body').animate({
			    scrollTop: $(hash).offset().top
		    }, 1000, function() {
			    window.location.hash = hash;
		    });
	    }
    });

    // Displays text above button when hovered
    if (matchMedia) {
        var mq = window.matchMedia("(min-width: 992px)");
        mq.addListener(WidthChange);
        WidthChange(mq);
    }

    function WidthChange(mq) {
        if (mq.matches) {
            $("[data-role='beats-target']").hide();

            $("[data-role='scroll-to-beats']").mouseenter(function(){
        	    $("[data-role='beats-target']").fadeIn(300);
            });

            $("[data-role='scroll-to-beats']").mouseleave(function(){
        	    $("[data-role='beats-target']").fadeOut(200);
            });
        } else {
            $("[data-role='beats-target']").show();
        }
    }

    // Back to home button
    $("#scrollup").hide();

    $(window).scroll(function(){
	    if ($(window).scrollTop() > 300) {
		    $("#scrollup").fadeIn(300)
		    .addClass("animate-right");
	    } else {
		    $("#scrollup").fadeOut(300);
	    }
    });

});
