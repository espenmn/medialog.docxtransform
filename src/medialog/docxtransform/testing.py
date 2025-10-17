# -*- coding: utf-8 -*-
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)

import medialog.docxtransform


class MedialogDocxtransformLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.docxtransform)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.docxtransform:default')


MEDIALOG_DOCXTRANSFORM_FIXTURE = MedialogDocxtransformLayer()


MEDIALOG_DOCXTRANSFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_DOCXTRANSFORM_FIXTURE,),
    name='MedialogDocxtransformLayer:IntegrationTesting',
)


MEDIALOG_DOCXTRANSFORM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_DOCXTRANSFORM_FIXTURE,),
    name='MedialogDocxtransformLayer:FunctionalTesting',
)
