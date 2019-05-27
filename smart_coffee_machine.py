class SmartCoffeeMachine:
    def __init__(self, cafe_db, menu, processing_service, reporting_service):
        self.cafe_db = cafe_db
        self.menu = menu
        self.processing_service = processing_service
        self.reporting_service = reporting_service
