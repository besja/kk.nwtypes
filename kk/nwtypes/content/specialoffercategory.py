from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.nwtypes.interfaces import ISpecialOfferCategory
from kk.nwtypes.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf

SOCategorySchema = folder.ATFolderSchema.copy()
class SpecialOfferCategory(folder.ATFolder):
    """ category """
    
    implements(ISpecialOfferCategory)
    portal_type=meta_type="SpecialOfferCategory"
    schema = SOCategorySchema

registerType(SpecialOfferCategory, PROJECTNAME)