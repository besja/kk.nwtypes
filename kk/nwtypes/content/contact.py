from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import image, document
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content.base import ATCTContent
from kk.nwtypes.interfaces import IContact
from kk.nwtypes.config import PROJECTNAME, INFORMATION
from Products.ATContentTypes.configuration import zconf
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent
documentSchema = document.ATDocumentSchema.copy()
documentSchema['text'].primary = False

ContactSchema =  documentSchema + image.ATImageSchema.copy() + Schema((
	StringField("position", 
	widget = StringWidget(label="position"), ), 
	StringField("phone", 
	widget = StringWidget(label="phone"), ), 
	
	StringField("fax", 
	widget = StringWidget(label="fax"), ), 
	
	StringField("email", 
	required = True,
	widget = StringWidget(label="email"),), 

	StringField("information", 
		vocabulary = INFORMATION, 
		multiValued= True, 
		widget = MultiSelectionWidget(label="information"),)
		
))

class Contact(ATCTContent):
    """ contact """
    
    implements(IContact)
    portal_type=meta_type="Contact"
    schema = ContactSchema
    
        
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)
    def getInfDict(self):
        return INFORMATION
       
        
registerType(Contact, PROJECTNAME)