from django.db import models


class Khuán(models.Model):
    miâ = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.miâ

    class Meta:
        verbose_name = "Khuán"
        verbose_name_plural = verbose_name


class Luī(models.Model):
    khuán = models.ForeignKey(
        Khuán,
        related_name='luī',
        on_delete=models.PROTECT,
    )
    miâ = models.CharField(max_length=30, unique=True)
    siktsuí = models.CharField(max_length=10)
    singāu = models.PositiveIntegerField()

    def __str__(self):
        return self.miâ

    class Meta:
        verbose_name = "Luī"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['khuán', 'miâ'],
                name='khuán-luī',
            ),
        ]


class Iūnn(models.Model):
    khuán = models.ForeignKey(
        Khuán,
        related_name='iūnn',
        on_delete=models.CASCADE,
    )
    css = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Iūnn"
        verbose_name_plural = verbose_name
