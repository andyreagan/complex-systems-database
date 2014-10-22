# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'cmplxsys_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(default='University of Vermont', max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(default='Professor', max_length=200, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(default='Mathematics and Statistics', max_length=200, null=True, blank=True)),
            ('blurb', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('middle', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('last', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('sur', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('webpage', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('strava', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('youtube', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('vine', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('instagram', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('scholar', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('bitbucket', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('stackoverflow', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('plus', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('pinterest', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Person'])

        # Adding model 'Project'
        db.create_table(u'cmplxsys_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Earth shattering project.', max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Project'])

        # Adding M2M table for field people on 'Project'
        m2m_table_name = db.shorten_name(u'cmplxsys_project_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'cmplxsys.project'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'person_id'])

        # Adding model 'Funding'
        db.create_table(u'cmplxsys_funding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='100M Award.', max_length=500)),
            ('url', self.gf('django.db.models.fields.CharField')(default='http://www.nsf.gov', max_length=2000)),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('enddate', self.gf('django.db.models.fields.DateTimeField')()),
            ('shortdescription', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('longdescription', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Funding'])

        # Adding M2M table for field project on 'Funding'
        m2m_table_name = db.shorten_name(u'cmplxsys_funding_project')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('funding', models.ForeignKey(orm[u'cmplxsys.funding'], null=False)),
            ('project', models.ForeignKey(orm[u'cmplxsys.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['funding_id', 'project_id'])

        # Adding M2M table for field people on 'Funding'
        m2m_table_name = db.shorten_name(u'cmplxsys_funding_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('funding', models.ForeignKey(orm[u'cmplxsys.funding'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['funding_id', 'person_id'])

        # Adding model 'Course'
        db.create_table(u'cmplxsys_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shortcode', self.gf('django.db.models.fields.CharField')(default='CSYS 500.', max_length=500)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Learn all the things.', max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=2000)),
            ('logline', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
            ('url', self.gf('django.db.models.fields.CharField')(default='http://www.uvm.edu/~bagrow', max_length=2000)),
            ('nextoffering', self.gf('django.db.models.fields.DateTimeField')()),
            ('numtimesoffered', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('imagelink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Course'])

        # Adding M2M table for field students on 'Course'
        m2m_table_name = db.shorten_name(u'cmplxsys_course_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'cmplxsys.course'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'person_id'])

        # Adding M2M table for field teachers on 'Course'
        m2m_table_name = db.shorten_name(u'cmplxsys_course_teachers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'cmplxsys.course'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'person_id'])

        # Adding model 'Paper'
        db.create_table(u'cmplxsys_paper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('logline', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(default='There are none.')),
            ('img', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('arxiv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('arxivpw', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('googlescholarlink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('preprintlink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('supplementarylink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('onlineappendices', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('journalpagelink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('arxivlink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('titlelink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('bibref', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('timescited', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Paper'])

        # Adding M2M table for field authors on 'Paper'
        m2m_table_name = db.shorten_name(u'cmplxsys_paper_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'cmplxsys.paper'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paper_id', 'person_id'])

        # Adding M2M table for field fromclass on 'Paper'
        m2m_table_name = db.shorten_name(u'cmplxsys_paper_fromclass')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'cmplxsys.paper'], null=False)),
            ('course', models.ForeignKey(orm[u'cmplxsys.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paper_id', 'course_id'])

        # Adding model 'Press'
        db.create_table(u'cmplxsys_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='UVM Researcher catapaults into fame.', max_length=500)),
            ('url', self.gf('django.db.models.fields.CharField')(default='http://www.nytimes.com', max_length=2000)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('imagelink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Press'])

        # Adding M2M table for field papers on 'Press'
        m2m_table_name = db.shorten_name(u'cmplxsys_press_papers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('press', models.ForeignKey(orm[u'cmplxsys.press'], null=False)),
            ('paper', models.ForeignKey(orm[u'cmplxsys.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['press_id', 'paper_id'])

        # Adding M2M table for field projects on 'Press'
        m2m_table_name = db.shorten_name(u'cmplxsys_press_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('press', models.ForeignKey(orm[u'cmplxsys.press'], null=False)),
            ('project', models.ForeignKey(orm[u'cmplxsys.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['press_id', 'project_id'])

        # Adding M2M table for field people on 'Press'
        m2m_table_name = db.shorten_name(u'cmplxsys_press_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('press', models.ForeignKey(orm[u'cmplxsys.press'], null=False)),
            ('person', models.ForeignKey(orm[u'cmplxsys.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['press_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'cmplxsys_person')

        # Deleting model 'Project'
        db.delete_table(u'cmplxsys_project')

        # Removing M2M table for field people on 'Project'
        db.delete_table(db.shorten_name(u'cmplxsys_project_people'))

        # Deleting model 'Funding'
        db.delete_table(u'cmplxsys_funding')

        # Removing M2M table for field project on 'Funding'
        db.delete_table(db.shorten_name(u'cmplxsys_funding_project'))

        # Removing M2M table for field people on 'Funding'
        db.delete_table(db.shorten_name(u'cmplxsys_funding_people'))

        # Deleting model 'Course'
        db.delete_table(u'cmplxsys_course')

        # Removing M2M table for field students on 'Course'
        db.delete_table(db.shorten_name(u'cmplxsys_course_students'))

        # Removing M2M table for field teachers on 'Course'
        db.delete_table(db.shorten_name(u'cmplxsys_course_teachers'))

        # Deleting model 'Paper'
        db.delete_table(u'cmplxsys_paper')

        # Removing M2M table for field authors on 'Paper'
        db.delete_table(db.shorten_name(u'cmplxsys_paper_authors'))

        # Removing M2M table for field fromclass on 'Paper'
        db.delete_table(db.shorten_name(u'cmplxsys_paper_fromclass'))

        # Deleting model 'Press'
        db.delete_table(u'cmplxsys_press')

        # Removing M2M table for field papers on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_papers'))

        # Removing M2M table for field projects on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_projects'))

        # Removing M2M table for field people on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_people'))


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
            'affiliation': ('django.db.models.fields.CharField', [], {'default': "'University of Vermont'", 'max_length': '200'}),
            'bitbucket': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'default': "'Mathematics and Statistics'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'middle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'plus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'Professor'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'scholar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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