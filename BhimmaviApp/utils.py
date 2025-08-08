from .models import Gallery


def retrieve_categorywise_gallery():
    gallery_image = Gallery.objects.filter(category='Photos')

    gallery_video = Gallery.objects.filter(category='Videos')
    image_title_list =[]
    video_title_list = []

    for image in gallery_image:
        gallery_title = image.gallery_title
        if gallery_title not in image_title_list:
            image_title_list.append(gallery_title)

    gallery_image_queryset = []

    for category in image_title_list:
        gallery_image_queryset.append({'category':category, 'image_count':gallery_image.filter(gallery_title__title=category).count(),'thumbnail':gallery_image.filter(gallery_title__title=category).first().image.url})

    for video in gallery_video:
        gallery_title = video.gallery_title
        if gallery_title not in video_title_list:
            video_title_list.append(gallery_title)

    gallery_video_queryset = []

    for category in video_title_list:
        gallery_video_queryset.append({'category':category, 'video_count':gallery_video.filter(gallery_title__title=category).count(),'thumbnail':gallery_video.filter(gallery_title__title=category).first().image.url})

    return gallery_image_queryset, gallery_video_queryset
