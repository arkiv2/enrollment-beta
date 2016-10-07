<script>
    var navHeight = $('#main_navbar').offset().top;
    DoNotScroll(navHeight);
    $(window).bind('scroll', function() {DoNotScroll(navHeight);});

    function DoNotScroll(navHeight) {
        if (!$('#main_navbar').hasClass('navbar-fixed-bottom')) {
            if ($(window).scrollTop() > navHeight) {
                $('#main_navbar').addClass('navbar-fixed-top')
                $('body').css({'margin-top': $('#main_navbar').height()+'px'});
                if ($('#main_navbar').parent('div').hasClass('container')) $('#main_navbar').children('div').addClass('container').removeClass('container-fluid');
                else if ($('#main_navbar').parent('div').hasClass('container-fluid')) $('#main_navbar').children('div').addClass('container-fluid').removeClass('container');
            }
            else {
                $('#main_navbar').removeClass('navbar-fixed-top');
                $('#main_navbar').children('div').addClass('container-fluid').removeClass('container');
                $('body').css({'margin-top': ''});
            }
        }
    }
</script>

<script>
    $( window ).load(function() {
        $(document).on('click', '.navbar .dropdown-menu', function(e) {e.stopPropagation();})
    });
</script>

<script src="/static/js/modal/classie.js"></script>
<script src="/static/js/modal/modalEffects.js"></script>
<script src="/static/js/modal/modernizr.custom.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>