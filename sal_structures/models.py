from django.db import models


class Sal_Structure(models.Model):
    sal_type = models.CharField(max_length=200)
    basic = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    rent = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    transport = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    meal = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    furniture = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    hazard = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    shift_call = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    medical = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    domestic = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    entertainment = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    exam = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    learned = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    teach = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    leave_grant = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    personnel_assistant = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    news_paper = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    vehicle = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    dta = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    responsibility = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    wardrope = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)

    def __str__(self):
        return self.sal_type, self.basic, self.rent, self.transport, self.meal, self.furniture, self.hazard, self.shift_call, self.medical, self.domestic, self.entertainment, self.exam, self.learned, self.teach, self.leave_grant, self.personnel_assistant, self.personnel_assistant, self.news_paper, self.vehicle, self.responsibility, self.wardrope
