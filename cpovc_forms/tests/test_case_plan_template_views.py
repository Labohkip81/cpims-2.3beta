from datetime import timedelta

from django.core.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import RequestFactory
from django.utils import timezone

from model_mommy import mommy

from cpovc_registry.models import RegPerson
from cpovc_forms.models import OVCCareEvents, OVCCareCasePlan
from cpovc_ovc.models import OVCFacility, OVCHHMembers, OVCHouseHold

user_model = get_user_model()

class TestOVCCareCasePlanViews(TestCase):
	"""
		Class to test OVCCareCasePlan views.
	"""
	def setUp(self, *args, **kwargs):
		"""
			Set up all the tests
		"""
        self.factory = RequestFactory()
        self.person = mommy.make(RegPerson, surname='Doe')
        self.url = reverse('case_plan_template', kwargs={'id': self.person.id})
        person_1 = mommy.make(RegPerson, surname='test')
        user = mommy.make(user_model, username='test_user', reg_person=person_1)
        user.set_password('test_user')
        user.save()
        self.client.login(username='test_user', password='test_user')

    def test_case_plan_template_get(self):
        event = mommy.make(OVCCareEvents, person=self.person)
        facility = mommy.make(OVCFacility, facility_name='')
        mommy.make(
            OVCHIVRiskScreening, event=event, facility=facility,
            person=self.person)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'forms/new_hivscreeningtool.html')
