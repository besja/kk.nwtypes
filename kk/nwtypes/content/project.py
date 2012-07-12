from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.nwtypes.interfaces import IProject
from kk.nwtypes.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent

ProjectSchema = folder.ATFolderSchema.copy() + document.ATDocumentSchema.copy() + Schema((

	StringField("projectPosition", 
	vocabulary=[(str(i), str(i)) for i in range(0, 100)], 
	default = 0, 
	widget = SelectionWidget(label="position"), 
	)
))

class Project(folder.ATFolder, document.ATDocument):
    """ folder with rich descrpition """
    
    implements(IProject)
    portal_type=meta_type="Project"
    schema = ProjectSchema
    
    def getProjectPositionIndex(self):
        return int(self.getProjectPosition())
    
    def getProjectIcon(self, scale):
        portal_catalog = getToolByName(self, "portal_catalog")
        results = portal_catalog(portal_type="Image", sort_on="getObjPositionInParent", path="/".join(self.getPhysicalPath()))
        if len(results):
           return results[0].getObject().tag(scale=scale)
        return ""
    def getProjectFilter(self):
        return self.aq_parent.getId()
        
        
registerType(Project, PROJECTNAME)