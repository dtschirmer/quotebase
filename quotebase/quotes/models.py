# QUOTES MODEL

from django.db import models

class Quote(models.Model):

    LEAD_TYPE_CHOICES = (
        ('company', 'Relo Company'),
        ('retail', 'Email/Call-In'),
        ('web', 'Web Lead'),
        ('hr', 'HR Contact'),
    )
    LEAD_CONTACT_CHOICES = (
        ('coordinator', 'Coordinator'),
        ('customer', 'Customer'),
        ('other', 'Other'),
    )

    date            = models.DateField()
    assigned        = models.CharField(max_length=30)
    lead_type       = models.CharField(max_length=30, choices=LEAD_TYPE_CHOICES)
    lead_contact    = models.CharField(max_length=30, choices=LEAD_CONTACT_CHOICES)
    coordinator     = models.CharField(max_length=30, blank=True)
    coord_email     = models.EmailField(blank=True)
    coord_phone     = models.CharField(max_length=30, blank=True)
    relo_company    = models.ForeignKey('contacts.Relo_Company', db_index=False, blank=True, null=True)
    customer        = models.CharField(max_length=30, blank=True)
    cust_email      = models.EmailField(max_length=30, blank=True)
    cust_phone      = models.CharField(max_length=30, blank=True)
    cust_company    = models.CharField(max_length=30, blank=True)
    other_contact   = models.CharField(max_length=30, blank=True)
    other_email     = models.EmailField(max_length=30, blank=True)
    other_phone     = models.CharField(max_length=30, blank=True)
    other_company   = models.CharField(max_length=30, blank=True)
    o_city          = models.CharField(max_length=50, blank=True)
    o_st_pr         = models.CharField(max_length=2, blank=True)
    o_country       = models.CharField(max_length=50)
    d_city          = models.CharField(max_length=50, blank=True)
    d_st_pr         = models.CharField(max_length=2, blank=True)
    d_country       = models.CharField(max_length=50)
    pets            = models.CharField(max_length=50)
    pet_notes       = models.TextField(max_length=100, blank=True)
    total_costs     = models.IntegerField(max_length=10, blank=True, null=True)
    contingency     = models.IntegerField(max_length=10, blank=True, null=True)
    incentive       = models.IntegerField(max_length=10, blank=True, null=True)
    referral_fee    = models.IntegerField(max_length=10, blank=True, null=True)
    cc_fee          = models.IntegerField(max_length=10, blank=True, null=True)
    markup          = models.IntegerField(max_length=10, blank=True, null=True)
    total_quote     = models.IntegerField(max_length=10, blank=True, null=True)
    prc_approved    = models.BooleanField(blank=True)
    prc_appvd_date  = models.DateField(blank=True, null=True)
    sent_date       = models.DateField(blank=True, null=True)
    convert_date    = models.DateField(blank=True, null=True)
    prc             = models.CharField(max_length=30, blank=True)
    notes           = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s, %s, %s, %s %s to %s %s, %s' % (self.date, self.assigned, self.lead_contact, self.o_city, self.o_country, self.d_city, self.d_country, self.pets)
    
