from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from kk.nwtypes.interfaces import ISpecialOfferCategory
from kk.nwtypes.config import PROJECTNAME

SOCategorySchema = folder.ATFolderSchema.copy()


class SpecialOfferCategory(folder.ATFolder):
    """ category """
    implements(ISpecialOfferCategory)
    portal_type = meta_type = "SpecialOfferCategory"
    schema = SOCategorySchema

atapi.registerType(SpecialOfferCategory, PROJECTNAME)
