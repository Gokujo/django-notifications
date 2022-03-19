''' Django notifications apps file '''
# -*- coding: utf-8 -*-
from django.apps import AppConfig
try:
    from django.utils.translation import gettext_lazy as _
except TypeError: # Django 4.x
    from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = "notifications"
    verbose_name = _("Notifications")

    def ready(self):
        super(Config, self).ready()
        # this is for backwards compability
        import notifications.signals
        notifications.notify = notifications.signals.notify