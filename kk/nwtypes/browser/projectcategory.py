from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ProjectCategoryView(BrowserView):
    """ project category view """
    __call__ = ViewPageTemplateFile('templates/projectcategory.pt')
    

class SOCategoryView(BrowserView):
    """ special offer category """
    __call__ = ViewPageTemplateFile('templates/socategory.pt')       