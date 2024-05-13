from src.services.works_service import WorksService

class WorksController:

    def __init__(self, db):
        self.worksService = WorksService(db)


    async def create_work(self, request_data):
        try:
            create_work = await self.worksService.create_work(request_data)

            return create_work
        except Exception as e:
            print(e)


    async def list_works(self):
        try:
            list_works = await self.worksService.list_works() 
            
            return list_works
        
        except Exception as e:
            print(e)