from django.contrib import admin
from .models import Dog, DogBreed, DogUser, Breed, CustomUser, Activity, ActivityList, WeightChange, HeightChange

admin.site.register(Dog)
admin.site.register(DogBreed)
admin.site.register(DogUser)
admin.site.register(Breed)
admin.site.register(CustomUser)
admin.site.register(Activity)
admin.site.register(ActivityList)
admin.site.register(WeightChange)
admin.site.register(HeightChange)



