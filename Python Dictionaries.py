# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:10:29 2024

@author: Loren
"""



# 1. Real-World Python Dictionary Applications



# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }

# # Add a new category
# restaurant_menu["Beverages"] = {"Coffee": 2.99, "Tea": 2.50}

# # Update the price
# restaurant_menu["Main Course"]["Steak"] = 17.99

# # Remove 
# del restaurant_menu["Starters"]["Bruschetta"]

# print(restaurant_menu)



# 2. Advanced Data Handling with Python



# hotel_rooms = {
#     "101": {"status": "available", "customer": ""},
#     "102": {"status": "booked", "customer": "John Doe"}
# }

# def book_room(room_number, customer_name):
#     if hotel_rooms[room_number]["status"] == "available":
#         hotel_rooms[room_number]["status"] = "booked"
#         hotel_rooms[room_number]["customer"] = customer_name
#         print(f"Room {room_number} booked successfully for {customer_name}.")
#     else:
#         print(f"Room {room_number} is already booked.")

# def check_out(room_number):
#     if hotel_rooms[room_number]["status"] == "booked":
#         hotel_rooms[room_number]["status"] = "available"
#         customer_name = hotel_rooms[room_number]["customer"]
#         hotel_rooms[room_number]["customer"] = ""
#         print(f"{customer_name} has checked out of room {room_number}.")
#     else:
#         print(f"Room {room_number} is already available.")

# def display_status():
#     for room_number, details in hotel_rooms.items():
#         print(f"Room {room_number}: {details['status']} (Customer: {details['customer']})")

# # Example usage
# display_status()
# book_room("101", "Jane Smith")
# check_out("102")
# display_status()



# 3. Python Programming Challenges 

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# def open_ticket(ticket_id, customer, issue):
#     if ticket_id not in service_tickets:
#         service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
#         print(f"Ticket {ticket_id} opened for {customer}.")
#     else:
#         print(f"Ticket {ticket_id} already exists.")

# def update_ticket_status(ticket_id, status):
#     if ticket_id in service_tickets:
#         service_tickets[ticket_id]["Status"] = status
#         print(f"Ticket {ticket_id} status updated to {status}.")
#     else:
#         print(f"Ticket {ticket_id} does not exist.")

# def display_tickets(status=None):
#     for ticket_id, details in service_tickets.items():
#         if status is None or details["Status"] == status:
#             print(f"{ticket_id}: {details['Customer']} - {details['Issue']} ({details['Status']})")

# # Example usage
# display_tickets()
# open_ticket("Ticket003", "Charlie", "Service outage")
# update_ticket_status("Ticket001", "closed")
# display_tickets("open")



# 4. Python Essentials for Business Analytics




# import copy

# weekly_sales = {
#     "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
#     "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
# }

# # Create a deep copy 
# weekly_sales_copy = copy.deepcopy(weekly_sales)

# # Update the sales 
# weekly_sales_copy["Week 2"]["Electronics"] = 18000

# print("Original Sales Data:")
# print(weekly_sales)

# print("\nModified Sales Data:")
# print(weekly_sales_copy)