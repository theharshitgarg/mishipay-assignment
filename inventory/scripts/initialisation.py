from inventory import models

vendor = models.Vendor.objects.create(
    name="Burton"
)
vendor.save()

