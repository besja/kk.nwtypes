from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content import image, document
from kk.nwtypes.interfaces import ISpecialOffer
from kk.nwtypes.config import PROJECTNAME


imgSchema = image.ATImageSchema.copy()
documentSchema = document.ATDocumentSchema.copy()
documentSchema['text'].primary = False
SpecialOfferSchema = documentSchema + imgSchema + atapi.Schema((

    atapi.StringField(
        "projectPosition",
        vocabulary=[(str(i), str(i)) for i in range(0, 100)],
        default=0,
        widget=atapi.SelectionWidget(
            label="position"),
    )
))


class SpecialOffer(document.ATDocument):
    """ special offer """
    implements(ISpecialOffer)
    portal_type = meta_type = "SpecialOffer"
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

atapi.registerType(SpecialOffer, PROJECTNAME)
