
from datetime import timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from model_mommy import mommy

from cpovc_registry.models import RegPerson
from cpovc_forms.models import OVCCareEvents, OVCHIVRiskScreening
from cpovc_ovc.models import OVCFacility, OVCHHMembers, OVCHouseHold

user_model = get_user_model()


class TestHivScreenToolViews(TestCase):
    def setUp(self, *args, **kwargs):
        self.person = mommy.make(RegPerson, surname='John')
        self.url = reverse(
            'new_hivscreeningtool', kwargs={'id': self.person.id})
        person_2 = mommy.make(RegPerson, surname='test')
<<<<<<< HEAD
        user = mommy.make(
            user_model, username='test_user', reg_person=person_2)
        user.set_password('test_user')
        user.save()
        self.client.login(username='test_user', password='test_user')

    def test_new_hivscreeningtool_get(self):
        event = mommy.make(OVCCareEvents, person=self.person)
        facility = mommy.make(OVCFacility, facility_name='Kenyatta')
        mommy.make(
            OVCHIVRiskScreening, event=event, facility=facility,
=======
        self.user = mommy.make(
            user_model, username='test_user', reg_person=person_2)
        self.user.set_password('test_user')
        self.user.is_staff = True
        self.user.save()
        self.client.login(username='test_user', password='test_user')
        super(TestHivScreenToolViews, self).setUp(*args, **kwargs)

    def test_new_hivscreeningtool_get(self):
        event = mommy.make(
            OVCCareEvents, person=self.person, event_type_id='HRST')
        facility = mommy.make(
            OVCFacility, facility_name='Kenyatta', facility_code=12000)
        mommy.make(
            OVCHIVRiskScreening, event=event,
            facility_code=facility.facility_code,
>>>>>>> origin/master
            person=self.person)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'forms/new_hivscreeningtool.html')

<<<<<<< HEAD
    def test_new_hivscreeningtool_post_invalid_choices(self):
        now = timezone.now()
        date_of_assessment = now - timedelta(days=300)
        facility = mommy.make(
            OVCFacility, facility_name='Kenyatta National Hospital')

        post_data = {
            'HIV_RA_1A': date_of_assessment,
            'HIV_RS_01': 'NO',
            'HIV_RS_02': 'ANNO',
            'HIV_RS_03': 'NO',
            'HIV_RS_03A': 'NO',
            'HIV_RS_04': 'NO',
            'HIV_RS_05': 'NO',
            'HIV_RS_06': 'NO',
            'HIV_RS_07': 'NO',
            'HIV_RS_08': 'NO',
            'HIV_RS_09': 'NO',
            'HIV_RS_10': 'NO',
            'HIV_RS_11': 'NO',
            'HIV_RS_14': 'NO',
            'HIV_RS_15': now - timedelta(days=100),
            'HIV_RS_16': 'NO',
            'HIV_RS_17': now - timedelta(days=90),
            'HIV_RS_18': 'NO',
            'HV_RS_18A': 'lorem ipsum',
            'HIV_RS_18B': '2',
            'HIV_RS_19': now - timedelta(days=80),
            'HIV_RS_21': 'NO',
            'HIV_RS_22': now - timedelta(days=70),
            'HIV_RS_23': 'ANNO',
            'HIV_RS_24': now - timedelta(days=60),
            'HIV_RA_3Q6': facility.id
        }
        person = mommy.make(RegPerson, surname='John')

        # create a house hold to attach the child
        house_hold = mommy.make(OVCHouseHold, head_person=person)

        # Add the OVC to a house hold
        mommy.make(OVCHHMembers, person=self.person, house_hold=house_hold)

        # Create an event
        mommy.make(OVCCareEvents, person=self.person)
        response = self.client.post(self.url, post_data)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'forms/new_hivscreeningtool.html')
        self.assertContains(
            response,
            'Select a valid choice. NO is not one of the available choices'
        )

