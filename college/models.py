from django.db import models
from core import db
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

class Accrediation(db.BaseModal):
    COUNTRY_TYPE_INDIA = "India"
    COUNTRY_TYPE_UNITED_KINDOM = "United Kindom"
    COUNTRY_TYPE_AUSTRALIA = "Australia"
    COUNTRY_TYPE_UNITED_STATES = "United States"
    COUNTRY_TYPE_CANADA = "Canada"
    COUNTRY_TYPE_FRANCE = "France"
    COUNTRY_TYPE_GERMANY = "Germany"

    COUNTRY_TYPES = (
        (COUNTRY_TYPE_INDIA, COUNTRY_TYPE_INDIA),
        (COUNTRY_TYPE_UNITED_KINDOM, COUNTRY_TYPE_UNITED_KINDOM),
        (COUNTRY_TYPE_AUSTRALIA, COUNTRY_TYPE_AUSTRALIA),
        (COUNTRY_TYPE_UNITED_STATES, COUNTRY_TYPE_UNITED_STATES),
        (COUNTRY_TYPE_CANADA, COUNTRY_TYPE_CANADA),
        (COUNTRY_TYPE_FRANCE, COUNTRY_TYPE_FRANCE),
        (COUNTRY_TYPE_GERMANY, COUNTRY_TYPE_GERMANY)
    )
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250, choices=COUNTRY_TYPES, default=COUNTRY_TYPE_INDIA)

    def __str__(self):
        return self.name


class Facility(db.BaseModal):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class College(db.BaseModal):
    GENDER_ACCEPTED_CO_ED = "Co-Ed"
    GENDER_ACCEPTED_FEMALE = "Female"
    GENDER_ACCEPTED_MALE = "Male"
    GENDER_ACCEPTED_TYPES = (
        (GENDER_ACCEPTED_CO_ED, GENDER_ACCEPTED_CO_ED),
        (GENDER_ACCEPTED_MALE, GENDER_ACCEPTED_MALE),
        (GENDER_ACCEPTED_FEMALE, GENDER_ACCEPTED_FEMALE),
    )

    COLLEGE_TYPE_UNIVERSITY = "University"
    COLLEGE_TYPE_COLLEGE = "College"
    COLLEGE_TYPES = (
        (COLLEGE_TYPE_COLLEGE, COLLEGE_TYPE_COLLEGE),
        (COLLEGE_TYPE_UNIVERSITY, COLLEGE_TYPE_UNIVERSITY),
    )

    def img_path(instance, filename):
        extension = 'png'
        timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S') 
        return f'college/{instance.id}/IMG_{instance.name}_{timestamp}.{extension}'

    name = models.CharField(max_length=250)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to=img_path, null=True)
    gender_accepted = models.CharField(max_length=250, choices=GENDER_ACCEPTED_TYPES, default=GENDER_ACCEPTED_CO_ED)
    college_type = models.CharField(max_length=250, choices=COLLEGE_TYPES, default=COLLEGE_TYPE_COLLEGE)
    affiliated = models.CharField(max_length=250)
    accrediation = models.ForeignKey(Accrediation, on_delete=models.CASCADE)
    accrediation_grade = models.CharField(max_length=50)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.IntegerField(validators=[MaxValueValidator(50)], null=True, blank=True)
    contact1 = models.IntegerField(validators=[MaxValueValidator(50)], null=True, blank=True)
    facility = models.ManyToManyField(Facility)

    def __str__(self):
        return self.name


RANK_TYPE_OVERALL = "Overall"
RANK_TYPE_ENGINEERING = "Engineering"
RANK_TYPE_PHARMACY = "Pharmacy"
RANK_TYPE_MANAGEMENT = "Management"

RANK_TYPES = (
    (RANK_TYPE_OVERALL, RANK_TYPE_OVERALL),
    (RANK_TYPE_ENGINEERING, RANK_TYPE_ENGINEERING),
    (RANK_TYPE_PHARMACY, RANK_TYPE_PHARMACY),
    (RANK_TYPE_MANAGEMENT, RANK_TYPE_MANAGEMENT),
)


class Degree(models.Model):
    DEGREE_TYPE_ENGINEERING = "Engineering"
    DEGREE_TYPE_ARTS = "Arts"
    DEGREE_TYPE_NURSING = "Nursing"
    DEGREE_TYPE_LAW = "Law"

    DEGREE_TYPES = (
        (DEGREE_TYPE_ENGINEERING, DEGREE_TYPE_ENGINEERING),
        (DEGREE_TYPE_ARTS, DEGREE_TYPE_ARTS),
        (DEGREE_TYPE_NURSING, DEGREE_TYPE_NURSING),
        (DEGREE_TYPE_LAW, DEGREE_TYPE_LAW),
    )

    DEGREE_ROLE_BACHELOR = "Bachelor"
    DEGREE_ROLE_MASTER = "Master"
    DEGREE_ROLE_DOCTRATE = "Doctrate"

    DEGREE_ROLES = (
        (DEGREE_ROLE_BACHELOR, DEGREE_ROLE_BACHELOR),
        (DEGREE_ROLE_MASTER, DEGREE_ROLE_MASTER),
        (DEGREE_ROLE_DOCTRATE, DEGREE_ROLE_DOCTRATE),
    )

    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    degree_type = models.CharField(max_length=250, choices=DEGREE_TYPES)
    degree_role = models.CharField(max_length=250, choices=DEGREE_ROLES) 

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    course = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class NIRF(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class Outlook(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class ARIIA(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class IndiaToday(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class BusinessToday(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class TimesofIndia(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class EconomicTimes(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class IndianExpress(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)


class IndiaEducation(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class USNews(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class MBAUniverse(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class QS(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class IIRF(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)

class CollegeWorld(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    year = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=250, choices=RANK_TYPES, default=RANK_TYPE_OVERALL)
