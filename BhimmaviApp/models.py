from django.db import models
from BhimmaviApp.softdelete_manager import SoftDeleteModel
from django.contrib.auth.models import User  # Assuming 'written_by' references a user in your system
from django.core.validators import MinValueValidator, MaxValueValidator
from django.templatetags.static import static
from django.core.exceptions import ValidationError


# Menus model with submenu relationship and soft deletion
class Menus(SoftDeleteModel):
    name = models.CharField(max_length=255)  # Menu item name
    link = models.CharField(max_length=255)  # Link for the menu item
    submenu = models.ForeignKey(
        'self',  # Links to the same model (Menus) for hierarchical relationship
        on_delete=models.CASCADE,  # Deletes the submenu if its parent is deleted
        related_name='submenus',  # Access submenus using "menu_item.submenus"
        null=True,  # Allows the submenu field to be empty for top-level items
        blank=True,  # Makes the submenu field optional in forms
        help_text="If this menu item is a submenu, select its parent here. Leave blank if this is a top-level item."
    )
    priority = models.IntegerField()  # Field for ordering menu items (e.g., display order)

    def _str_(self):
        return self.name  # String representation of the menu item (its name)

    def get_submenus(self):
        """Get all submenus related to this menu item."""
        return self.submenus.all()  # Access submenus through the related_name 'submenus'

    class Meta:
        ordering = ['-priority']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'




class Notice(SoftDeleteModel):
    NOTICE_TYPES = [
        ('General', 'General'),
        ('Event', 'Event'),
        ('Holiday', 'Holiday'),
        ('Urgent', 'Urgent'),
    ]
    
    # created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='notices/', blank=True, null=True)
    type = models.CharField(max_length=10, choices=NOTICE_TYPES, default='General')

    class Meta:
        ordering = ['-event_date', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.get_type_display()}"
    


class Event(SoftDeleteModel):
    EVENT_CATEGORIES = [
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Competition', 'Competition'),
        ('Festival', 'Festival'),
        ('Others', 'Others'),
    ]
    
    event_date = models.DateField()
    event_time = models.TimeField()  # Added time field
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)  # Added address field
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES, default='Others')

    class Meta:
        ordering = ['-event_date', '-event_time']

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
    



class StudentAlumni(SoftDeleteModel):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='alumni/', blank=True, null=True)
    detail = models.TextField()
    slc_batch = models.CharField(max_length=20)  # e.g., "Batch 2015"
    current_address = models.CharField(max_length=255)
    current_position = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['-slc_batch']  # Order by batch first, then by name

    def __str__(self):
        return f"{self.name} ({self.slc_batch}) - {self.gender}"
    


class GalleryTitle(SoftDeleteModel):
    title = models.CharField(max_length=255)  # Title of the gallery

    class Meta:
        verbose_name = 'Gallery Title'
        verbose_name_plural = 'Gallery Titles'

    def __str__(self):
        return self.title



class Gallery(SoftDeleteModel):
    CATEGORY_CHOICES = [
        ('Photos', 'Photos'),
        ('Videos', 'Videos'),
    ]

    gallery_title = models.ForeignKey(GalleryTitle, on_delete=models.CASCADE, related_name='galleries')
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)  # For photos or video thumbnails
    video_link = models.CharField(max_length=250)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name = 'Gallery Item'
        verbose_name_plural = 'Gallery Items'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.category} - {self.gallery_title.title}"

    def total_image_count(self):
        """Returns the total count of images in the 'Photos' category."""
        return Gallery.objects.filter(category='Photos').count()

    def total_video_count(self):
        """Returns the total count of videos in the 'Videos' category."""
        return Gallery.objects.filter(category='Videos').count()

    def categorywise_image_count(self):
        """Returns the count of images in the 'Photos' category for a specific gallery title."""
        return Gallery.objects.filter(gallery_title=self.gallery_title, category='Photos').count()

    def categorywise_video_count(self):
        """Returns the count of videos in the 'Videos' category for a specific gallery title."""
        return Gallery.objects.filter(gallery_title=self.gallery_title, category='Videos').count()
    



class BlogPost(SoftDeleteModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    written_by = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_posts/', blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-date']  # Latest posts first

    def __str__(self):
        return self.title

    def summary(self):
        """Returns a short summary of the content (first 100 characters)."""
        return self.content[:100] + '...' if len(self.content) > 100 else self.content





