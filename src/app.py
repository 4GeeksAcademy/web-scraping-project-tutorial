import sys
from service.tesla_revenue_service import TeslaRevenueService
from config.database import Database


def main():
    
    """Main function."""

    config = Database()
    config.create_table()

    TeslaRevenueService().get_data_tesla()


if __name__ == "__main__":
    main()
    sys.exit(0)