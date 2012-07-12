from zope.interface import Interface

class IProject(Interface):
    """ project """


class IProjectCategory(Interface):
    """ project category """

class ISpecialOffer(Interface):
    """ special offer """
class ISpecialOfferCategory(Interface):
    """ special offer category"""

class IContact(Interface):
    """ contact """
class IAddonInstalled(Interface):
    """A layer specific for this add-on product."""