# polls/api.py
import json
#from django.core.serializers import json
from django.core.serializers.json import DjangoJSONEncoder
#from django.utils import simplejson 
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource 
from Admission.models import Students
from tastypie import fields 
#from Admission.models import Students
from tastypie.authorization import Authorization
class PrettyJSONSerializer(Serializer): 
    json_indent = 4 
    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return json.dumps(data, cls=DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 

class StudentsResource(ModelResource): 
    class Meta:
        queryset=Students.objects.all()
        resource_name='entry'
        serializer = PrettyJSONSerializer()
        authorization=Authorization()
 


#class StudentsResource(ModelResource): 
    #choices = fields.ToManyField('polls.api.ChoiceResource', 'choice_set', related_name='poll', full=True) 
    
  #  class Meta: 
   #     queryset = Students.objects.all() 
    #    serializer = PrettyJSONSerializer() 
     #   authorization = Authorization()
    
