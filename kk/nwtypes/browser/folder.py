from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class IsotopeView(BrowserView):
    """ isotope view """
    __call__ = ViewPageTemplateFile('templates/isotope.pt')
    
    def getContents(self, is_topic = False):
       return self.contents("Project", is_topic)
       
    def contents(self, portal_type, is_topic = False):
        # todo sort by custom index
        results = []
        if not is_topic:
            results = self.context.portal_catalog(portal_type=portal_type, path = {"query":"/".join(self.context.getPhysicalPath()), "depth":10}, sort_on="getProjectPosition", sort_order="descending")
        else: 
            contentFilter = self.request.get("contentFilter", None)
            contentFilter = contentFilter and dict(contentFilter) or {}
            results = self.context.queryCatalog(batch=False, **contentFilter)
        return results
        
class IsotopeOffersView(IsotopeView):
    """ isotope view """
    
    def getContents(self, is_topic = False):
       return self.contents("SpecialOffer", is_topic)

class ContactListView(BrowserView):
    """ contact list """
    __call__ = ViewPageTemplateFile('templates/contactlist.pt')
    
    def getContents(self, is_topic = False):
        results = self.context.portal_catalog(portal_type="Contact", path = {"query":"/".join(self.context.getPhysicalPath()), "depth":10}, sort_on="getObjPositionInParent", sort_order="ascending")
        return results