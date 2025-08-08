from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Menus, Notice, Event, StudentAlumni, GalleryTitle, Gallery, BlogPost, Testimonial, Contact, Enquiry, Teacher, BODMember, Admission, Introduction, History



class MenusAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'priority', 'submenu', 'created_at', 'modified_at')  # Fields to display in the list view
    search_fields = ('name', 'link')  # Enable search by name or link
    list_filter = ('submenu',)  # Filter by submenu (parent-child relation)
    ordering = ('priority',)  # Default ordering by priority
    
    # Make created_at, modified_at, and deleted_at read-only
    readonly_fields = ('created_at', 'modified_at', 'deleted_at')

    # Customize the form to make the submenu field more user-friendly (display as a dropdown)
    fieldsets = (
        (None, {
            'fields': ('name', 'link', 'submenu', 'priority')
        }),
        ('Dates', {
            'fields': ('created_at', 'modified_at', 'deleted_at'),
            'classes': ('collapse',)  # Hide the date fields by default
        }),
    )

# Register the customized MenusAdmin
admin.site.register(Menus, MenusAdmin)

admin.site.register(Notice, )

admin.site.register(Event,)

admin.site.register(StudentAlumni, )

admin.site.register(GalleryTitle, )

admin.site.register(Gallery, )

admin.site.register(BlogPost, )

admin.site.register(Testimonial, )

admin.site.register(Contact,)

admin.site.register(Enquiry,)


admin.site.register(Teacher,)

admin.site.register(BODMember,)

admin.site.register(Admission,)

admin.site.register(Introduction,)

admin.site.register(History,)
