# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'images_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumb_small', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('thumb_large', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('extension', self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=2048, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'images', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'images_image')


    models = {
        u'images.image': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'Image'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'thumb_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'thumb_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'unique_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['images']