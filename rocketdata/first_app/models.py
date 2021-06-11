from django.db import models


class Employee(models.Model):
    fio = models.CharField(
        max_length=150,
        verbose_name='ФИО'
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )
    date_of_employment = models.DateField(verbose_name='Дата приема на работу')
    salary_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Размер заработной платы'
    )
    salary_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Выплаченная зарплата'
    )
    chief = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
        verbose_name='Начальник'
    )
    LEVEL_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    level = models.CharField(
        max_length=1,
        choices=LEVEL_CHOICES,
        default='5',
        verbose_name='Уровень иерархии'
    )

    class Meta:
        ordering = ['fio']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.position + ', ' + self.fio