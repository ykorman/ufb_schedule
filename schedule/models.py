# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

class Trainee(models.Model):
  user = models.OneToOneField(auth_models.User, verbose_name=u'שם מתאמן')
  credit = models.PositiveSmallIntegerField(verbose_name=u'קרדיט')
  
  def __unicode__(self):
    return unicode(self.user)

  class Meta:
    app_label = u'לוח אימונים'
    verbose_name = u'מתאמן'
    verbose_name_plural = u'מתאמנים'
    db_table = 'schedule_trainee' 


class Workout(models.Model):
  when = models.DateTimeField(verbose_name=u'תאריך ושעת האימון')
  numOfTrainees = models.PositiveSmallIntegerField(verbose_name=u'מספר מתאמנים רשום', default=12)
  lenghInMinutes = models.PositiveSmallIntegerField(verbose_name=u'אורך האימון בדקות', default=60)
  
  def __unicode__(self):
    return unicode(self.when)

  class Meta:
    app_label = u'לוח אימונים'
    verbose_name = u'אימון'
    verbose_name_plural = u'אימונים'
    db_table = 'schedule_workout' 

class Registration(models.Model):
  trainee = models.ForeignKey(Trainee)
  workout = models.ForeignKey(Workout)
  
  def __unicode__(self):
    return unicode(str(self.trainee.user) + ' on ' + str(self.workout.when))
  
  class Meta:
    app_label = u'לוח אימונים'
    verbose_name = u'רישום'
    verbose_name_plural = u'רישומים'
    db_table = 'schedule_registration' 
