# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.is_meme'
        db.add_column(u'images_image', 'is_meme',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Image.source_image'
        db.add_column(u'images_image', 'source_image',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='related_memes', null=True, to=orm['images.Image']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.is_meme'
        db.delete_column(u'images_image', 'is_meme')

        # Deleting field 'Image.source_image'
        db.delete_column(u'images_image', 'source_image_id')


    models = {
        u'images.image': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'Image'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_meme': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'source_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related_memes'", 'null': 'True', 'to': u"orm['images.Image']"}),
            'thumb_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'thumb_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'unique_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['images']