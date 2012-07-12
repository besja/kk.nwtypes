from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ProjectView(BrowserView):
    """ project view """
    __call__ = ViewPageTemplateFile('templates/project.pt')

         