=======
>>>>>>> origin/master
    def test_new_hivscreeningtool_post_valid_choices(self):
        now = timezone.now()
        date_of_assessment = now - timedelta(days=300)
        facility = mommy.make(
<<<<<<< HEAD
            OVCFacility, facility_name='Kenyatta National Hospital')

        post_data = {
            'HIV_RA_1A': date_of_assessment,
            'HIV_RS_01': 'ANNO',
            'HIV_RS_02': 'ANNO',
            'HIV_RS_03': 'ANNO',
            'HIV_RS_03A': 'ANNO',
            'HIV_RS_04': 'ANNO',
            'HIV_RS_05': 'ANNO',
            'HIV_RS_06': 'ANNO',
            'HIV_RS_07': 'ANNO',
            'HIV_RS_08': 'ANNO',
            'HIV_RS_09': 'ANNO',
            'HIV_RS_10': 'ANNO',
            'HIV_RS_11': 'ANNO',
            'HIV_RS_14': 'ANNO',
            'HIV_RS_15': now - timedelta(days=100),
            'HIV_RS_16': 'ANNO',
            'HIV_RS_17': now - timedelta(days=90),
            'HIV_RS_18': 'ANNO',
            'HV_RS_18A': 'lorem ipsum',
            'HIV_RS_18B': '2',
            'HIV_RS_19': now - timedelta(days=80),
            'HIV_RS_21': 'ANNO',
            'HIV_RS_22': now - timedelta(days=70),
            'HIV_RS_23': 'ANNO',
            'HIV_RS_24': now - timedelta(days=60),
=======
            OVCFacility, facility_name='Kenyatta National Hospital',
            facility_code=12000)
        mommy.make(OVCCareEvents, person=self.person, event_type_id='HRST')
        post_data = {
            'HIV_RA_1A': str(date_of_assessment)[0:10],
            'HIV_RS_01': 'AYES',
            'HIV_RS_02': 'AYES',
            'HIV_RS_03': 'AYES',
            'HIV_RS_03A': 'AYES',
            'HIV_RS_04': 'AYES',
            'HIV_RS_05': 'AYES',
            'HIV_RS_06': 'AYES',
            'HIV_RS_07': 'AYES',
            'HIV_RS_08': 'AYES',
            'HIV_RS_09': 'AYES',
            'HIV_RS_10': 'AYES',
            'HIV_RS_11': 'AYES',
            'HIV_RS_14': 'AYES',
            'HIV_RS_15': str(now - timedelta(days=100))[0:10],
            'HIV_RS_16': 'AYES',
            'HIV_RS_17': str(now - timedelta(days=90))[0:10],
            'HIV_RS_18': 'AYES',
            'HIV_RS_18A': 'lorem ipsum',
            'HIV_RS_18B': '2',
            'HIV_RS_19': str(now - timedelta(days=80))[0:10],
            'HIV_RS_21': 'AYES',
            'HIV_RS_22': str(now - timedelta(days=70))[0:10],
            'HIV_RS_23': 'AYES',
            'HIV_RS_24': str(now - timedelta(days=60))[0:10],
>>>>>>> origin/master
            'HIV_RA_3Q6': facility.id
        }
        person = mommy.make(RegPerson, surname='John')

        # create a house hold to attach the child
        house_hold = mommy.make(OVCHouseHold, head_person=person)

        # Add the OVC to a house hold
        mommy.make(OVCHHMembers, person=self.person, house_hold=house_hold)

        # Create an event
<<<<<<< HEAD
        mommy.make(OVCCareEvents, person=self.person)
        response = self.client.post(self.url, post_data)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'forms/new_hivscreeningtool.html')
        self.assertContains(response, 'lorem ipsum')
=======
        mommy.make(OVCCareEvents, person=self.person, event_type_id='HRST')

        response = self.client.post(self.url, post_data, follow=True)
        self.assertEqual(200, response.status_code)
        redirect_url = reverse('ovc_view', kwargs={'id': self.person.id})
        response = self.client.get(redirect_url)
        self.assertIn('Permission denied', response.content)
>>>>>>> origin/master
