from src.models.service import Service

class WorksRepository :

    def __init__(self, db):
        self.db = db


    async def create_work(self, create_work_data : Service):
        try:
            
            work = await self.db.works.insert_one(create_work_data)
            print(work)
            return work.inserted_id
        except Exception as e:
            print(e)

    async def find_work_by_name_and_category(self, name, category):
        try:
            work =  self.db.works.find_one({'name': name, 'category': category})
            print(work)
            return work
        except Exception as e:
            print(e)

    async def find_works_by_owner(self, owner):
        try:
            works =  self.db.works.find({'owner': owner})
            print(works)
            return works
        except Exception as e:
            print(e)