class Cost(models.Model):

    SERVICE_POINT_CHOICES = (
        ( 1 , 'Origin Cost (1)'),
        ( 3 , 'Middle/Transit (3)'),
        ( 5 , 'Destination Cost (5)'),
        ( 2 , 'Other (2)'),
        ( 4 , 'Other (4)'),
        ( 6 , 'Other (6)'),
    )

    date            = models.DateField()
    agent           = models.ForeignKey('contacts.Agent')
    estimated       = models.BooleanField()
    currency        = models.ForeignKey('reference.Currency')
    exchange_rate   = models.DecimalField(decimal_places=3, max_digits=6, blank=True)
    quotes          = models.ManyToManyField(Quote)
    service_point   = models.IntegerField(max_length=1, choices=SERVICE_POINT_CHOICES)
    airline         = models.ForeignKey('reference.Airline', db_index=False)
    o_airport       = models.CharField(max_length=3)
    d_airport       = models.CharField(max_length=3)
    af_cost         = models.IntegerField(max_length=10, blank=True, null=True)
    af_cost_lcl     = models.IntegerField(max_length=10, blank=True, null=True)
    af_fee          = models.IntegerField(max_length=10, blank=True, null=True)
    af_fee_lcl      = models.IntegerField(max_length=10, blank=True, null=True)    
    ap_fee_customs  = models.IntegerField(max_length=10, blank=True, null=True)
    ap_fee_lcl      = models.IntegerField(max_length=10, blank=True, null=True)
    ap_cust_notes   = models.CharField(max_length=50, blank=True)
    transportation  = models.IntegerField(max_length=10, blank=True, null=True)
    trans_lcl       = models.IntegerField(max_length=10, blank=True, null=True)     
    trans_notes     = models.CharField(max_length=50, blank=True)
    travel_kennel   = models.IntegerField(max_length=10, blank=True, null=True)
    tk_lcl          = models.IntegerField(max_length=10, blank=True, null=True)    
    tk_notes        = models.CharField(max_length=50, blank=True)
    vaccination     = models.IntegerField(max_length=10, blank=True, null=True)
    vcn_lcl         = models.IntegerField(max_length=10, blank=True, null=True)
    vcn_notes       = models.CharField(max_length=50, blank=True)
    parasite        = models.IntegerField(max_length=10, blank=True, null=True)
    para_lcl        = models.IntegerField(max_length=10, blank=True, null=True)
    para_notes      = models.CharField(max_length=50, blank=True)
    health_cert     = models.IntegerField(max_length=10, blank=True, null=True)
    hc_lcl          = models.IntegerField(max_length=10, blank=True, null=True)
    hc_notes        = models.CharField(max_length=50, blank=True)
    hc_2            = models.IntegerField(max_length=10, blank=True, null=True)
    hc_2_lcl        = models.IntegerField(max_length=10, blank=True, null=True)
    hc_2_notes      = models.CharField(max_length=50, blank=True)
    gov_endorse     = models.IntegerField(max_length=10, blank=True, null=True)
    gov_end_lcl     = models.IntegerField(max_length=10, blank=True, null=True)
    gov_end_notes   = models.CharField(max_length=50, blank=True)
    postage         = models.IntegerField(max_length=10, blank=True, null=True)
    post_lcl        = models.IntegerField(max_length=10, blank=True, null=True)
    post_notes      = models.CharField(max_length=50, blank=True)
    gov_permit      = models.IntegerField(max_length=10, blank=True, null=True)
    gov_perm_lcl    = models.IntegerField(max_length=10, blank=True, null=True) 
    gov_perm_notes  = models.CharField(max_length=50, blank=True)
    quarantine      = models.IntegerField(max_length=10, blank=True, null=True)
    q_lcl           = models.IntegerField(max_length=10, blank=True, null=True)
    q_notes         = models.CharField(max_length=50, blank=True)
    boarding        = models.IntegerField(max_length=10, blank=True, null=True)
    board_lcl       = models.IntegerField(max_length=10, blank=True, null=True)
    board_notes     = models.CharField(max_length=50, blank=True)
    other_name      = models.CharField(max_length=50, blank=True)
    other_cost      = models.IntegerField(max_length=10, blank=True, null=True)
    other_lcl       = models.IntegerField(max_length=10, blank=True, null=True)
    other_notes     = models.CharField(max_length=50, blank=True)
    total_cost      = models.IntegerField(max_length=12, blank=True, null=True)
    total_lcl       = models.IntegerField(max_length=10, blank=True, null=True)
    notes           = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.service_point, self.date, self.agent, self.total_cost)

#Not being used for actual choices any more. 
#This is a reference for values to add to the Airline table
AIRLINE_CHOICES = (
    ('aat', 'Austrian Air'),
    ('ac', 'Air Canada'),
    ('af', 'Air France'),
    ('am', 'Aero Mexico'),
    ('ar', 'Aerolineas Argentinas'),
    ('as', 'Alaska Airlines'),
    ('av', 'Avianca'),
    ('az', 'Alitalia'),
    ('b6', 'JetBlue Airways'),
    ('bw', 'Caribbean Airlines'),
    ('cm', 'COPA'),
    ('cx', 'Cathay Pacific'),
    ('cz', 'China Southern Airlines'),
    ('dl', 'Delta Air Lines'),
    ('ei', 'Aer Lingus'),
    ('ek', 'Emirates'),
    ('f9', 'Frontier Airlines'),
    ('ib', 'Iberia'),
    ('jj', 'TAM Linhas Aereas'),
    ('ke', 'Korean Air Lines'),
    ('kl', 'KLM'),
    ('kq', 'Kenya Airways'),
    ('la', 'LAN Airlines'),
    ('lh', 'Lufthansa'),
    ('lo', 'LOT Polish Airlines'),
    ('lx', 'SWISS'),
    ('nh', 'All Nippon Airways'),
    ('o6', 'Avianca Brazil'),
    ('pz', 'TAM'),
    ('sk', 'SAS Scandinavian Airlines'),
    ('sq', 'Singapore Airlines'),
    ('ua', 'United Airlines'),
    ('vs', 'Virgin Atlantic'),
    ('vx', 'Virgin America'),
    ('ws', 'WestJet'), 
)

CURRENCY_CHOICES = (
    ('USD', 'US Dollars'),
    ('GBP', 'British pound'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese yen'),
    ('SGD', 'Singapore dollar'),
    ('HKD', 'Hong Kong dollar'),
    ('AUD', 'Australian dollar'),
    ('CHF', 'Swiss Franc'),
    ('CAD', 'Canadian dollar'),
    ('SEK', 'Swedish krona'),
    ('CZK', 'Czech koruna'),
    ('NOK', 'Norwegian krone'),
    ('INR', 'Indian rupee'),
    ('NZD', 'New Zealand dollar'),
    ('DKK', 'Danish kroner'),
    ('AED', 'Emirati dirham'),
    ('EGP', 'Egyptian pound'),
    ('ZAR', 'South African rand'),
    ('THB', 'Thai baht'),
    ('PKR', 'Pakistani rupee'),
)
