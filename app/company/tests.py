from django.test import TestCase
from model_mommy import mommy
from app.company.models import Company

class CompanyTest(TestCase):

  def test_company_str(self):
    company = mommy.make(Company, name='Fake Company') 
    self.assertEqual(str(company), 'Fake Company')
