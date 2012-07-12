
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Acquisition import aq_base, aq_inner
from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope.formlib import form
from zope.interface import implements, Interface
from zope import schema
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from AccessControl import getSecurityManager

from zope.component import getMultiAdapter, getUtility


class IContactPortlet(IPortletDataProvider):
    """A portlet to show contact
    """
    name = schema.ASCIILine(title=_(u'Name'),
                            description=_(u'Name.'),
                            required=True)

    target_contact = schema.Choice(
        title=_(u"Contact"),
        description=_(u"Select contact"),
        required=True,
        source=SearchableTextSourceBinder(
            {'portal_type': 'Contact'},
            default_query='path:'))

    
class ContactAssignment(base.Assignment):
    implements(IContactPortlet)
    title = _(u'Contact')

    name = u""
    target_contact = None

    def __init__(self, name=u"", target_contact=None):
        self.name = name


class ContactRenderer(base.Renderer):
   
    def __init__(self, context, request, view, manager, data):

        base.Renderer.__init__(self, context, request, view, manager, data)

        self.properties = getToolByName(context, 'portal_properties').navtree_properties
        self.urltool = getToolByName(context, 'portal_url')

    def title(self):
        return self.data.target_contact.Title()


    @memoize
    def contact(self):
        contact_path = self.data.target_contact
        if not contact_path:
            return None

        if contact_path.startswith('/'):
            contact_path = contact_path[1:]

        if not contact_path:
            return None

        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        portal = portal_state.portal()
        if isinstance(contact_path, unicode):
            # restrictedTraverse accepts only strings
            contact_path = str(contact_path)
        result = portal.unrestrictedTraverse(contact_path, default=None)
        
        if result is not None:
            sm = getSecurityManager()
            if not sm.checkPermission('View', result):
                result = None
        if result.portal_type == "Contact":
            return result
        else:
            return None


    def hasName(self):
        return self.data.name

    @property
    def available(self):
        if self.contact:
            return True
        return False

    def update(self):
        pass

    def render(self):

        return self._template()

    _template = ViewPageTemplateFile('templates/contact.pt')



class ContactAddForm(base.AddForm):
    form_fields = form.Fields(IContactPortlet)
    form_fields['target_contact'].custom_widget = UberSelectionWidget
    label = _(u"Add Contact Portlet")
    description = _(u"This portlet display a contact.")

    def create(self, data):

        return ContactAssignment(name=data.get('name', u""), target_contact=data.get('target_contact', u""))


class ContactEditForm(base.EditForm):
    form_fields = form.Fields(IContactPortlet)
    form_fields['target_contact'].custom_widget = UberSelectionWidget
    label = _(u"Edit Contact Portlet")
    description = _(u"This portlet display a contact.")
