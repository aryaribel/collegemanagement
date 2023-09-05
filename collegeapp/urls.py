from django.urls import path
from collegeapp import views
from django.contrib import admin


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('signin/',views.signin,name="signin"),
    path('admin_home_page',views.admin_home_page,name="admin_home_page"),
    path('teacher_home_page',views.teacher_home_page,name="teacher_home_page"),
    path("CoursePage",views.CoursePage,name="CoursePage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("StudentPage",views.StudentPage,name="StudentPage"),
    path("AddStudent",views.AddStudent,name="AddStudent"),
    path("StudentDetails",views.StudentDetails,name="StudentDetails"),
    path("logout",views.logout,name="logout"),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path("teacherdetails",views.teacherdetails,name="teacherdetails"),
    path("s_details/<int:pk>",views.s_details,name="s_details"),
    path('deleteteacherpage/<int:pk>',views.deleteteacherpage,name='deleteteacherpage'),
    path('delete_teacher/<int:pk>',views.delete_teacher,name='delete_teacher'),
    path('remove_image/<int:pk>',views.remove_image,name="remove_image"),
    path('updatedetails/<int:pk>',views.updatedetails,name="updatedetails"),
    path('update_details/<int:pk>',views.update_details,name="update_details"),
    path('showdetails/<int:pk>',views.showdetails,name='showdetails'),
 
       
       

]