# from rest_framework import serializers
#
# from .models import Project
#
#
# class CreateProjectSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Project()
#         fields = ['name', 'desc', 'status_choice', 'users',]
#
#     def save(self, **kwargs):
#         project = Project()
#         project.name = self.validated_data['name']
#         project.desc = self.validated_data['desc']
#         project.status_choice = self.validated_data['status_choice']
#         project.users(self.validated_data['users'])
#         project.save()
#         return project
#
#
# # class CreateProjectUserSerializer(serializers.ModelSerializer):
# #
# #     class Meta:
# #         model = Project()
# #         fields = ['name', 'desc', 'status_choice', 'users',]
# #
# #     def save(self, **kwargs):
# #         project = Project()
# #         project.name = self.validated_data['name']
# #         project.desc = self.validated_data['desc']
# #         project.status_choice = self.validated_data['status_choice']
# #         project.users(self.validated_data['users'])
# #         project.save()
# #         return project
