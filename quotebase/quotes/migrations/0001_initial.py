# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotes_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('assigned', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lead_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lead_contact', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('coordinator', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('coord_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('coord_phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('relo_company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Relo_Company'], db_index=False, blank=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('cust_email', self.gf('django.db.models.fields.EmailField')(max_length=30, blank=True)),
            ('cust_phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('cust_company', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('other_contact', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('other_email', self.gf('django.db.models.fields.EmailField')(max_length=30, blank=True)),
            ('other_phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('other_company', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('o_city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('o_st_pr', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('o_country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('d_city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('d_st_pr', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('d_country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pets', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pet_notes', self.gf('django.db.models.fields.TextField')(max_length=100, blank=True)),
            ('total_costs', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('contingency', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('incentive', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('referral_fee', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('cc_fee', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('markup', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('total_quote', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('prc_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prc_appvd_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sent_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('convert_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('prc', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Quote'])

        # Adding model 'Cost'
        db.create_table(u'quotes_cost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Agent'])),
            ('estimated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reference.Currency'])),
            ('exchange_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3, blank=True)),
            ('service_point', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('airline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reference.Airline'], db_index=False)),
            ('o_airport', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('d_airport', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('af_cost', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('af_cost_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('af_fee', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('af_fee_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('ap_fee_customs', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('ap_fee_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('ap_cust_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('transportation', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('trans_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('trans_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('travel_kennel', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('tk_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('tk_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('vaccination', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('vcn_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('vcn_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('parasite', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('para_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('para_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('health_cert', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('hc_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('hc_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('hc_2', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('hc_2_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('hc_2_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('gov_endorse', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('gov_end_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('gov_end_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('postage', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('post_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('post_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('gov_permit', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('gov_perm_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('gov_perm_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('quarantine', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('q_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('q_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('boarding', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('board_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('board_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('other_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('other_cost', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('other_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('other_notes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('total_cost', self.gf('django.db.models.fields.IntegerField')(max_length=12, null=True, blank=True)),
            ('total_lcl', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Cost'])

        # Adding M2M table for field quotes on 'Cost'
        m2m_table_name = db.shorten_name(u'quotes_cost_quotes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cost', models.ForeignKey(orm[u'quotes.cost'], null=False)),
            ('quote', models.ForeignKey(orm[u'quotes.quote'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cost_id', 'quote_id'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotes_quote')

        # Deleting model 'Cost'
        db.delete_table(u'quotes_cost')

        # Removing M2M table for field quotes on 'Cost'
        db.delete_table(db.shorten_name(u'quotes_cost_quotes'))


    models = {
        u'contacts.agent': {
            'Meta': {'object_name': 'Agent'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'contacts.relo_company': {
            'Meta': {'object_name': 'Relo_Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quotes.cost': {
            'Meta': {'object_name': 'Cost'},
            'af_cost': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'af_cost_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'af_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'af_fee_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Agent']"}),
            'airline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reference.Airline']", 'db_index': 'False'}),
            'ap_cust_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ap_fee_customs': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ap_fee_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'board_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'board_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'boarding': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reference.Currency']"}),
            'd_airport': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'estimated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exchange_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'gov_end_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'gov_end_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gov_endorse': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'gov_perm_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'gov_perm_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gov_permit': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hc_2': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hc_2_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hc_2_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'hc_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hc_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'health_cert': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'o_airport': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'other_cost': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'other_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'other_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'other_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'para_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'para_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'parasite': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'post_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'post_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postage': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'q_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'q_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'quarantine': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'quotes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quotes.Quote']", 'symmetrical': 'False'}),
            'service_point': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'tk_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tk_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'total_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'trans_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'trans_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'transportation': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'travel_kennel': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'vaccination': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'vcn_lcl': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'vcn_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'assigned': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cc_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'contingency': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'convert_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'coord_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'coord_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'coordinator': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cust_company': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cust_email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'blank': 'True'}),
            'cust_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'd_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'd_country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'd_st_pr': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incentive': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'lead_contact': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'lead_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'markup': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'o_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'o_country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'o_st_pr': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'other_company': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_contact': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'other_email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'blank': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pet_notes': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'pets': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prc': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'prc_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prc_appvd_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'referral_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'relo_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Relo_Company']", 'db_index': 'False', 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'total_costs': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_quote': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['quotes']