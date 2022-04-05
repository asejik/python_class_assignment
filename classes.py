# class User():
#     first_name = ''
#     last_name = ''
#     user_type = ''
#     phone_number = ''
#     email_adress = ''
    
#     def get_full_name(self):
#         return "{}, {}".format(self.first_name, self.last_name)
    
# class MealItem():
#     name = ''
#     description = ''
#     serving_size = ''
#     allergens = ''
    
# class Order():
#     pass

# class Price():
#     pass


# # initiating a class
# user = User()
# user.first_name = 'Ini'
# user.last_name = 'Arthur'
# user.phone_number = '09033664489'
# user.email_adress = 'asejik@gmail.com'

# print("My name is {} and we are Fuudia".format(user.get_full_name()))

# ASSIGNMENT

class meal:
    name = ""
    ingredients = ""
    imageUrl = ""
    Id = ""


class order:
    userName = ""
    userType = ""
    mealId = ""
    orderId = ""
    extraPortion = False
    toBePacked = False


class eitOrder(order):
    toBeDelivered = False
    deliveryLocation = ""
    hasInformedTrainingDirector = False


class nonEitOrder(order):
    toBeDeliveredToOffice = False
    willBeLate = False


class menu(meal):
    breakfastId = ""
    lunchId = ""
    dinnerId = ""


class user:
    userType = ""
    userId = ""
    firstName = ""
    lastName = ""
    emailAddress = ""
    phoneNumber = ""
    allergies = ""
    foodDiet = ""
    isActive = ""