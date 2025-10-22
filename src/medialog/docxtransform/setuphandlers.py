# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from Products.CMFCore.utils import getToolByName
from plone import api
import mimetypes
from importlib import import_module

from . import config


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
    
    transforms_tool = getToolByName(site, 'portal_transforms')
    if config.TRANSFORM_NAME not in transforms_tool.objectIds():
        # Not already installed
        transforms_tool.manage_addTransform(config.TRANSFORM_NAME, 'medialog.docxtransform.transform')


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    site =  api.portal.get() 
    transforms_tool = getToolByName(site, 'portal_transforms')    
    if config.TRANSFORM_NAME in transforms_tool.objectIds():        
        transforms_tool.unregisterTransform(config.TRANSFORM_NAME)
 


  