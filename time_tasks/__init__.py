from __future__ import absolute_import, unicode_literals #ALLOWING "__future__ " simply ensures backward compatility with older django versions

from .celery import app as celery_app #THIS IS THE APP in celery.ini

__all__ = ('celery_app', )