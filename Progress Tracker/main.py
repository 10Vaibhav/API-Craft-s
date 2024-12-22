import requests
from datetime import datetime


class PixelaTracker:
    def __init__(self):
        self.TOKEN = "" # Put Your Token here
        self.USERNAME = "" # Put Your UserName here
        self.GRAPH_ID = "progresstracker"
        self.base_endpoint = "https://pixe.la/v1/users"
        self.headers = {"X-USER-TOKEN": self.TOKEN}

    def create_user(self):
        user_params = {
            "token": self.TOKEN,
            "username": self.USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        response = requests.post(url=self.base_endpoint, json=user_params)
        return response.text

    def create_graph(self):
        graph_endpoint = f"{self.base_endpoint}/{self.USERNAME}/graphs"
        graph_config = {
            "id": self.GRAPH_ID,
            "name": "Progress Graph",
            "unit": "commit",
            "type": "int",
            "color": "ajisai"
        }
        response = requests.post(url=graph_endpoint, json=graph_config, headers=self.headers)
        return response.text

    def add_pixel(self, date=None, quantity=None):
        pixel_endpoint = f"{self.base_endpoint}/{self.USERNAME}/graphs/{self.GRAPH_ID}"
        if date is None:
            date = datetime.now()
        if quantity is None:
            quantity = input("Enter the quantity for today: ")

        pixel_params = {
            "date": str(date.strftime("%Y%m%d") if isinstance(date, datetime) else date),
            "quantity": quantity,
        }
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=self.headers)
        return response.text

    def update_pixel(self, date=None, quantity=None):
        if date is None:
            date = input("Enter date to update (YYYYMMDD): ")
        if quantity is None:
            quantity = input("Enter new quantity: ")

        update_endpoint = f"{self.base_endpoint}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{date}"
        pixel_params = {"quantity": quantity}
        response = requests.put(url=update_endpoint, json=pixel_params, headers=self.headers)
        return response.text

    def delete_pixel(self, date=None):
        if date is None:
            date = input("Enter date to delete (YYYYMMDD): ")

        delete_endpoint = f"{self.base_endpoint}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{date}"
        response = requests.delete(url=delete_endpoint, headers=self.headers)
        return response.text


def main():
    tracker = PixelaTracker()

    while True:
        print("\nPixela Progress Tracker Menu:")
        print("1. Create New User")
        print("2. Create New Graph")
        print("3. Add Pixel")
        print("4. Update Pixel")
        print("5. Delete Pixel")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ")

        match choice:
            case "1":
                print("Creating new user...")
                print(tracker.create_user())

            case "2":
                print("Creating new graph...")
                print(tracker.create_graph())

            case "3":
                print("Adding new pixel...")
                use_today = input("Use today's date? (y/n): ").lower()
                if use_today == 'y':
                    print(tracker.add_pixel())
                else:
                    date = input("Enter date (YYYYMMDD): ")
                    quantity = input("Enter quantity: ")
                    print(tracker.add_pixel(date, quantity))

            case "4":
                print("Updating pixel...")
                print(tracker.update_pixel())

            case "5":
                print("Deleting pixel...")
                print(tracker.delete_pixel())

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

    