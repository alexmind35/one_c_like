var scrolled;
window.onscroll = function() {
    scrolled = window.pageYOffset || document.documentElement.scrollTop;
    if ($( document ).width() > 280 && scrolled > 200){
        $(".header-one .menu-wrapper, .header-two .menu-wrapper").css({"background": "#2f3b73"})
    }
    if(200 > scrolled){
        $(".header-one .menu-wrapper, .header-two .menu-wrapper").css({"background": "none"})         
    }

}
