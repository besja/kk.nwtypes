from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from kk.nwtypes.interfaces import IProjectCategory
from kk.nwtypes.config import PROJECTNAME

ProjectCategorySchema = folder.ATFolderSchema.copy()


class ProjectCategory(folder.ATFolder):
    """ category """
    implements(IProjectCategory)
    portal_type = meta_type = "ProjectCategory"
    schema = ProjectCategorySchema

atapi.registerType(ProjectCategory, PROJECTNAME)
