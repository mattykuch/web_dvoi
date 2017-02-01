from django.db import models

from datetime import date


class Vaccine(models.Model):
	name = models.CharField(max_length=50)


class District(models.Model):
	name = models.CharField(max_length=50)



class Order(models.Model):
	owner = models.ForeignKey('account.Profile')
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
	month = models.CharField(max_length=50, default="e.g. January")
	submitter = models.CharField(max_length=50, default="e.g. Elton John Mabirizi")
	title_submitter = models.CharField(max_length=50, default="e.g. DCCT")

	#dateof_submit = models.DateField()
	class Meta:
		verbose_name = 'OrderGeneralInfo'
		verbose_name_plural = 'OrderGeneralInfos'


class OrderLine(models.Model):
	order = models.ForeignKey(Order)
	vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True)
	stock_balance = models.IntegerField(default=0)
	comment = models.CharField(max_length=250) 

	class Meta(object):
		unique_together = ("order", "vaccine")	

	
# class OrderMeasles(models.Model):
# 	#MEASLES
# 	sbmeasles = models.IntegerField(blank=False, null=False, default=0)
# 	oqmeasles = models.IntegerField(blank=False, null=False, default=0)
# 	aomeasles = models.IntegerField(blank=False, null=False, default=0)
# 	commmeasles = models.CharField(max_length=500, default="Add comment here")

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

	#PENTA
	#sbpenta = models.IntegerField(blank=False, null=False, default=0)
	#oqpenta = models.IntegerField(blank=False, null=False, default=0)
	#aopenta = models.IntegerField(blank=False, null=False, default=0)
	#commpenta = models.CharField(max_length=500, default="Add comment here")

	#IPV
	#sbipv = models.IntegerField(blank=False, null=False, default=0)
	#oqipv = models.IntegerField(blank=False, null=False, default=0)
	#aoipv = models.IntegerField(blank=False, null=False, default=0)
	#commipv = models.CharField(max_length=500, default="Add comment here")

    #ROTA
	#sbrota = models.IntegerField(blank=False, null=False, default=0)
	#oqrota = models.IntegerField(blank=False, null=False, default=0)
	#aorota = models.IntegerField(blank=False, null=False, default=0)
	#commrota = models.CharField(max_length=500, default="Add comment here")

    #Syringes 0.05ml
	#sbs005 = models.IntegerField(blank=False, null=False, default=0)
	#oqs005 = models.IntegerField(blank=False, null=False, default=0)
	#aos005 = models.IntegerField(blank=False, null=False, default=0)
	#comms005 = models.CharField(max_length=500, default="Add comment here")

    #Syringes 0.5ml
	#sbs05 = models.IntegerField(blank=False, null=False, default=0)
	#oqs05 = models.IntegerField(blank=False, null=False, default=0)
	#aos05 = models.IntegerField(blank=False, null=False, default=0)
	#comms05 = models.CharField(max_length=500, default="Add comment here")

    #Syringes 5ml
	#sbs5 = models.IntegerField(blank=False, null=False, default=0)
	#oqs5 = models.IntegerField(blank=False, null=False, default=0)
	#aos5 = models.IntegerField(blank=False, null=False, default=0)
	#comms5 = models.CharField(max_length=500, default="Add comment here")

    #Syringes 2ml
	#sbs2 = models.IntegerField(blank=False, null=False, default=0)
	#oqs2 = models.IntegerField(blank=False, null=False, default=0)
	#aos2 = models.IntegerField(blank=False, null=False, default=0)
	#comms2 = models.CharField(max_length=500, default="Add comment here")

    #Safety Boxes
	#sbsb = models.IntegerField(blank=False, null=False, default=0)
	#oqsb = models.IntegerField(blank=False, null=False, default=0)
	#aosb = models.IntegerField(blank=False, null=False, default=0)
	#commsb = models.CharField(max_length=500, default="Add comment here")

    #Tetanus Toxoid (TT) Cards
	#sbttc = models.IntegerField(blank=False, null=False, default=0)
	#oqttc = models.IntegerField(blank=False, null=False, default=0)
	#aottc = models.IntegerField(blank=False, null=False, default=0)
	#commttc = models.CharField(max_length=500, default="Add comment here")

    #Child Health Cards (CHC)
	#sbchc = models.IntegerField(blank=False, null=False, default=0)
	#oqchc = models.IntegerField(blank=False, null=False, default=0)
	#aochc = models.IntegerField(blank=False, null=False, default=0)
	#commchc = models.CharField(max_length=500, default="Add comment here")

    #Vaccine Control Book (VCB)
	#sbvcb = models.IntegerField(blank=False, null=False, default=0)
	#oqvcb = models.IntegerField(blank=False, null=False, default=0)
	#aovcb = models.IntegerField(blank=False, null=False, default=0)
	#commvcb = models.CharField(max_length=500, default="Add comment here")


