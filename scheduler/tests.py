from rest_framework.test import APIClient
from model_mommy import mommy
from django.test import TestCase
from .models import CommunicationScheduling
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def get_payload(self):
        return {
            "message_type": 'sms',
            "scheduling": '2020-12-31T23:59:59-03:00',
            "message": "Feliz Ano Novo!!!",
            "recipient": "cliente@teste.dev"
        }

    def setUp(self):
        user = User.objects.create(username='test-user')
        password = 'test-user-password'
        user.set_password(password)
        user.save()
        self.client = APIClient()
        self.client = APIClient()
        self.client.login(username=user.username, password=password)


class SchedulingCreationTestCase(BaseTest):
    def test_add_scheduling_ok(self):
        """
        Garante que ao enviar todos os parâmetros obrigatórios
        um agendamento é criado
        """
        response = self.client.post(
            '/scheduling/',
            self.get_payload(),
            format='json'
        )
        # validando o status code retornado
        self.assertEqual(response.status_code, 201)

    def test_message_type_validation(self):
        """
        Garante que ao enviar um tipo inválido de mensagem o
        agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload['message_type'] = ['invalid']
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_required_message_validation(self):
        """
        Garante que ao tentar criar um agendamento sem mensagem o
        agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload.pop('message')
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_required_message_type_validation(self):
        """
        Garante que ao tentar criar um agendamento sem o tipo de mensagem o
        agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload.pop('message_type')
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_required_scheduling_validation(self):
        """
        Garante que ao tentar criar um agendamento sem a data de agendamento
        o agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload.pop('scheduling')
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_prevent_past_scheduling_validation(self):
        """
        Garante que ao tentar criar um agendamento com a data passada o
        agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload['scheduling'] = '2019-12-31T23:59:59-03:00'
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_required_recipient_validation(self):
        """
        Garante que ao tentar criar um agendamento sem o destinatário
        agendamento não seja criado e o erro HTTP 400 seja retornado
        """
        payload = self.get_payload()
        payload.pop('recipient')
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_status_readonly(self):
        """
        O status do agendamento não pode ser definido/alterado através da API
        """
        payload = self.get_payload()
        payload['status'] = 'done'
        response = self.client.post(
            '/scheduling/',
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json()['status'], CommunicationScheduling.STATUS.waiting
        )


class SchedulingGetStatusTestCase(BaseTest):
    def test_get_scheduling_status_ok(self):
        """
        Garante que ao passar o id de um agendamento existente seja possível
        consultar seu status
        """
        instance = mommy.make(CommunicationScheduling)
        response = self.client.get(
            f'/scheduling/{instance.id}/',
        )
        # validando o status code retornado
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], instance.status)

    def test_get_scheduling_status_404(self):
        """
        Garante que ao passar o id de um agendamento não existente
        seja retoranado o status HTTP 404
        """
        response = self.client.get(
            '/scheduling/invalid-id/',
        )
        # validando o status code retornado
        self.assertEqual(response.status_code, 404)


class AuthenticationTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.client.logout()

    def test_login_required_creation(self):
        """
        Garante que para conseguir acessar os dados da API o cliente precisa
        estar autenticado
        """
        response = self.client.post(
            '/scheduling/',
            self.get_payload(),
            format='json'
        )
        # validando o status code retornado
        self.assertEqual(response.status_code, 403)

    def test_login_required_list(self):
        """
        Garante que para conseguir acessar os dados da API o cliente precisa
        estar autenticado
        """
        response = self.client.get(
            '/scheduling/'
        )
        # validando o status code retornado
        self.assertEqual(response.status_code, 403)

    def login_required_detail(self):
        instance = mommy.make(CommunicationScheduling)
        response = self.client.get(
            f'/scheduling/{instance.id}'
        )
        self.assertEqual(response.status_code, 403)

    def login_required_detail(self):
        instance = mommy.make(CommunicationScheduling)
        response = self.client.delete(
            f'/scheduling/{instance.id}'
        )
        self.assertEqual(response.status_code, 403)
