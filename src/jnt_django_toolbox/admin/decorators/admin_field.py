# -*- coding: utf-8 -*-

from functools import wraps


def admin_field(short_description=None, allow_tags=True):
    """Decorator used for custom field or add link in
    the admin detail page.

    ``short_description (str)``
        Description of the field.
    ``allow_tags (bool)``
        Allow tags.

    The wrapped method receives the custom field.

    Usage::

        from jnt_admin_tools.decorators import admin_field
        from django.contrib import admin
        from django.utils.safestring import mark_safe
        from test_app.models import Bar

        @admin.register(Bar)
        class BarAdmin(admin.ModelAdmin):
            fields = ('name', 'foos', 'custom_field')
            readonly_fields = ('foos', 'custom_field')

            @admin_field('Custom field')
            def custom_field(self, obj):
                return mark_safe('<h1>custom field</h1>')

    .. image:: images/decorators/decorator_admin_field.png
    """

    def wrap(func):  # noqa: WPS430
        @wraps(func)
        def field_func(self, instance):  # noqa: WPS430
            return func(self, instance)

        field_func.short_description = short_description
        field_func.allow_tags = allow_tags
        return field_func

    return wrap