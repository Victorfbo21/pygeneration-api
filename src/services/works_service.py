from src.repositories.works_repository import WorksRepository
from src.utils.generate_work_code import generate_work_code

class WorksService:

    def __init__(self, db):
        self._worksRepository = WorksRepository(db)


    async def create_work(self, request_data):
        
        try:

            verify_exists = await self._worksRepository.find_work_by_name_and_category(request_data['name'], request_data['category'])

            if verify_exists:
                return {
                    "data" : None,
                    "error": True,
                    "statusCode":400,
                    "message": 'Serviço Já Cadastrado!'
                }

            work_code = generate_work_code()

            request_data['code'] = work_code

            work = await self._worksRepository.create_work(request_data)

            return {
                "data": work,
                "error": False,
                "statusCode": 201,
                "message": 'Serviço Cadastrado com Sucesso!'
            }
        except Exception as e:
            return {
                "data": None,
                "error":True,
                "statusCode": 500,
                "message": str(e)
            }
        

    async def list_works(self, owner : str):
        try:
            works = await self._worksRepository.find_works_by_owner(owner)

            return {
                "data": works,
                "error": False,
                "statusCode": 200,
                "message": 'Serviços Listados com Sucesso!'
            }   

        except Exception as e:
            return {
                "data": None,
                "error":True,
                "statusCode": 500,
                "message": str(e)
            }