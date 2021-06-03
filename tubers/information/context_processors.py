from .models import Info

# We write context processor coz it will be accessible in all template and it returns a dictionary


def info(request):
    info = Info.objects.all()
    return {
        "info": info
    }
