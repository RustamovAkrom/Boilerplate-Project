from django.utils.translation import gettext_lazy as _
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import TimeStampedModel
from apps.telemarketing.choices import (
    CallStatus,
    CallScriptModuleChoice,
    ProductTypeChoice,
    CustomerLevel,
)


class Credit(TimeStampedModel):
    name = models.TextField()
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="text")

    class Meta:
        verbose_name = _("Credit")
        verbose_name_plural = _("Credits")
    
    def __str__(self) -> str:
        return self.name
    

class Type(TimeStampedModel):
    name = models.CharField(max_length=40)

    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="types")

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self) -> str:
        return self.name


class CustomerStatus(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="customer_status")
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = _("CustomerStatus")
        verbose_name_plural = _("CusomerStatuses")

    def __str__(self) -> str:
        return self.name
    

class CustomerCategory(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="customer_categories")
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = _("CustomerCategory")
        verbose_name_plural = _("CustomerCategories")
    
    def __str__(self) -> str:
        return self.name
    

class Customer(TimeStampedModel):
    class GenderChoice(models.TextChoices):
        MALE = "male", _("Male")
        FAMALE = "famale", _("Famale")

    full_name = models.CharField(max_length=56, null=True)
    passport = models.CharField(max_length=9, unique=True, null=True, blank=True)
    phone = PhoneNumberField(region="UZ")
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GenderChoice.choices, null=True)
    client_id = models.ForeignKey("telemarketing.CustomerStatus", models.PROTECT, related_name="customers", null=True)
    category = models.ForeignKey(
        "telemarketing.CustomerCategory", models.PROTECT, related_name="customers", null=True, blank=True
    )
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="customers")
    channel = models.ForeignKey("telemarketing.Channel", models.PROTECT, related_name="customers", null=True)
    pnfl = models.CharField(max_length=14, null=True, blank=True)
    level = models.CharField(
        max_length=6, choices=CustomerLevel.choices, default=CustomerLevel.LOW
    )

    class Meta:
        ordering = [
            "-created_at"
        ]
    
    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"


class AppealStatus(TimeStampedModel):
    name = models.CharField(max_length=32)
    is_closed = models.BooleanField(default=False)
    color = models.CharField(max_length=16, default="FFFFFF")
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="appeal_status")

    class Meta:
        verbose_name = _("AppealStatus")
        verbose_nam_plural = _("AppealStatuses")
    
    def __str__(self) -> str:
        return self.name


class Comment(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="comments")
    appeal = models.ForeignKey("telemarketing.Appeal", models.PROTECT, related_name="comments")
    text = models.TextField()
    type = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.text


class Appeal(TimeStampedModel):
    customer = models.ForeignKey("telemarketing.Customer", models.PROTECT, related_name="appeals")
    type = models.ForeignKey("telemarketing.Type", models.PROTECT, related_name="appeals", null=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    branch = models.ForeignKey("telemarketing.Branch", models.SET_NULL, related_name="appeals", null=True)
    status = models.ForeignKey("telemarketing.AppealStatus", models.PROTECT, related_name="appeals")
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="appeals")
    products = models.ManyToManyField("telemarketing.Product", related_name="related_appeals")
    options = models.ManyToManyField("telemarketing.Option", related_name="appeals", blank=True)
    call_status = models.CharField(max_length=23, choices=CallStatus.choices, blank=True)

    class Meta:
        ordering = [
            "-updated_at"
        ]
    
    def __str__(self) -> str:
        return f"{self.title}-{self.agent}"
    
    @property
    def rating_value(self):
        return self.reviews.last().rating
    

class Chouse(TimeStampedModel):
    appeal = models.ForeignKey(
        "telemarketing.Appeal", models.PROTECT, null=True, blank=True
    )
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="chouses", null=True, blank=True)
    fullname = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    request_time = models.DateTimeField(blank=True, null=True)
    fraud_type = models.CharField(max_length=128, null=True, blank=True)
    stealing_info = models.TextField(null=True, blank=True)
    fraudser_info = models.TextField(null=True, blank=True)
    payment_service = models.TextField(null=True, blank=True)
    owner_name = models.TextField(null=True, blank=True)
    stolen_amount = models.FloatField(null=True, blank=True)
    customer_card = models.TextField(null=True, blank=True)
    rogue_address = models.TextField(null=True, blank=True)
    scrammed_device_info = models.TextField(null=True, blank=True)
    fraudcer_payment_info = models.TextField(null=True, blank=True)
    scam_info = models.TextField(null=True, blank=True)
    phishing_site = models.URLField(null=True, blank=True)
    otp_code = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = [
            "-updated_at",
        ]

    def __str__(self):
        return self.fullname


class Product(TimeStampedModel):
    parent = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    info = models.TextField()
    type = models.ManyToManyField("telemarketing.Type", "products")
    status = models.CharField(max_length=11, choices=ProductTypeChoice.choices)
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="products")
    product_id = models.IntegerField(null=True, blank=True)
    product_url = models.CharField(max_length=256, null=True, blank=True)
    iabsproduct_id = models.IntegerField(default=-1)
    options = models.ManyToManyField("telemarketing.Option", "products")
    order_id = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class Channel(TimeStampedModel):
    name = models.CharField(max_length=40)
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="channels")

    def __str__(self) -> str:
        return self.name
    

class ScriptCategory(TimeStampedModel):
    name = models.CharField(max_length=128)
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="script_categories")

    @property
    def script_count(self):
        return self.scripts.count()

    def __str__(self) -> str:
        return self.script_count
    

class Script(TimeStampedModel):
    title = models.CharField(max_length=512)
    category = models.ForeignKey("telemarketing.ScriptCategory", models.PROTECT, related_name="scripts")
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="scripts")

    def __str__(self) -> str:
        return self.id
    

class OptionObject(TimeStampedModel):
    name = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.pk
    

class Option(TimeStampedModel):
    name = models.CharField(max_length=128)
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="options0")
    functions = models.TextField(null=True, blank=True)
    object = models.ForeignKey(
        "telemarketing.OptionObject", models.SET_NULL, related_name="options", null=True
    )
    register_client = models.BooleanField(default=False)

    @property
    def appel_count(self):
        return self.appeals.count()
    
    def __str__(self) -> str:
        return self.name
    

class CallScript(TimeStampedModel):
    type = models.CharField(max_length=23, unique=True)
    module = models.CharField(max_length=23, choices=CallScriptModuleChoice.choices)
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="call_scripts")
    text = models.TextField()
    is_active = models.BooleanField()
    
    class Meta:
        verbose_name = _("Call Script")
        verbose_name_plural = _("Call Scripts")
    
    def __str__(self) -> str:
        return f"{self.type} {self.module}"
    

class Branch(TimeStampedModel):
    is_main = models.BooleanField(default=True)
    name = models.CharField(max_length=128)
    fax = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    phone = PhoneNumberField(region="UZ")
    email = models.EmailField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name} {self.is_main}"
    

class Process(TimeStampedModel):
    appeal = models.ForeignKey("telemarketing.Appeal", models.PROTECT, related_name="processes")
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="processes")
    branch = models.ForeignKey("telemarketing.Branch", models.PROTECT, related_name="processes")
    products = models.ManyToManyField("telemarketing.Product", "processes")
    is_lead = models.BooleanField(default=False)
    is_agrement = models.BooleanField(default=False)
    is_visit = models.BooleanField(default=False)
    is_scoring = models.BooleanField(default=False)
    is_issuance = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Process")
        verbose_name_plural = -("Processes")
