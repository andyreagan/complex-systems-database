# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.department'
        db.delete_column(u'cmplxsys_person', 'department')

        # Deleting field 'Person.affiliation'
        db.delete_column(u'cmplxsys_person', 'affiliation')

        # Deleting field 'Person.position'
        db.delete_column(u'cmplxsys_person', 'position')

        # Adding field 'Person.institution'
        db.add_column(u'cmplxsys_person', 'institution',
                      self.gf('django.db.models.fields.CharField')(default='University of Vermont', max_length=200),
                      keep_default=False)

        # Adding field 'Person.affiliation0'
        db.add_column(u'cmplxsys_person', 'affiliation0',
                      self.gf('django.db.models.fields.CharField')(default='Department of Mathematics and Statistics', max_length=200),
                      keep_default=False)

        # Adding field 'Person.role0'
        db.add_column(u'cmplxsys_person', 'role0',
                      self.gf('django.db.models.fields.CharField')(default='Professor', max_length=200),
                      keep_default=False)

        # Adding field 'Person.affiliation1'
        db.add_column(u'cmplxsys_person', 'affiliation1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.role1'
        db.add_column(u'cmplxsys_person', 'role1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.affiliation2'
        db.add_column(u'cmplxsys_person', 'affiliation2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.role2'
        db.add_column(u'cmplxsys_person', 'role2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.affiliation3'
        db.add_column(u'cmplxsys_person', 'affiliation3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.role3'
        db.add_column(u'cmplxsys_person', 'role3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.affiliation4'
        db.add_column(u'cmplxsys_person', 'affiliation4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.role4'
        db.add_column(u'cmplxsys_person', 'role4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryaffiliation0'
        db.add_column(u'cmplxsys_person', 'secondaryaffiliation0',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryrole0'
        db.add_column(u'cmplxsys_person', 'secondaryrole0',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryaffiliation1'
        db.add_column(u'cmplxsys_person', 'secondaryaffiliation1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryrole1'
        db.add_column(u'cmplxsys_person', 'secondaryrole1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryaffiliation2'
        db.add_column(u'cmplxsys_person', 'secondaryaffiliation2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryrole2'
        db.add_column(u'cmplxsys_person', 'secondaryrole2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryaffiliation3'
        db.add_column(u'cmplxsys_person', 'secondaryaffiliation3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryrole3'
        db.add_column(u'cmplxsys_person', 'secondaryrole3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryaffiliation4'
        db.add_column(u'cmplxsys_person', 'secondaryaffiliation4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.secondaryrole4'
        db.add_column(u'cmplxsys_person', 'secondaryrole4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Person.department'
        db.add_column(u'cmplxsys_person', 'department',
                      self.gf('django.db.models.fields.CharField')(default='Mathematics and Statistics', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.affiliation'
        db.add_column(u'cmplxsys_person', 'affiliation',
                      self.gf('django.db.models.fields.CharField')(default='University of Vermont', max_length=200),
                      keep_default=False)

        # Adding field 'Person.position'
        db.add_column(u'cmplxsys_person', 'position',
                      self.gf('django.db.models.fields.CharField')(default='Professor', max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Person.institution'
        db.delete_column(u'cmplxsys_person', 'institution')

        # Deleting field 'Person.affiliation0'
        db.delete_column(u'cmplxsys_person', 'affiliation0')

        # Deleting field 'Person.role0'
        db.delete_column(u'cmplxsys_person', 'role0')

        # Deleting field 'Person.affiliation1'
        db.delete_column(u'cmplxsys_person', 'affiliation1')

        # Deleting field 'Person.role1'
        db.delete_column(u'cmplxsys_person', 'role1')

        # Deleting field 'Person.affiliation2'
        db.delete_column(u'cmplxsys_person', 'affiliation2')

        # Deleting field 'Person.role2'
        db.delete_column(u'cmplxsys_person', 'role2')

        # Deleting field 'Person.affiliation3'
        db.delete_column(u'cmplxsys_person', 'affiliation3')

        # Deleting field 'Person.role3'
        db.delete_column(u'cmplxsys_person', 'role3')

        # Deleting field 'Person.affiliation4'
        db.delete_column(u'cmplxsys_person', 'affiliation4')

        # Deleting field 'Person.role4'
        db.delete_column(u'cmplxsys_person', 'role4')

        # Deleting field 'Person.secondaryaffiliation0'
        db.delete_column(u'cmplxsys_person', 'secondaryaffiliation0')

        # Deleting field 'Person.secondaryrole0'
        db.delete_column(u'cmplxsys_person', 'secondaryrole0')

        # Deleting field 'Person.secondaryaffiliation1'
        db.delete_column(u'cmplxsys_person', 'secondaryaffiliation1')

        # Deleting field 'Person.secondaryrole1'
        db.delete_column(u'cmplxsys_person', 'secondaryrole1')

        # Deleting field 'Person.secondaryaffiliation2'
        db.delete_column(u'cmplxsys_person', 'secondaryaffiliation2')

        # Deleting field 'Person.secondaryrole2'
        db.delete_column(u'cmplxsys_person', 'secondaryrole2')

        # Deleting field 'Person.secondaryaffiliation3'
        db.delete_column(u'cmplxsys_person', 'secondaryaffiliation3')

        # Deleting field 'Person.secondaryrole3'
        db.delete_column(u'cmplxsys_person', 'secondaryrole3')

        # Deleting field 'Person.secondaryaffiliation4'
        db.delete_column(u'cmplxsys_person', 'secondaryaffiliation4')

        # Deleting field 'Person.secondaryrole4'
        db.delete_column(u'cmplxsys_person', 'secondaryrole4')


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
        u'cmplxsys.paper': {
            'Meta': {'object_name': 'Paper'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': "'There are none.'"}),
            'arxiv': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivpw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'symmetrical': 'False'}),
            'bibref': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fromclass': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'googlescholarlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journalpagelink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'onlineappendices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'preprintlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'supplementarylink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'timescited': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titlelink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'cmplxsys.person': {
            'Meta': {'ordering': "('uname',)", 'object_name': 'Person'},
            'affiliation0': ('django.db.models.fields.CharField', [], {'default': "'Department of Mathematics and Statistics'", 'max_length': '200'}),
            'affiliation1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'affiliation4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'bitbucket': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'default': "'University of Vermont'", 'max_length': '200'}),
            'last': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'middle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'plus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
        u'cmplxsys.press': {
            'Meta': {'object_name': 'Press'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Earth shattering project.'", 'max_length': '500'})
        }
    }

    complete_apps = ['cmplxsys']