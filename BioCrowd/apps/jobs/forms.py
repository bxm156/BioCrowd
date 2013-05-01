from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field

from pycrowd.jobs.forms import CrowdsourceJobForm

class CrispyCrowdsourceJobForm(CrowdsourceJobForm):
    
    def __init__(self, *args, **kwargs):
        super(CrispyCrowdsourceJobForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-create-job'
        self.helper.form_method = 'post'
        self.helper.form_action = '/jobs/create/'
        self.helper.add_input(Submit('submit', 'Create Job'))
        self.helper['name'].wrap(Field, css_class="input-xxlarge")
        self.helper['instructions'].wrap(Field, css_class="input-xxlarge")