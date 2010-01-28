/*
 * Crossposting 1.0 - jQuery plugin implements simple crossposting
 * 
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
 *
 * Revision: $Id: jquery.treeview.js 4684 2008-02-07 19:08:06Z joern.zaefferer $
 *
 */

;(function($) {

    $.fn.crossposting.services.twitter = function(params) {
        if (!$('#zojax-crossposting-twitter-post').attr('checked'))
            return params.callback()
        if (!$.fn.crossposting.services.twitter.logged_in) {
            var url = 'http://twitter.com/home?status=' + encodeURIComponent(params.text + ' | ' + params.title + ' ' + params.description + '(' +params.url + ')');
            $.fn.crossposting.services.twitter.spawn_modal_and_wait(url, params.callback)
        }
    };
    
    $.fn.crossposting.services.twitter.modal_window = null;

    $.fn.crossposting.services.twitter.spawn_modal_and_wait = function (url, callback) {
        $.fn.crossposting.services.twitter.modal_window = window.open(url, '_blank', 'height=600,width=800,left=300,top=200,resizable=yes', true);
        var intervalId = setInterval("$.fn.crossposting.services.twitter.waitForWindow()", 500);

        $.fn.crossposting.services.twitter.waitForWindow = function() {
            if ($.fn.crossposting.services.twitter.modal_window.closed) {
                //window.location.href=$('#redirect_url_div').innerHTML;
                clearInterval(intervalId);
                callback();
            }
        }
    };
    
    $.fn.crossposting.services.push($.fn.crossposting.services.twitter);
    
})(jQuery);