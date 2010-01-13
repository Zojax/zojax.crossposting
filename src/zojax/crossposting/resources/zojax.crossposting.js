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
                formId: "",
                buttonId: "",
                title: '',
                description: '',
                url: ''
			}, settings);
			

			var textInput = settings.textInputId ? $('#'+settings.textInputId):false;
			var titleInput = settings.titleInputId ? $('#'+settings.titleInputId):false;
			var button = settings.buttonId ? $('#'+settings.buttonId):false;
			var form = settings.formId ? $('#'+settings.formId):false;
			
			var cnt = $.fn.crossposting.services.length
			
			function click_callback() {
			    cnt -= 1
			    if (cnt <= 0) {
			        button.click()
			    }
			}
			button.one('click', function(){
			    var text = textInput.val();
			            for (i = 0; i < $.fn.crossposting.services.length; i++) {
			                var plugin = $.fn.crossposting.services[i];
			                plugin({text:text, 
			                        title:settings.title, 
			                        description: settings.description,
			                        url: settings.url,
			                        callback: click_callback})
			            }
			            return false;
			    });
			
	    };
	    
	$.fn.crossposting.services = [];
	
})(jQuery);