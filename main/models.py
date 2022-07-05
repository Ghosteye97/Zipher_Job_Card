from django.db import models

class jobCardsClass(models.Model):
    customerName = models.CharField("Customer Name",max_length=50 , blank=False)

    addressStreetNo = models.CharField(max_length=50 , blank=False)
    addressStreet = models.CharField(max_length=50 , blank=False)
    addressSuburb = models.CharField(max_length=50, blank=True )
    addressCity = models.CharField(max_length=50, blank=True )

    contact = models.CharField(max_length=50, blank=False )
    mail = models.CharField(max_length=50, blank=True )
    CellNo = models.CharField(max_length=50, blank=True )

    jobNumber = models.CharField(max_length=50, blank=True )
    dateRecieved = models.DateTimeField(auto_now=False, auto_now_add=False)
    dateToBeCompleted = models.DateTimeField(auto_now=False, auto_now_add=False)
    instructionBy = models.CharField(max_length=50, blank=True )
    jobDoneBy = models.CharField(max_length=50, blank=True )
    timeStarted = models.TimeField(auto_now=False, auto_now_add=False)
    timeCompleted = models.TimeField(auto_now=False, auto_now_add=False)

    Instructions = models.TextField(max_length=255)

    matDescription1 =models.CharField(max_length=50, blank=True )
    matDescription2 = models.CharField(max_length=50, blank=True)
    matDescription3 = models.CharField(max_length=50, blank=True)
    matDescription4 = models.CharField(max_length=50, blank=True)
    matDescription5 = models.CharField(max_length=50, blank=True)
    matDescription6 = models.CharField(max_length=50, blank=True)

    matQuantity1 =models.CharField(max_length=50, blank=True )
    matQuantity2 = models.CharField(max_length=50, blank=True)
    matQuantity3 = models.CharField(max_length=50, blank=True)
    matQuantity4 = models.CharField(max_length=50, blank=True)
    matQuantity5 = models.CharField(max_length=50, blank=True)
    matQuantity6 = models.CharField(max_length=50, blank=True)

    matUnitPrice1 =models.CharField(max_length=50, blank=True )
    matUnitPrice2 = models.CharField(max_length=50, blank=True)
    matUnitPrice3 = models.CharField(max_length=50, blank=True)
    matUnitPrice4 = models.CharField(max_length=50, blank=True)
    matUnitPrice5 = models.CharField(max_length=50, blank=True)
    matUnitPrice6 = models.CharField(max_length=50, blank=True)

    matTotal1 =models.CharField(max_length=50, blank=True )
    matTotal2 =models.CharField(max_length=50, blank=True )
    matTotal3 = models.CharField(max_length=50, blank=True)
    matTotal4 = models.CharField(max_length=50, blank=True)
    matTotal5 = models.CharField(max_length=50, blank=True)
    matTotal6 = models.CharField(max_length=50, blank=True)

    labDescription1 =models.CharField(max_length=50, blank=True )
    labDescription2 =models.CharField(max_length=50, blank=True )
    labDescription3 =models.CharField(max_length=50, blank=True )
    labDescription4 =models.CharField(max_length=50, blank=True )
    labDescription5 =models.CharField(max_length=50, blank=True )
    labDescription6 =models.CharField(max_length=50, blank=True )

    labQuantity1 =models.CharField(max_length=50, blank=True )
    labQuantity2 =models.CharField(max_length=50, blank=True )
    labQuantity3 =models.CharField(max_length=50, blank=True )
    labQuantity4 =models.CharField(max_length=50, blank=True )
    labQuantity5 =models.CharField(max_length=50, blank=True )
    labQuantity6 =models.CharField(max_length=50, blank=True )

    labUnitPrice1 =models.CharField(max_length=50, blank=True )
    labUnitPrice2 =models.CharField(max_length=50, blank=True )
    labUnitPrice3 =models.CharField(max_length=50, blank=True )
    labUnitPrice4 =models.CharField(max_length=50, blank=True )
    labUnitPrice5 =models.CharField(max_length=50, blank=True )
    labUnitPrice6 =models.CharField(max_length=50, blank=True )

    labTotal1 =models.CharField(max_length=50, blank=True )
    labTotal2 =models.CharField(max_length=50, blank=True )
    labTotal3 =models.CharField(max_length=50, blank=True )
    labTotal4 =models.CharField(max_length=50, blank=True )
    labTotal5 =models.CharField(max_length=50, blank=True )
    labTotal6 =models.CharField(max_length=50, blank=True )

    matTotalExVat = models.CharField(max_length=50, blank=True)
    matVat = models.CharField(max_length=50, blank=True)
    matTotalDue = models.CharField(max_length=50, blank=True)

    labTotalExVat = models.CharField(max_length=50, blank=True )
    labVat = models.CharField(max_length=50, blank=True )
    labTotalDue = models.CharField(max_length=50, blank=True )

    totalCostOfJob = models.CharField(max_length=50, blank=True)
