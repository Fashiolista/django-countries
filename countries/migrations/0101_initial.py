# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'countries_country', (
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('name_official', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sort_priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'countries', ['Country'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'countries_country')


    models = {
        u'countries.country': {
            'Meta': {'ordering': "('-sort_priority', 'name')", 'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_official': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sort_priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['countries']