from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL

from zojax.resourcepackage.library import includeInplaceSource

from zojax.principal.facebook.interfaces import IFacebookAuthenticationProduct

script = """
    <script type="text/javascript">
    $(document).ready(function() {
        $.fn.crossposting.services.facebook.api_key = '%(key)s';
        $.fn.crossposting.services.facebook.channel_path = '%(channel)s';
        })
    </script>
"""

class Headers(object):

    def render(self):
        key = getUtility(IFacebookAuthenticationProduct).apiKey
        channel = '%s/xd_receiver.htm'%absoluteURL(getSite(), self.request)
        includeInplaceSource(script % dict(key=key, channel=channel), ('zojax-crossposting',))
        return super(Headers, self).render()
