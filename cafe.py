class Cafe:
    def __init__(self, cafe_db, menu, processing_service, reporting_service):
        self.cafe_db = cafe_db
        self.menu = menu
        self.processing_service = processing_service
        self.reporting_service = reporting_service

    def list_of_names_by_role(self, role_name):
        return self.cafe_db.get_names_by_role(role_name)
