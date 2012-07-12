from Products.CMFPlone import PloneMessageFactory as _
plone_utils=context.plone_utils

name = context.REQUEST.get('name', None)
phone = context.REQUEST.get('phone', None)
street = context.REQUEST.get('street', None)
email = context.REQUEST.get('email', None)
plzort = context.REQUEST.get('plzort', None)
betreff = context.REQUEST.get('betreff', None)
email_ok = False
if not name:
   state.setError('name', _(u'Please enter your name'), new_status='failure')
   
if not phone:
   state.setError('phone', _(u'Please enter your phone'), new_status='failure')
   
if not street:
   state.setError('street', _(u'Please enter your street'), new_status='failure')

if not plzort:
   state.setError('plzort', _(u'Please enter plzort'), new_status='failure')

if not betreff:
   state.setError('betreff', _(u'Please enter betreff'), new_status='failure')
      
if not email:
   state.setError('email',_(u'Please submit an email address.'), new_status='failure')

else:
   if not plone_utils.validateSingleEmailAddress(email):
       state.setError('email', _(u'Please submit a valid email address.'), new_status='failure')     
         
if state.getErrors():
   context.plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'), 'error')
   
return state