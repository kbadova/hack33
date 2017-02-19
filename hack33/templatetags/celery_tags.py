import datetime
from django import template
from hack33.celery import app
register = template.Library()


@app.task
def display_time():
    return datetime.datetime.now()


@register.simple_tag
def display_different_messages_with_celery():
    kk = display_time.delay()
    return kk.result
