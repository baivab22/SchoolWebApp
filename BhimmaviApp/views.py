from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Notice, Event, StudentAlumni, Gallery, BlogPost, Testimonial, Contact, Enquiry, Teacher, BODMember, Admission, Introduction, History
from .utils import retrieve_categorywise_gallery
# Home view
def home(request):
    return render(request, 'gallery/gallery_list.html')

class Homeview(TemplateView):
    template_name='home.html'


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        gallery_image_queryset, gallery_video_queryset = retrieve_categorywise_gallery()

        context['notice'] = Notice.objects.all()[:7]
        context['event'] = Event.objects.all()[:3]
        context['last_batch'] = StudentAlumni.objects.first().slc_batch
        context['student_alumni'] = StudentAlumni.objects.filter(slc_batch= context['last_batch'])[:3]
        context['gallery_image'] = gallery_image_queryset[:2]
        context['gallery_video'] = gallery_video_queryset[:2]
        context['blog_post'] = BlogPost.objects.all()[:5]
        context['testimonials'] = Testimonial.objects.all() 
        context['introduction'] = Introduction.objects.first()
        context['teachers'] = BODMember.objects.all()
        message=False
        for message in messages.get_messages(self.request):
            message=message.message
            break
        context['message'] =message

        return context
    

    
def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    recent_post = BlogPost.objects.all()[:5]
    return render(request, 'events/event_details.html',context={'event':event,'recent_post':recent_post})

def event_list(request):
    event = Event.objects.all()
    return render(request, 'events/event_list.html',context={'event':event})


def blogpost_detail(request, pk):
    blogpost = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_post/post_details.html',context={'alumni':blogpost})


def blogpost_list(request):
    blogpost = BlogPost.objects.all()
    return render(request, 'blog_post/post_list.html',context={'blogpost':blogpost})



def alumni_detail(request, pk):
    alumni = StudentAlumni.objects.get(pk=pk)
    return render(request, 'student_alumni/student_alumni_details.html',context={'alumni':alumni})
    


def alumni_list(request):
    # Get all distinct batches
    distinct_batches = StudentAlumni.objects.values_list('slc_batch', flat=True).distinct()
    
    # Filter alumni based on selected batch
    selected_batch = request.GET.get('batch', None)
    if selected_batch:
        alumni = StudentAlumni.objects.filter(slc_batch=selected_batch)
    else:
        alumni = StudentAlumni.objects.all()

    return render(request, 'student_alumni/student_alumni_list.html', {
        'alumni_list': alumni,
        'batches': distinct_batches,
        'selected_batch': selected_batch,
    })


def gallery_category(request):
    gallery_image_queryset, gallery_video_queryset = retrieve_categorywise_gallery()
    context = {
        'gallery_image': gallery_image_queryset,
        'gallery_video': gallery_video_queryset,
    }
    return render(request, 'gallery/gallery_category.html', context)

def gallery_list(request,gallery_title,category):
    gallery_list= Gallery.objects.filter(gallery_title__title=gallery_title,category=category)
    context = {
        'gallery_list':gallery_list
    }

    return render(request,'gallery/gallery_list.html',context)



def testimonial_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials})

def contact(request):
    return render(request, 'contact.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not (name and email and phone and subject and message):
            messages.error(request, 'All fields are required.')
        else:
            try:
                Contact.objects.create(
                    full_name=name,
                    email=email,
                    phone=phone,
                    subject=subject,
                    message=message
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('home')  # Redirect to the same page or another success page

            except Exception as e:
                messages.error(request, f'Error saving your message: {e}')

    return render(request, 'contact.html')


def enquiry(request):
    return render(request, 'enquiry.html')

def enquiry_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        enquiry = request.POST.get('enquiry', '').strip()
        message = request.POST.get('message', '').strip()

        if not (name and email and phone and enquiry and message):
            messages.error(request, 'All fields are required.')
        else:
            try:
                Enquiry.objects.create(
                    full_name=name,
                    phone=phone,
                    email = email,
                    enquiry=enquiry,
                    message=message
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('home')  # Redirect to the same page or another success page

            except Exception as e:
                messages.error(request, f'Error saving your message: {e}')

    return render(request, 'enquiry.html')



def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'BOD/teachers.html',context={'teachers':teachers})

def bod_member(request):
    teachers = BODMember.objects.all()
    return render(request, 'BOD/teachers.html',context={'teachers':teachers, 'bod_member' :True})



def bod_details(request, pk):
    bod_member = BODMember.objects.get(pk=pk)
    return render(request, 'BOD/bod_details.html',context={'bod_details':bod_member})

def admission(request):
    return render(request, 'admission.html')



def admission_view(request):
    if request.method == 'POST':
        # Extract and strip form data
        full_name = request.POST.get('full_name', '').strip()
        date_of_birth = request.POST.get('date_of_birth', '').strip()
        place_of_birth = request.POST.get('place_of_birth', '').strip()
        gender = request.POST.get('gender', '').strip()
        nationality = request.POST.get('nationality', '').strip()
        mother_tongue = request.POST.get('mother_tongue', '').strip()
        religion = request.POST.get('religion', '').strip()
        grade_applied_for = request.POST.get('grade_applied_for', '').strip()
        academic_year = request.POST.get('academic_year', '').strip()
        permanent_address = request.POST.get('permanent_address', '').strip()
        current_address = request.POST.get('current_address', '').strip()
        last_academic_info = request.POST.get('last_academic_info', '').strip()
        co_curricular_activities = request.POST.get('co_curricular_activities', '').strip()
        blood_group = request.POST.get('blood_group', '').strip()
        height = request.POST.get('height', '').strip()
        weight = request.POST.get('weight', '').strip()
        contact_number = request.POST.get('contact_number', '').strip()
        email = request.POST.get('email', '').strip()

        # Validate required fields
        if not (full_name and date_of_birth and place_of_birth and gender and religion and
                nationality and grade_applied_for and academic_year and permanent_address and contact_number and last_academic_info):
            messages.error(request, 'All required fields must be filled.')
        else:
            try:
                # Save the data to the database
                Admission.objects.create(
                    full_name=full_name,
                    date_of_birth=date_of_birth,
                    place_of_birth=place_of_birth,
                    gender=gender,
                    nationality=nationality,
                    mother_tongue=mother_tongue,
                    religion=religion,
                    grade_applied_for=grade_applied_for,
                    academic_year=academic_year,
                    permanent_address=permanent_address,
                    current_address=current_address,
                    last_academic_info=last_academic_info,
                    co_curricular_activities=co_curricular_activities,
                    blood_group=blood_group,
                    height=height,
                    weight=weight,
                    contact_number=contact_number,
                    email=email
                )
                messages.success(request, 'Your admission form has been submitted successfully!')
                return redirect('home')  # Redirect to the same page or another success page
            except Exception as e:
                messages.error(request, f'Error saving your admission form: {e}')

    return render(request, 'admission.html')

def introduction(request):
    introduction = Introduction.objects.first()
    return render(request, 'introduction.html',context={'introduction':introduction})



def history(request):
    history = History.objects.all()
    return render(request, 'history.html',context={'history':history})