# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Quote.relo_company'
        db.alter_column(u'quotes_quote', 'relo_company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Relo_Company'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Quote.relo_company'
        raise RuntimeError("Cannot reverse this migration. 'Quote.relo_company' and its values cannot be restored.")

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
            'cust_company': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
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
            'other_company': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'other_contact': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'other_email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'blank': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pet_notes': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'pets': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prc': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'prc_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prc_appvd_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'referral_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'relo_company': ('django.db.models.fields.related.ForeignKey', [], {'db_index': 'False', 'to': u"orm['contacts.Relo_Company']", 'null': 'True', 'blank': 'True'}),
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