class Testimonial(SoftDeleteModel):
    STUDENT = 'Student'
    TEACHER = 'Teacher'
    PARENT = 'Parent'
    BOARD_MEMBER = 'BoardMember'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (PARENT, 'Parent'),
        (BOARD_MEMBER, 'Board Member'),
    ]

    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    content = models.TextField()
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Rating between 1 and 5"
    )

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['name']  # Order alphabetically by name

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"

    def short_content(self):
        """Returns a short version of the content (first 50 characters)."""
        return self.content[:50] + '...' if len(self.content) > 50 else self.content



class Contact(SoftDeleteModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"



class Enquiry(SoftDeleteModel):
    SERVICES = 'services'
    ADMISSION = 'admission'

    ENQUIRY_CHOICES = [
        (SERVICES, 'Services'),
        (ADMISSION, 'Admission'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    enquiry = models.CharField(max_length=10, choices=ENQUIRY_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_enquiry_display()}"



class Teacher(SoftDeleteModel):
    # Basic information
    name = models.CharField(max_length=100)  # Teacher's full name
    title = models.CharField(max_length=50)  # Job title or designation
    image = models.ImageField(upload_to='teachers/images/')  # Profile picture

    # Social media links
    facebook = models.URLField(blank=True, null=True)  # Facebook URL
    instagram = models.URLField(blank=True, null=True)  # Instagram URL
    twitter = models.URLField(blank=True, null=True)  # Twitter URL

    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return self.image.url 
        return static('assets/image/avatar.png')
    


class BODMember(SoftDeleteModel):
    # Basic information
    name = models.CharField(max_length=100)  # Full name of the board member
    image = models.ImageField(upload_to='bod_members/images/', blank=True, null=True)  # Profile picture
    title = models.CharField(max_length=50)  # Job title or designation
    
    # Introduction and details
    short_intro = models.CharField(max_length=255)  # Brief introduction
    details = models.TextField()  # Detailed biography or description
    experience = models.PositiveIntegerField()  # Years of experience

    # Contact information
    email = models.EmailField()  # Email address
    website = models.URLField(blank=True, null=True)  # Personal or professional website

    message = models.TextField()  # message for home
    
    # Social media links
    facebook = models.URLField(blank=True, null=True)  # Facebook URL
    instagram = models.URLField(blank=True, null=True)  # Instagram URL
    twitter = models.URLField(blank=True, null=True)  # Twitter URL
    
    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return self.image.url
        return static('assets/image/avatar.png')

    


class Admission(SoftDeleteModel):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    # Personal Information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    mother_tongue = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    grade_applied_for = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=10)
    permanent_address = models.TextField()
    current_address = models.TextField()

    # Last Academic Information
    last_academic_info = models.TextField()

    # Co-Curricular Activities
    co_curricular_activities = models.TextField(blank=True, null=True)

    # Medical Information
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  

    # Applicant’s Contact Details
    contact_number = models.CharField(max_length=15)
    email = models.EmailField( blank=True, null=True)

    # Automatically capture the created date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - Grade {self.grade_applied_for}"



class Introduction(SoftDeleteModel):
    # Introduction Section
    introduction_text = models.TextField()
    introduction_image1 = models.ImageField(upload_to='images/introduction/', null=True, blank=True)
    introduction_image2 = models.ImageField(upload_to='images/introduction/', null=True, blank=True)
    introduction_image3 = models.ImageField(upload_to='images/introduction/', null=True, blank=True)
    introduction_home_image1 = models.ImageField(upload_to='images/introduction_home/', null=True, blank=True)
    introduction_home_image2 = models.ImageField(upload_to='images/introduction_home/', null=True, blank=True)

    # About Us Section
    vision_text = models.TextField()
    vision_image = models.ImageField(upload_to='images/about_us/', null=True, blank=True)
    
    # Mission Section
    mission_text = models.TextField()
    mission_image = models.ImageField(upload_to='images/mission/', null=True, blank=True)

    # Additional Information
    years_of_experience = models.CharField(max_length=5, blank=True, null=True)
    student_each_year = models.CharField(max_length=10, blank=True, null=True)
    no_of_teacher = models.CharField(max_length=5, blank=True, null=True)
    no_of_awards = models.CharField(max_length=5, blank=True, null=True)


    def __str__(self):
        return f"Introduction  created Date : {self.created_at}"

    class Meta:
        verbose_name = "Introduction"
        verbose_name_plural = "Introduction"
        ordering=['-created_at']


class History(SoftDeleteModel):
    history_text = models.TextField()
    history_year = models.DateField()  # Stores only the year

    def __str__(self):
        return f"{self.history_text[:50]} ({self.history_year})"
    
    class Meta:
        ordering = ['-history_year']
