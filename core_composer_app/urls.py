""" Url router for the composer application
"""
from django.conf.urls import url, include
from core_composer_app.views.user import views as user_views, ajax as user_ajax

urlpatterns = [
    url(r'^$', user_views.index,
        name='core_composer_index'),
    url(r'^build-template/(?P<template_id>\w+)$', user_views.build_template,
        name='core_composer_build_template'),
    url(r'^download-xsd$', user_views.download_xsd,
        name='core_composer_download_xsd'),

    url(r'^change-xsd-type$', user_ajax.change_xsd_type,
        name='core_composer_change_xsd_type'),
    url(r'^change-root-type-name$', user_ajax.change_root_type_name,
        name='core_composer_change_root_type_name'),
    url(r'^insert-element-sequence$', user_ajax.insert_element_sequence,
        name='core_composer_insert_element_sequence'),
    url(r'^rename-element$', user_ajax.rename_element,
        name='core_composer_rename_element'),
    url(r'^delete-element$', user_ajax.delete_element,
        name='core_composer_delete_element'),
    url(r'^get-element-occurrences$', user_ajax.get_element_occurrences,
        name='core_composer_get_element_occurrences'),
    url(r'^set-element-occurrences$', user_ajax.set_element_occurrences,
        name='core_composer_set_element_occurrences'),
    url(r'^save-template$', user_ajax.save_template,
        name='core_composer_save_template'),
    url(r'^save-type$', user_ajax.save_type,
        name='core_composer_save_type'),

    url(r'^rest/', include('core_composer_app.rest.urls')),
]