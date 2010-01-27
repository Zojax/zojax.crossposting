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

    $.fn.crossposting = function(settings) {
			
			settings = $.extend({
				textInputId: "",
                titleInputId: "",
                descriptionInputId: "",
                formId: "",
                buttonId: "",
                text: '',
                title: '',
                description: '',
                url: '',
                confirmMessage: 'Your comment please'
			}, settings);
			

			var textInput = settings.textInputId ? $('#'+settings.textInputId):false;
			var titleInput = settings.titleInputId ? $('#'+settings.titleInputId):false;
			var descriptionInput = settings.descriptionInputId ? $('#'+settings.descriptionInputId):false;
			var button = settings.buttonId ? $('#'+settings.buttonId):false;
			var form = settings.formId ? $('#'+settings.formId):false;
			
            var cnt = $.fn.crossposting.services.length;
            if (cnt == 0)
                return;
			function click_callback() {
			    cnt -= 1
			    if (cnt <= 0) {
			        button.click()
			    }
			}
			button.one('click', function(){
			        settings.title = settings.title || (titleInput ? titleInput.val():'');
		            settings.description = settings.description || (descriptionInput ? descriptionInput.val():'');
		            settings.text = settings.text || (textInput ? textInput.val():'');

			        for (i = 0; i < cnt; i++) {
    	                var plugin = $.fn.crossposting.services[i];
    	                plugin({text:settings.text, 
    	                        title:settings.title, 
    	                        description: settings.description,
    	                        url: settings.url,
    	                        confirmMessage: settings.confirmMessage,
    	                        callback: click_callback})
    	            }
    	            return false;
			    });
			
	    };
	    
	$.fn.crossposting.services = [];
	
})(jQuery);