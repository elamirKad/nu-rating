from django_cron import CronJobBase, Schedule
from rating.extract import get_profs_and_courses
from rating.models import Professor, Course, CourseDescription
from rating.courses_details_scrapper import get_course_details
from django.conf import settings
from django.core.mail import send_mail
import time


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every week

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'rating.my_cron_job'

    def do(self):
        print("start")
        start_time = time.time()
        subject = 'Cronjob starts'
        message = f'Hello me, your/my cronjob activated'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['elamirkad@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        new_courses = []
        response_data = get_profs_and_courses(1)
        response_data.update(get_profs_and_courses(0))
        for r in response_data:
            try:
                prof = Professor.objects.get(name=r)
            except:
                prof = None
            if prof:
                for course in response_data[r]:
                    course = course.replace('/', ' OR ')
                    try:
                        c = Course.objects.get(name=course)
                    except:
                        c = None
                    if c:
                        c.professors.add(prof)
                        print("Added course", course, " to the prof ", r)
                    else:
                        c = Course(name=course)
                        c.save()
                        c.professors.add(prof)
                        new_courses.append(c.name)
                        print("Created course ", course, " and added to the prof ", r)
            else:
                prof = Professor(name=r)
                prof.save()
                print("Created ", r)
            print(response_data[r], r)


        for newcourse in new_courses:
            print("Processing", newcourse)
            data = get_course_details(newcourse)
            course = Course.objects.get(name=newcourse)
            try:
                course_desc = CourseDescription.objects.get(course=newcourse)
            except:
                course_desc = None
            if not course_desc:
                try:
                    c = CourseDescription(course=course, title=data['TITLE'], ects=int(data['CRECTS']),
                                        school=data['SCHOOL'], department=data['DEPARTMENT'],
                                        description=data['SHORTDESC'],
                                        prereq=data['PREREQ'], coreq=data['COREQ'], antireq=data['ANTIREQ'])
                    c.save()
                except:
                    pass
            else:
                print("Course exists")
            elapsed_time = time.time() - start_time
        send_mail("Cronjob ended", f"Everything fine, cronjob completed but check it out. It took {elapsed_time} seconds", email_from, recipient_list)