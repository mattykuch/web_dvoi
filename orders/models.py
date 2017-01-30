from django.db import models

from datetime import date

class Order(models.Model):

	owner = models.ForeignKey('account.Profile')
	district = models.CharField(max_length=50, default="e.g. Abim")
	month = models.CharField(max_length=50, default="e.g. January")
	submitter = models.CharField(max_length=50, default="e.g. Elton John Mabirizi")
	title_submitter = models.CharField(max_length=50, default="e.g. DCCT")
	#dateof_submit = models.DateField()
	class Meta:
		verbose_name = 'OrderGeneralInfo'
		verbose_name_plural = 'OrderGeneralInfos'
	
	#MEASLES
	#sbmeasles = models.IntegerField(blank=False, null=False, default=0)
	#oqmeasles = models.IntegerField(blank=False, null=False, default=0)
	#aomeasles = models.IntegerField(blank=False, null=False, default=0)
	#commmeasles = models.CharField(max_length=500, default="Add comment here")

	#BCG
	#sbbcg = models.IntegerField(blank=False, null=False, default=0)
	#oqbcg = models.IntegerField(blank=False, null=False, default=0)
	#aobcg = models.IntegerField(blank=False, null=False, default=0)
	#commbcg = models.CharField(max_length=500, default="Add comment here")

	#HPV
	#sbhpv = models.IntegerField(blank=False, null=False, default=0)
	#oqhpv = models.IntegerField(blank=False, null=False, default=0)
	#aohpv = models.IntegerField(blank=False, null=False, default=0)
	#commhpv = models.CharField(max_length=500, default="Add comment here")

    #HepB
	#sbhepb = models.IntegerField(blank=False, null=False, default=0)
	#oqhepb = models.IntegerField(blank=False, null=False, default=0)
	#aohepb = models.IntegerField(blank=False, null=False, default=0)
	#commhepb = models.CharField(max_length=500, default="Add comment here")

    #TT
	#sbtt = models.IntegerField(blank=False, null=False, default=0)
	#oqtt = models.IntegerField(blank=False, null=False, default=0)
	#aott = models.IntegerField(blank=False, null=False, default=0)
	#commtt = models.CharField(max_length=500, default="Add comment here")

    #OPV
	#sbopv = models.IntegerField(blank=False, null=False, default=0)
	#oqopv = models.IntegerField(blank=False, null=False, default=0)
	#aoopv = models.IntegerField(blank=False, null=False, default=0)
	#commopv = models.CharField(max_length=500, default="Add comment here")

    #YF
	#sbyf = models.IntegerField(blank=False, null=False, default=0)
	#oqyf = models.IntegerField(blank=False, null=False, default=0)
	#aoyf = models.IntegerField(blank=False, null=False, default=0)
	#commyf = models.CharField(max_length=500, default="Add comment here")

    #PCV
	#sbpcv = models.IntegerField(blank=False, null=False, default=0)
	#oqpcv = models.IntegerField(blank=False, null=False, default=0)
	#aopcv = models.IntegerField(blank=False, null=False, default=0)
	#commpcv = models.CharField(max_length=500, default="Add comment here")


