
REQUEST=context.REQUEST

from Products.CMFPlone.utils import transaction_note
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from ZODB.POSException import ConflictError

state_success = "success"
state_failure = "failure"

plone_utils = getToolByName(context, 'plone_utils')
urltool = getToolByName(context, 'portal_url')
portal = urltool.getPortalObject()
url = urltool()

## make these arguments?
name = context.REQUEST.get('name', None)
phone = context.REQUEST.get('phone', None)
street = context.REQUEST.get('street', None)
email = context.REQUEST.get('email', None)
plzort = context.REQUEST.get('plzort', None)
betreff = context.REQUEST.get('betreff', None)
message = context.REQUEST.get('message', None)
chks = context.REQUEST.get("chk[]", [])

send_to_address = context.getEmail()
envelope_from = portal.getProperty('email_from_address')

state.set(status=state_success) ## until proven otherwise

host = context.MailHost # plone_utils.getMailHost() (is private)
encoding = portal.getProperty('email_charset')

chks_dict = context.getInfDict()
infs = []
for i in chks_dict:
   if i[0] in chks:
       infs.append(i[1])
variables = {'email' : email,
             'name'     : name,	
             'phone':phone,
             'street':street, 
             'plzort':plzort, 
             'betreff':betreff, 
             'message'             : message, 
             'infs':infs
             }

try:
    message = context.team_contact_template(context, **variables)
    message = message.encode(encoding)
    result = host.send(message, send_to_address, envelope_from,
                       subject=_(u'New message'), charset=encoding)
except ConflictError:
    raise
except: # TODO Too many things could possibly go wrong. So we catch all.
    exception = plone_utils.exceptionString()
    message = _(u'Unable to send mail: ${exception}',
                mapping={u'exception' : exception})
    plone_utils.addPortalMessage(message, 'error')
    return state.set(status=state_failure)

## clear request variables so form is cleared as well
REQUEST.set('phone', None)
REQUEST.set('name', None)
REQUEST.set('street', None)
REQUEST.set('email', None)
REQUEST.set('plzort', None)
REQUEST.set('betreff', None)
REQUEST.set('message', None)
REQUEST.set('chk[]', [])

plone_utils.addPortalMessage(_(u'Mail sent.'))
return state