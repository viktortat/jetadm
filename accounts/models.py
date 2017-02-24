from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import to_locale, get_language, ugettext_lazy as _



class UserType(models.Model):
    name = models.CharField(_('Name'),
        max_length=250,
        default="")
    class Meta:
        verbose_name = _('User type')
        verbose_name_plural = _('User types')



class User(AbstractUser):
    
    type = models.ForeignKey(UserType,
        null=True,
        on_delete=models.CASCADE,
        related_name='user_types',
        blank=True,
        verbose_name=_('User type'))

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')




