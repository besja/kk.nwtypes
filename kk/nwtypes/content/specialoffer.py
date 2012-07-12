from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import image, document
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.nwtypes.interfaces import ISpecialOffer
from kk.nwtypes.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent
documentSchema = document.ATDocumentSchema.copy()
documentSchema['text'].primary = False
SpecialOfferSchema =  documentSchema + image.ATImageSchema.copy() + Schema((

	StringField("projectPosition", 
	vocabulary=[(str(i), str(i)) for i in range(0, 100)], 
	default = 0, 
	widget = SelectionWidget(label="position"), 
	)
))

class SpecialOffer(document.ATDocument):
    """ special offer """
    
    implements(ISpecialOffer)
    portal_type=meta_type="SpecialOffer"
    schema = SpecialOfferSchema
    
    def getProjectPositionIndex(self):
        return int(self.getProjectPosition())
    def getProjectIcon(self, scale):
        return self.tag(scale=scale)
    def getProjectFilter(self):
        return self.aq_parent.getId()
        
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

       
        
registerType(SpecialOffer, PROJECTNAME)