import resend
import os
from jinja2 import Template
from src.utils.generate_code  import generate_random_code

class ResendSendEmailService:


    async def send_email(self, send_email_data):
        try:

            print(send_email_data)
            resend.api_key = os.getenv('RESEND_API_KEY')
            to = send_email_data['to']
            with open("src/templates/recovery_password.html","r", encoding="utf-8") as file:
                template_content = file.read()

            template = Template(template_content)    

            params : resend.Emails.SendParams = {
                "sender" : os.getenv('EMAIL_FROM_ADDRESS'),
                "to" : to,
                "subject": 'Recuperação de Senha',
                'html': template.render(code = generate_random_code())
            }

            email = resend.Emails.send(params)

            print(email)
            
            return "E-mail enviado com sucesso!"

        
        except Exception as e:
            print(f"Erro ao enviar e-mail:", e)
            return e