from Acquisition import aq_inner
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from kk.nwtypes.utils import find_assignment_context

from kk.nwtypes import nwMessageFactory as _

from zope.i18nmessageid import MessageFactory
__ = MessageFactory("plone")


class IFilterNavigationPortlet(IPortletDataProvider):
    """ A portlet """


class Assignment(base.Assignment):
    """ Portlet assignment """

    implements(IFilterNavigationPortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        return _(u"Filter navigation")


class Renderer(base.Renderer):
    """ Portlet renderer """

    render = ViewPageTemplateFile('filternavigationportlet.pt')

    def root_info(self):
        context = aq_inner(self.context)
        actx = find_assignment_context(self.data, context)
        info = {}
        info['title'] = actx.Title()
        info['url'] = actx.absolute_url()
        return info

    def isRootLevel(self):
        context = aq_inner(self.context)
        actx = find_assignment_context(self.data, context)
        toplevel = False
        if context.getId() == actx.getId():
            toplevel = True
        return toplevel

    def is_current(self, itemid):
        context = aq_inner(self.context)
        context_id = context.getId()
        current = False
        if itemid == context_id:
            current = True
        return current

    def items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        assignment_context = find_assignment_context(self.data, self.context)
        folder_path = '/'.join(assignment_context.getPhysicalPath())
        brains = catalog(portal_types=['ProjectCategory',
                                       'SpecialOfferCategory'],
                         path={'query': folder_path,
                               'depth': 1},
                         sort_on='getObjPositionInParent')
        return brains


class AddForm(base.NullAddForm):
    """Portlet add form."""

    def create(self):
        return Assignment()
