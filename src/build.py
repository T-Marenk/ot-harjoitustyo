from services.budget_service import budget_service
from initialize_database import initialize_database


def build():
    budget_service.delete_all()
    initialize_database()


if __name__ == '__main__':
    build()
