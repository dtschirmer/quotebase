from django.contrib import admin
from quotebase.contacts.models import User, Agent, Partner, Relo_Company


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Partner)
admin.site.register(Relo_Company)

