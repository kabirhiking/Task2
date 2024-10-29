from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from django.http import JsonResponse

# View all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# View event details and registration option
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# Register for an event
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Check if user already registered
    if Registration.objects.filter(event=event, user=request.user).exists():
        return JsonResponse({'message': 'Already registered'}, status=400)

    # Register the user if seats are available
    if event.available_seats > event.registrations.count():
        Registration.objects.create(event=event, user=request.user)
        return JsonResponse({'message': 'Successfully registered'}, status=200)
    else:
        return JsonResponse({'message': 'No available seats'}, status=400)

# User's registrations
@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/my_registrations.html', {'registrations': registrations})
