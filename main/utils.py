from .models import Resume 
import random
import string 

ID_LENGTH = 10
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
NUMBER = string.digits 
ALL = LOWER + UPPER + NUMBER 
    

def get_resume_id():
    resume_id_set = [ resume.resumeid for resume in Resume.objects.all()]
    id = ''.join(random.sample(ALL,ID_LENGTH))
    if id in resume_id_set:
        get_resume_id()
    else:
        return id 

