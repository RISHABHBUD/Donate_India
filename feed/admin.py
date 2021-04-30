from feed.models import Add_user, DonateBlood, DonateClothes, DonateFood, DonateStationary, DonateTime, Postimg
from django.contrib import admin

# Register your models here.
admin.site.register(Add_user)
admin.site.register(Postimg)
admin.site.register(DonateClothes)
admin.site.register(DonateFood)
admin.site.register(DonateStationary)
admin.site.register(DonateTime)
admin.site.register(DonateBlood)
