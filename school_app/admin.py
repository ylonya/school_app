from django.contrib import admin

from school_app.models import (
    Employee,
    Pupil,
    Group,
    Parent,
    Application, 
    Document,
)


class DocumentAdmin(admin.ModelAdmin):
    def my_parent(self, obj):
        return obj.pupil
    def my_emp(self, obj):
        return obj.employee
    def my_pupil(self, obj):
        return obj.pupil
    
    
    my_parent.short_description = 'Родитель'
    my_emp.short_description = 'Сотрудник'
    my_pupil.short_description = 'Ребёнок'

    list_display = ('id', 'my_parent', 'my_pupil', 'my_emp', 'status', 'date')

    search_fields = ('date','pupil__id', 'pupil__last_name_pupil', 
                     'pupil__middle_name_pupil', 'pupil__first_name_pupil', 'parent__id', 
                     'parent__last_name_parent', 'parent__middle_name_parent', 
                     'parent__first_name_parent', 'employee__id',
                     'employee__last_name_emp', 'employee__middle_name_emp', 
                     'employee__first_name_emp')



class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name_pupil', 'middle_name_pupil', 
                    'first_name_pupil', 'date_birth_pupil', 'date_reception')
    
    search_fields = ('id', 'last_name_pupil', 'middle_name_pupil', 
                    'first_name_pupil')
    

class ParentAdmin(admin.ModelAdmin):
    # list_display = ('id', 'pupil', 'last_name_parent', 'middle_name_parent', 
    #                 'first_name_parent', 'date_birth_parent', 
    #                 'passport_detail_parent', 'address_parent', 'number_parent')
    #метод для поиска из связных таблиц
    def my_pupil(self, obj):
        return obj.pupil
    
    my_pupil.short_description = 'Ребёнок'
    list_display = ('id', 'my_pupil', 'last_name_parent', 'middle_name_parent', 
                     'first_name_parent', 'date_birth_parent', 
                    'passport_detail_parent', 'address_parent', 'number_parent')
    #поля для поиска РЕБЕНКА У РОДИТЕЛЕЙ и РОДИТЕЛЯ
    search_fields = ('pupil__id', 'pupil__last_name_pupil', 'pupil__middle_name_pupil', 
                     'pupil__first_name_pupil', 'id', 
                     'last_name_parent', 'middle_name_parent', 'first_name_parent')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name_emp', 'middle_name_emp', 
                    'first_name_emp', 'date_birth_emp', 'email_emp', 
                    'number_emp', 'passport_detail_emp', 'post', 'address_emp')
    
    search_fields = ('id', 'last_name_emp', 'middle_name_emp', 'first_name_emp')


class ApplicationAdmin(admin.ModelAdmin):
    def my_parent(self, obj):
        return obj.parent
    def my_emp(self, obj):
        return obj.employee
    
    my_parent.short_description = 'Родитель'
    my_emp.short_description = 'Сотрудник'
    
    list_display = ('id','my_emp', 'my_parent', 'status', 'date')
    search_fields = ('id', 'employee__last_name_emp', 'employee__middle_name_emp', 
                     'employee__first_name_emp',
                     'parent__id', 'employee__id','parent__last_name_parent', 
                     'parent__middle_name_parent', 'parent__first_name_parent' )


class GroupAdmin(admin.ModelAdmin):
    
    def my_pupil(self, obj):
        return obj.pupil
    def my_emp(self, obj):
        return obj.employee
    
    my_pupil.short_description = 'Ребёнок'
    my_emp.short_description = 'Воспитатель'

    list_display = ('id', 'my_pupil', 'my_emp', 'bias', 'count')

    search_fields = ('id','pupil__id', 'pupil__last_name_pupil', 'pupil__middle_name_pupil', 
                     'pupil__first_name_pupil', 
                     'employee__id', 'employee__last_name_emp', 'employee__middle_name_emp', 
                     'employee__first_name_emp', 'bias' )


admin.site.register(Pupil, PupilAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Group, GroupAdmin)