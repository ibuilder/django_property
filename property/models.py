from django.db import models
from django.utils.translation import ugettext_lazy as _


class Property(models.Model):
    address = models.CharField(_('address'), max_length=200)
    city = models.CharField(_('city'), max_length=200)
    state = models.CharField(_('state'), max_length=200)
    zipcode = models.CharField(_('zipcode'), max_length=200)
    county = models.CharField(_('county'), max_length=200)
    area = models.CharField(_('area'), max_length=200)
    zoning = models.CharField(_('zoning'), max_length=200)
    attributes = models.ForeignKey('property.Attributes', verbose_name=_('attributes'), on_delete=models.CASCADE)
    owner = models.ForeignKey('property.Owner', verbose_name=_('owner'), on_delete=models.CASCADE)
    purchase_price = models.DecimalField(_('purchase price'), max_digits=10, decimal_places=2)
    assessed_value = models.DecimalField(_('assessed value'), max_digits=10, decimal_places=2)
    purchase_date = models.DateField(_('purchase date'))
    expenses = models.ForeignKey('property.Expenses', verbose_name=_('expenses'), on_delete=models.CASCADE)
    renovation_costs = models.ForeignKey('property.Renovation_costs', verbose_name=_('renovation costs'), on_delete=models.CASCADE)
    mortgage = models.ForeignKey('property.Mortgage', verbose_name=_('mortgage'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('property')
        verbose_name_plural = _('properties')
    
    def __str__(self):
        return self.address


class Owner(models.Model):
    
    class Meta:
        verbose_name = _('owner')
        verbose_name_plural = _('owners')
    


class Company(models.Model):
    
    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')
    


class Mortgage(models.Model):
    mortgage_company = models.ForeignKey('property.Company', verbose_name=_('mortgage company'), on_delete=models.CASCADE)
    term = models.CharField(_('term'), max_length=200)
    interest_rate = models.CharField(_('interest rate'), max_length=200)
    payment = models.CharField(_('payment'), max_length=200)
    amortization = models.CharField(_('amortization'), max_length=200)
    
    class Meta:
        verbose_name = _('mortgage')
        verbose_name_plural = _('mortgages')
    
    def __str__(self):
        return self.term


class Expenses(models.Model):
    expense_name = models.CharField(_('expense name'), max_length=200)
    cost = models.DecimalField(_('cost'), max_digits=10, decimal_places=2)
    vendor = models.ForeignKey('property.Company', verbose_name=_('vendor'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('expenses')
        verbose_name_plural = _('expenses')
    
    def __str__(self):
        return self.expense_name


class Renovation_costs(models.Model):
    reno_description = models.TextField(_('reno description'))
    cost_type = models.CharField(_('cost type'), max_length=200)
    cost = models.DecimalField(_('cost'), max_digits=10, decimal_places=2)
    contractor = models.ForeignKey('property.Company', verbose_name=_('contractor'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('renovation_costs')
        verbose_name_plural = _('renovation_costs')
    
    def __str__(self):
        return self.reno_description


class Attributes(models.Model):
    Attribute_name = models.CharField(_('Attribute name'), max_length=200)
    
    class Meta:
        verbose_name = _('attributes')
        verbose_name_plural = _('attributes')
    
    def __str__(self):
        return self.Attribute_name
