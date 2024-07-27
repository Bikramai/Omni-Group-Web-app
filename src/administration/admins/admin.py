from django.contrib import admin
from .models import (
    PropertyTag, PropertyFeature, PropertyType, Property, PropertyImage, City, State, PropertyVideo, PropertyFloorPlan
)


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'is_active', 'created_on']


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state', 'zip_code', 'is_active', 'created_on']


class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_on']


class PropertyTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_on']


class PropertyFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'is_active', 'created_on']


class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'property', 'is_active', 'created_on']


class PropertyFloorPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'bed_rooms', 'bath_rooms', 'property', 'price_start', 'price_end', 'is_active', 'created_on']


class PropertyVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'youtube_video_id', 'property', 'is_active', 'created_on']


class FloorPlanInline(admin.TabularInline):
    model = PropertyFloorPlan
    fields = ['price_start', 'price_end', 'size_start', 'size_end', 'bed_rooms', 'bath_rooms']
    extra = 0


class ImageInline(admin.TabularInline):
    model = PropertyImage
    fields = ['image', 'is_active']
    extra = 0


class VideoInline(admin.TabularInline):
    model = PropertyVideo
    fields = ['youtube_video_id', 'is_active']
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price_start', 'price_end', 'property_type',
        'property_id', 'status', 'is_active', 'created_on'
    ]

    fieldsets = (
        (None, {'fields': ('name', 'property_type', 'property_id', 'slug')}),
        ('Pricing', {'fields': ('price_start', 'price_end')}),
        ('Content', {'fields': ('content',)}),
        ('Main Image', {'fields': ('image',)}),
        ('Main Video', {'fields': ('youtube_video_id',)}),
        ('Address', {'fields': ('address', 'city', 'lat', 'long')}),
        ('Downloadable Files', {'fields': ('price_list_file', 'floor_map_file')}),
        ('Tags and Features', {'fields': ('tags', 'features')}),
        ('Floor Payment', {'fields': ('floor_payment_image', 'floor_payment_file', 'floor_payment_description')}),
        ('Floor Design', {'fields': ('floor_design_image', 'floor_design_file', 'floor_design_description')}),
        ('Permissions', {
            'fields': ('status', 'is_active'),
        }),
    )

    list_filter = ['property_type', 'status', 'is_active']
    search_fields = ['name', 'property_id']
    inlines = [
        VideoInline, ImageInline
    ]


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(PropertyTag, PropertyTagAdmin)
admin.site.register(PropertyFloorPlan, PropertyFloorPlanAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(PropertyFeature, PropertyFeatureAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(PropertyVideo, PropertyVideoAdmin)
admin.site.register(Property, PropertyAdmin)
