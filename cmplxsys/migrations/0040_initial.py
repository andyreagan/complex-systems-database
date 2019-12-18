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
            ('institution', self.gf('django.db.models.fields.CharField')(default='University of Vermont', max_length=200)),
            ('affiliation0', self.gf('django.db.models.fields.CharField')(default='Department of Mathematics and Statistics', max_length=200, null=True, blank=True)),
            ('role0', self.gf('django.db.models.fields.CharField')(default='Professor', max_length=200)),
            ('affiliation1', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('role1', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('affiliation2', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('role2', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('affiliation3', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('role3', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('affiliation4', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('role4', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryaffiliation0', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryrole0', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryaffiliation1', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryrole1', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryaffiliation2', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryrole2', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryaffiliation3', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryrole3', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryaffiliation4', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('secondaryrole4', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
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
            ('arxiv', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('researchgate', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('orcid', self.gf('django.db.models.fields.CharField')(default='', max_length=19, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='people/blank.png', max_length=100)),
            ('collaborator', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alumni', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('current_student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('post_doc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=400, null=True, blank=True)),
            ('core_team', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('core_team_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('associated_faculty', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmplxsys', ['Person'])

        # Adding model 'Position'
        db.create_table(u'cmplxsys_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='PHD', max_length=4)),
            ('startyear', self.gf('django.db.models.fields.CharField')(default='2015', max_length=10)),
            ('endyear', self.gf('django.db.models.fields.CharField')(default='Current', max_length=10)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmplxsys.Person'])),
        ))
        db.send_create_signal(u'cmplxsys', ['Position'])

        # Adding model 'Project'
        db.create_table(u'cmplxsys_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Earth shattering project.', max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='project/blank.png', max_length=100)),
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
            ('imagelink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
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
            ('HTMLabstract', self.gf('django.db.models.fields.TextField')(default='There are none.<br>')),
            ('img', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('arxiv', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('arxivpw', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(default='Preprint', max_length=200, null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('issue', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=1950)),
            ('sort_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('googlescholarlink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('preprintlink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('supplementarylink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('onlineappendices', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('journalpagelink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('arxivlink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('titlelink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('bibref', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('timescited', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('google_scholar_cluster_id', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('google_scholar_result_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('google_scholar_most_recent_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('google_scholar_raw_result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('DOI', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('PMID', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('ISSN', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('altmetric_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('author_list_sorted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='papers/blank.png', max_length=100)),
        ))
        db.send_create_signal(u'cmplxsys', ['Paper'])

        # Adding M2M table for field fromclass on 'Paper'
        m2m_table_name = db.shorten_name(u'cmplxsys_paper_fromclass')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'cmplxsys.paper'], null=False)),
            ('course', models.ForeignKey(orm[u'cmplxsys.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paper_id', 'course_id'])

        # Adding model 'Order'
        db.create_table(u'cmplxsys_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmplxsys.Person'])),
            ('paper', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmplxsys.Paper'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'cmplxsys', ['Order'])

        # Adding model 'Press'
        db.create_table(u'cmplxsys_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='UVM Researcher catapaults into fame.', max_length=500)),
            ('url', self.gf('django.db.models.fields.CharField')(default='http://www.nytimes.com', max_length=2000)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('favorite', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('imagelink', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='press/blank.png', max_length=100)),
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

        # Adding model 'Event'
        db.create_table(u'cmplxsys_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Life Changing Event', max_length=500)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.CharField')(default='Burlington, Vermont', max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(default='There are none.')),
            ('organizer_name', self.gf('django.db.models.fields.CharField')(default='Roboctopus', max_length=500)),
            ('organizer_email', self.gf('django.db.models.fields.EmailField')(max_length=500, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='events/blank.png', max_length=100)),
            ('event_page', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmplxsys', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'cmplxsys_person')

        # Deleting model 'Position'
        db.delete_table(u'cmplxsys_position')

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

        # Removing M2M table for field fromclass on 'Paper'
        db.delete_table(db.shorten_name(u'cmplxsys_paper_fromclass'))

        # Deleting model 'Order'
        db.delete_table(u'cmplxsys_order')

        # Deleting model 'Press'
        db.delete_table(u'cmplxsys_press')

        # Removing M2M table for field papers on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_papers'))

        # Removing M2M table for field projects on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_projects'))

        # Removing M2M table for field people on 'Press'
        db.delete_table(db.shorten_name(u'cmplxsys_press_people'))

        # Deleting model 'Event'
        db.delete_table(u'cmplxsys_event')


    models = {
        u'cmplxsys.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'nextoffering': ('django.db.models.fields.DateTimeField', [], {}),
            'numtimesoffered': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'shortcode': ('django.db.models.fields.CharField', [], {'default': "'CSYS 500.'", 'max_length': '500'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'courses_taught'", 'blank': 'True', 'to': u"orm['cmplxsys.Person']"}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses_taken'", 'symmetrical': 'False', 'to': u"orm['cmplxsys.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Learn all the things.'", 'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.uvm.edu/~bagrow'", 'max_length': '2000'})
        },
        u'cmplxsys.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'There are none.'"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'event_page': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'events/blank.png'", 'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'Burlington, Vermont'", 'max_length': '500'}),
            'organizer_email': ('django.db.models.fields.EmailField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'organizer_name': ('django.db.models.fields.CharField', [], {'default': "'Roboctopus'", 'max_length': '500'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Life Changing Event'", 'max_length': '500'})
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
            'Meta': {'ordering': "['order']", 'object_name': 'Order'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmplxsys.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'paper': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmplxsys.Paper']"})
        },
        u'cmplxsys.paper': {
            'DOI': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'HTMLabstract': ('django.db.models.fields.TextField', [], {'default': "'There are none.<br>'"}),
            'ISSN': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-sort_date']", 'object_name': 'Paper'},
            'PMID': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'abstract': ('django.db.models.fields.TextField', [], {'default': "'There are none.'"}),
            'altmetric_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'arxiv': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'arxivpw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'author_list_sorted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Person']", 'through': u"orm['cmplxsys.Order']", 'symmetrical': 'False'}),
            'bibref': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fromclass': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmplxsys.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'google_scholar_cluster_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'google_scholar_most_recent_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'google_scholar_raw_result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'google_scholar_result_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'googlescholarlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'papers/blank.png'", 'max_length': '100'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'default': "'Preprint'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'journalpagelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'onlineappendices': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'preprintlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sort_date': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'supplementarylink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'timescited': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titlelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1950'})
        },
        u'cmplxsys.person': {
            'Meta': {'object_name': 'Person'},
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
            'current_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'position_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'post_doc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'Meta': {'ordering': "['-date']", 'object_name': 'Press'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'press/blank.png'", 'max_length': '100'}),
            'imagelink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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