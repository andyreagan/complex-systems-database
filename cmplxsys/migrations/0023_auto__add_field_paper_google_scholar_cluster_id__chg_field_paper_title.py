# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paper.google_scholar_cluster_id'
        db.add_column(u'cmplxsys_paper', 'google_scholar_cluster_id',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Paper.titlelink'
        db.alter_column(u'cmplxsys_paper', 'titlelink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):
        # Deleting field 'Paper.google_scholar_cluster_id'
        db.delete_column(u'cmplxsys_paper', 'google_scholar_cluster_id')


        # Changing field 'Paper.titlelink'
        db.alter_column(u'cmplxsys_paper', 'titlelink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'cmplxsys.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagelink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'nextoffering': ('django.db.models.fields.DateTimeField', [], {}),
            'numtimesoffered': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'shortcode': ('django.db.models.fields.CharField', [], {'default': "'CSYS 500.'", 'max_length': '500'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'courses_taught'", 'blank': 'True', 'to': u"orm['cmplxsys.Person']"}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses_taken'", 'symmetrical': 'False', 'to': u"orm['cmplxsys.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Learn all the things.'", 'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.uvm.edu/~bagrow'", 'max_length': '2000'})
        },
        u'cmplxsys.funding': {
            'Meta': {'object_name': 'Funding'},
            'enddate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longdescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Project']", 'symmetrical': 'False', 'blank': 'True'}),
            'shortdescription': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'100M Award.'", 'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.nsf.gov'", 'max_length': '2000'})
        },
        u'cmplxsys.order': {
            'Meta': {'object_name': 'Order'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmplxsys.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'paper': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmplxsys.Paper']"})
        },
        u'cmplxsys.paper': {
            'HTMLabstract': ('django.db.models.fields.TextField', [], {'default': "'There are none.<br>'"}),
            'Meta': {'object_name': 'Paper'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': "'There are none.'"}),
            'arxiv': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivpw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'author_list_sorted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'through': u"orm['cmplxsys.Order']", 'symmetrical': 'False'}),
            'bibref': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fromclass': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'google_scholar_cluster_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'googlescholarlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'papers/blank.png'", 'max_length': '100'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journalpagelink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'onlineappendices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'preprintlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sort_date': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'supplementarylink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'timescited': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titlelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1950'})
        },
        u'cmplxsys.person': {
            'Meta': {'ordering': "('uname',)", 'object_name': 'Person'},
            'affiliation0': ('django.db.models.fields.CharField', [], {'default': "'Department of Mathematics and Statistics'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arxiv': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'associated_faculty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bitbucket': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'collaborator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'core_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'core_team_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'people/blank.png'", 'max_length': '100'}),
            'instagram': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'default': "'University of Vermont'", 'max_length': '200'}),
            'last': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'middle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'orcid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '19', 'null': 'True', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'plus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'researchgate': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role0': ('django.db.models.fields.CharField', [], {'default': "'Professor'", 'max_length': '200'}),
            'role1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'scholar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryaffiliation0': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryaffiliation1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryaffiliation2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryaffiliation3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryaffiliation4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryrole0': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryrole1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryrole2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryrole3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secondaryrole4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stackoverflow': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'strava': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sur': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'uname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vine': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'cmplxsys.position': {
            'Meta': {'object_name': 'Position'},
            'endyear': ('django.db.models.fields.CharField', [], {'default': "'Current'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmplxsys.Person']"}),
            'startyear': ('django.db.models.fields.CharField', [], {'default': "'2015'", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'PHD'", 'max_length': '4'})
        },
        u'cmplxsys.press': {
            'Meta': {'object_name': 'Press'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'press/blank.png'", 'max_length': '100'}),
            'imagelink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'papers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Paper']", 'symmetrical': 'False', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Project']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'UVM Researcher catapaults into fame.'", 'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.nytimes.com'", 'max_length': '2000'})
        },
        u'cmplxsys.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'project/blank.png'", 'max_length': '100'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Earth shattering project.'", 'max_length': '500'})
        }
    }

    complete_apps = ['cmplxsys']