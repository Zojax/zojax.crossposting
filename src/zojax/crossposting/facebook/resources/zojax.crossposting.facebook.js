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

    $.fn.crossposting.services.facebook = function(params) {
        if (!$('#zojax-crossposting-facebook-post').val())
            return params.callback()
        FB_RequireFeatures(["Api"], function(){ 
                FB.Facebook.init($.fn.crossposting.services.facebook.api_key, $.fn.crossposting.services.facebook.channel_path);
                var attachment = {'name':params.title,'href': params.url,'description': params.description}
                function stream_callback (post_id, exception) {
                    if (post_id != 'null') {
                        params.callback(post_id)
                    }
                  }
                FB.Connect.streamPublish(params.text, attachment, null, null,
                                         'Confirm your comment please',
                                         stream_callback);
            })

    };
    
    $.fn.crossposting.services.push($.fn.crossposting.services.facebook)
	
})(jQuery);