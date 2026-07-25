from notifications.models import Notification

def unread_notifications(request):
    if not request.user.is_authenticated:
        return {
            'unread_notifications': [],
            'unread_notifications_count': 0
        }
    
    unread = Notification.objects.filter(user=request.user, is_read=False)
    
    return {
        'unread_notifications': unread,
        'unread_notifications_count': unread.count()
    }
