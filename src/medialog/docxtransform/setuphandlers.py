# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from Products.CMFCore.utils import getToolByName
from plone import api

# Imports to try to find out whyt it fails
from importlib import import_module
from logging import DEBUG
from logging import ERROR
from Products.PortalTransforms.libtransforms.utils import MissingBinary
from Products.PortalTransforms.utils import log



@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "medialog.docxtransform:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["medialog.docxtransform.upgrades"]


def post_install(context):
    """Post install script"""
    # Registering our transform at the end of the installation of this package.
    site = api.portal.get()
    
    # Adding our file types to Mime Type Registry
    mtr = getToolByName(site, 'mimetypes_registry')
    
    import pdb; pdb.set_trace()
    mtr.mimetypes()
    # if not mtr.lookup('application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
    #         mtr.manage_addMimeType(
    #             id = "Office Word 2007 XML document",
    #             mimetypes = ('application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
    #             extensions = None,
    #             icon_path = "word.png",
    #             binary=1,
    #         )
    
    transforms_tool = getToolByName(site, 'portal_transforms')
    if 'word_docx_to_text' not in transforms_tool.objectIds():
        # Not already installed
        transforms_tool.manage_addTransform('word_docx_to_text', 'medialog.docxtransform.transform')
        
 

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    # Is there any reason to uninstall mimetypes?
    site =  api.portal.get() 
    transforms_tool = getToolByName(site, 'portal_transforms')    
    if 'word_docx_to_text' in transforms_tool.objectIds():        
         transforms_tool.unregisterTransform('word_docx_to_text')
         
    # Removing our types from MTR
    # mtr = getToolByName(site, 'mimetypes_registry')
    # mtr.manage_delObjects('application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    





  