#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

def post(self, request, id=None):
            # rating = Rating.objects.get(user=request.data)                       
            # if rating.exists():
                serializer = self.serializer_class(data=request.data)
                print("HTSG", serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors)
            # else:
            #     rating.update(user=False)
            #     return Response(({'detail' : "you have given a rating before"}), status=status.HTTP_400_BAD_REQUEST)
            #         # raise PermissionDenied({'you have given a rating before'})


def post(self, request):
            rating = Rating.objects.filter(user=Token)
            if rating.exists():
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors)
            else:
                rating.update(user=False)
                return Response(({'message' : 'you give the rating before'}), status=status.HTTP_400_BAD_REQUEST)