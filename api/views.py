from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class aboutView(View):
    def get(self,request):
        data={
            'ID':1,
            'FULL NAME':'john',
            'PROFESSIONAL TITTLE':'backend developer',
            'BIO':'backend developer with 1 yera of experience',
            'EMAIL':'john123@gmail.com',
            'contact':'91475563566',
            'DOB':'12-2-2005',
            'GITHUB URL':'aghuu89000',
            'LINKDIN URL':'ghuuiokkk'
        }
        return JsonResponse(data)

class EducationView(View):
    def get (self,request):
        data={
            'ID':101,
            'INSTITUTION':'stc',
            'degree':'bsc',
            'university':'mg university',
            'location':'ernakulam',
            'start year':'2018',
            'end year':'2026',
            'grade':'A',
            'discription':'bsc computer science'
        }
        return JsonResponse(data)
class projectView(View):
    def get(self,request):
        data=[
            {
                'ID':201,
                'title':'SMART GYM',
                'short discription':'a fitness management website',
                'long discription':'a fitness management website with user authentication and payment',
                'live url':'https://smartgym.com',
                'github url':'https://github.com/smartgym',
                'image url':'https://smartgym.com/image.jpg',
                'featured':True


            },
            {
                'ID':202,
                'title':'PG management system',
                'short discription':'a pg management system',
                'long discription':'a pg management system with user authentication and payment',
                'live url':'https://pgmanagement.com',
                'github url':'https://github.com/pgmanagement',
                'image url':'https://pgmanagement.com/image.jpg',
                'featured':True
            },
            {
                'ID':203,
                'title':'E-commerce website',
                'short discription':'an online shopping platform',
                'long discription':'an online shopping platform with user authentication and payment',
                'live url':'https://ecommerce.com',
                'github url':'https://github.com/ecommerce',
                'image url':'https://ecommerce.com/image.jpg',
                'featured':True
            }
        ]
        return JsonResponse(data,safe =False)
class SkillsView(View):
    def get(self,request):
        skill=[
            {
                'id':502,
                'skillname':'python',
                'category':'frontend',
                'proficiency' :'intermediate',
                'years of experience':1,

            },
            {
                'id':504,
                'skillname':'java',
                'category':'backend',
                'proficiency':'beginer',
                'years of experience':0,

            },
            {
                'id':506,
                'skillname':'javascript',
                'category':'frontend',
                'proficiency':'beginer',
                'years of experience':0

            }
        ]
        return JsonResponse(skill,safe=False)
class ExperienceView(View):
    def get(self,request):
        data=[
            {
                'id'               :805,
                'job title'        :'develeoper',
                'company name'     :'hj4',
                'location'         :'ernakulam',
                'employement type' :'full time',
                'start date'       :'2022-02-09',
                'end date'         :'2023-02-09',
                'currently working':True,
                'description'      :'working as a backend developer'

            },
            {
                'id'    :805,
                'job title'        :'develeoper',
                'company name'     :'klo',
                'location'         :'ernakulam',
                'employement type' :'full time',
                'start date'       :'2025-05-01',
                'end date'         :'2026-09-01',
                'currently working':True,
                'description'      :'working as a frontend developer'

            }
        ]
        return JsonResponse(data,safe=False)
class CertificationView(View):
    def get(self,request):
        data=[
           {
                'id':211,
                'certification name':'python',
                'organization name':'ors',
                'issued year':'2022'
           },
           { 'id':211,
               'certification name':'python',
               'organization name':'ors',
               'issued year':'2022'
           }
        ]
        return JsonResponse(data,safe=False)
class ServicesView(View):
    def get(self,request):
        data=[
           {
                'id':504,
                'service name':'web development',
                'description':'a web development service',
                'technologies':[HTML,CSS]
           },
            {
                'id':506,
                'service name':'web development',
                'description':'a web development service',
                'technologies':[HTML,CSS]
            }
        ]
        return JsonResponse(data,safe=False)