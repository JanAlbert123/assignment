from django.shortcuts import render, get_object_or_404

# Dummy data for demonstration
ANNOUNCEMENTS = [
    {'id': 1, 'title': 'Announcement 1', 'content': 'This is the first announcement. <span class="more" style="display:none;">More details about announcement 1.</span>'},
    {'id': 2, 'title': 'Announcement 2', 'content': 'This is the second announcement. <span class="more" style="display:none;">More details about announcement 2.</span>'},
]

def home(request):
    return render(request, 'home.html', {'title': 'home'})

def announcement_list(request):
    return render(request, 'announcement_list.html', {'announcements': ANNOUNCEMENTS})

def announcement_detail(request, id):
    # Remove the get_object_or_404 line!
    announcement = next((a for a in ANNOUNCEMENTS if a['id'] == id), None)
    if not announcement:
        from django.http import Http404
        raise Http404("Announcement not found")
    return render(request, 'announcement_detail.html', {'announcement': announcement})

def announcement1(request):
    return render(request, 'announcement1.html', {'title': 'Announcement1'})

def announcement2(request):
    return render(request, 'announcement2.html', {'title': 'Announcement2'})