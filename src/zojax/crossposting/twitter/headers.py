import simplejson

from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL

from zojax.resourcepackage.library import includeInplaceSource

from zojax.principal.twitter.interfaces import ITwitterAuthenticationProduct

script = """
    <script type="text/javascript">
    $(document).ready(function() {
        $.fn.crossposting.services.twitter.consumer_key = %(key)s;
        $.fn.crossposting.services.twitter.consumer_secret = %(secret)s;
        $.fn.crossposting.services.twitter.logged_in = %(logged_in)s;
        })
    </script>
"""

class Headers(object):

    def render(self):
        product = getUtility(ITwitterAuthenticationProduct)
        key = product.consumerKey
        secret = product.consumerSecret
        logged_in = False
        includeInplaceSource(script % dict(key=key, secret=secret, \
                                           logged_in=simplejson.dumps(logged_in)), ('zojax-crossposting',))
        return super(Headers, self).render()
