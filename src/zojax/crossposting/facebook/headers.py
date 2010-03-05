import simplejson

from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL

from zojax.resourcepackage.library import includeInplaceSource

from zojax.principal.facebook.interfaces import IFacebookAuthenticationProduct

script = """
    <script type="text/javascript">
    $(document).ready(function() {
        $.fn.crossposting.services.facebook.api_key = %(key)s;
        $.fn.crossposting.services.facebook.channel_path = %(channel)s;
        })
    </script>
"""

class Headers(object):
    

    def update(self):
        super(Headers, self).update()
        self.product = getUtility(IFacebookAuthenticationProduct)
    
    def render(self):
        product = self.product
        key = self.product.apiKey
        channel = '%s/xd_receiver.htm'%absoluteURL(getSite(), self.request)
        includeInplaceSource(script % dict(key=simplejson.dumps(key), channel=simplejson.dumps(channel)), ('zojax-crossposting',))
        return super(Headers, self).render()
