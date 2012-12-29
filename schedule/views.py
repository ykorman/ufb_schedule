# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from schedule.models import Registration, Workout, Trainee

@login_required(login_url='login')
def trainee_schedule(request):
  my_regs = Registration.objects.filter(trainee__user__username__exact=request.user.username)
  trainee = Trainee.objects.get(user__exact=request.user)
  t = loader.get_template('my_schedule.html')
  c = Context({'my_regs': my_regs, 'username': request.user.username, 'credit': trainee.credit, })
#  return HttpResponse('hello Mr. ' + request.user.username + '\n' + str(reg))
  return HttpResponse(t.render(c))

@login_required(login_url='login')
def workout_select(request):
  available_workouts = Workout.objects.filter(when__gt=datetime.datetime.now())
  trainee = Trainee.objects.get(user__exact=request.user)
  return render_to_response('workout_select.html', { 'available_workouts': available_workouts, 'username': request.user.username, 'credit': trainee.credit, }, context_instance=RequestContext(request))

@login_required(login_url='login')
def workout_register(request):
  try:
    selected_workout = Workout.objects.get(pk=request.POST['workout'])
  except (KeyError, Workout.DoesNotExist):
      return render_to_response('workout_select.html', {
        'error_message': "You didn't select a workout.",
        }, context_instance=RequestContext(request))
  else:
    trainee = Trainee.objects.get(user=request.user)
    reg = Registration(trainee=trainee, workout=selected_workout)
    reg.save()
    return HttpResponseRedirect('my_schedule')
