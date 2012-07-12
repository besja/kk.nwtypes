from Products.CMFPlone import PloneMessageFactory as _
plone_utils=context.plone_utils

chks= context.REQUEST.get('chk[]', None)
if len(chks) < 2 :
    state.setError('info', _(u'Information is required'), new_status='failure')
if state.getErrors():
   context.plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'), 'error')
return state