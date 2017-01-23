from django.db import models

class Order(models.Model):
	owner = models.ForeignKey('account.Profile')
	district = models.CharField(max_length=50)
	month = models.CharField(max_length=50)
	submitter = models.CharField(max_length=50)
	title_submitter = models.CharField(max_length=50)
	#date_submit = models.DateTimeField(auto_now_add=True)
	#MEASLES
	#sbmeasles = models.IntegerField()
    #oqmeasles = models.IntegerField()
    #aomeasles = models.IntegerField()
    #commmeasles = models.CharField(max_length=500)

	#BCG
	#sbbcg = models.IntegerField()
    #oqbcg = models.IntegerField()
    #aobcg = models.IntegerField()
    #commbcg = models.CharField(max_length=500)

	#HPV
	#sbhpv = models.IntegerField()
    #oqhpv = models.IntegerField()
    #aohpv = models.IntegerField()
    #commhpv = models.CharField(max_length=500)

