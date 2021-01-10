$(function() {
    // setTimeout() function will be fired after page is loaded
    // it will wait for 5 sec. and then will fire
    
    setTimeout(function() {
        $("#message").hide('blind', {}, 500)
    }, 5000);
});