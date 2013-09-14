# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Airline'
        db.create_table(u'reference_airline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'reference', ['Airline'])

        # Adding model 'Currency'
        db.create_table(u'reference_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'reference', ['Currency'])

        # Adding model 'Referral_Fee'
        db.create_table(u'reference_referral_fee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relo_company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Relo_Company'])),
            ('fee', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reference', ['Referral_Fee'])


    def backwards(self, orm):
        # Deleting model 'Airline'
        db.delete_table(u'reference_airline')

        # Deleting model 'Currency'
        db.delete_table(u'reference_currency')

        # Deleting model 'Referral_Fee'
        db.delete_table(u'reference_referral_fee')


    models = {
        u'contacts.relo_company': {
            'Meta': {'object_name': 'Relo_Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'reference.airline': {
            'Meta': {'object_name': 'Airline'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'reference.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'reference.referral_fee': {
            'Meta': {'object_name': 'Referral_Fee'},
            'fee': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'relo_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Relo_Company']"})
        }
    }

    complete_apps = ['reference']