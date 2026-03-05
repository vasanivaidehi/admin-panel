from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from adminapp.models import Student


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # SubAdmin Group
        subadmin_group, created = Group.objects.get_or_create(name='SubAdmin')

        # Student model content type
        content_type = ContentType.objects.get_for_model(Student)

        # SubAdmin Permissions (Add + View)
        sub_permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=['add_student', 'view_student','delete_student']
        )

        subadmin_group.permissions.set(sub_permissions)

        # SubAdmin User
        subadmin_user, user_created = User.objects.get_or_create(username='subadmin')

        if user_created:
            subadmin_user.set_password('1234')
            subadmin_user.is_staff = True
            subadmin_user.save()
            self.stdout.write(self.style.SUCCESS("SubAdmin Created"))
        else:
            self.stdout.write("SubAdmin already exists")

        subadmin_user.groups.add(subadmin_group)

        # MiniAdmin Group
        miniadmin_group, created = Group.objects.get_or_create(name='MiniAdmin')

        # Only View Permission
        mini_permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=['view_student']
        )

        miniadmin_group.permissions.set(mini_permissions)

        # MiniAdmin User
        miniadmin_user, user_created = User.objects.get_or_create(username='miniadmin')

        if user_created:
            miniadmin_user.set_password('1234')
            miniadmin_user.is_staff = True
            miniadmin_user.save()
            self.stdout.write(self.style.SUCCESS("MiniAdmin Created"))
        else:
            self.stdout.write("MiniAdmin already exists")

        miniadmin_user.groups.add(miniadmin_group)


        self.stdout.write(self.style.SUCCESS("All Roles Setup Completed Successfully"))