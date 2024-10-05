#1
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#     @abstractmethod
#     def start(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self, brand, model, year, mileage, num_doors):
#         super().__init__(brand, model, year, mileage)
#         self.num_doors = num_doors
#
#     def get_info(self):
#         return f"Car: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage}, Doors: {self.num_doors}"
#
#     def start(self):
#         return "Car is starting."
#
#     def stop(self):
#         return "Car is stopping."
#
#     def open_trunk(self):
#         return "Trunk is open."
#
# class Bicycle(Vehicle):
#     def __init__(self, brand, model, year, mileage, gear_count):
#         super().__init__(brand, model, year, mileage)
#         self.gear_count = gear_count
#
#     def get_info(self):
#         return f"Bicycle: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage}, Gears: {self.gear_count}"
#
#     def start(self):
#         return "Bicycle ride started."
#
#     def stop(self):
#         return "Bicycle ride stopped."
#
#     def ring_bell(self):
#         return "Ring ring!"
#
# car = Car("Toyota", "Corolla", 2020, 15000, 4)
# bicycle = Bicycle("Giant", "Escape 3", 2021, 500, 21)
#
# print(car.get_info())
# print(car.start())
# print(car.open_trunk())
# print(car.stop())
#
# print(bicycle.get_info())
# print(bicycle.start())
# print(bicycle.ring_bell())
# print(bicycle.stop())
#2
# from abc import ABC, abstractmethod
#
# class Kitob(ABC):
#     def __init__(self, nomi, muallif, isbn, sahifa_soni):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.isbn = isbn
#         self.sahifa_soni = sahifa_soni
#         self.joriy_sahifa = 0
#
#     @abstractmethod
#     def malumot_olish(self):
#         pass
#
#     @abstractmethod
#     def sahifa_oqish(self):
#         pass
#
#     @abstractmethod
#     def sahifa_belgilash(self):
#         pass
#
# class ElektronKitob(Kitob):
#     def __init__(self, nomi, muallif, isbn, sahifa_soni, fayl_hajmi):
#         super().__init__(nomi, muallif, isbn, sahifa_soni)
#         self.fayl_hajmi = fayl_hajmi
#
#     def malumot_olish(self):
#         return f"Elektron Kitob: {self.nomi} - {self.muallif}, ISBN: {self.isbn}, Sahifalar: {self.sahifa_soni}, Fayl hajmi: {self.fayl_hajmi}MB"
#
#     def sahifa_oqish(self):
#         if self.joriy_sahifa < self.sahifa_soni:
#             self.joriy_sahifa += 1
#             return f"{self.nomi} kitobining {self.joriy_sahifasi} sahifasini o'qiyapman"
#         else:
#             return "Kitob tugadi"
#
#     def sahifa_belgilash(self):
#         return f"{self.nomi} kitobining {self.joriy_sahifasi} sahifasi belgilandi"
#
#     def yuklab_olish(self):
#         return f"{self.nomi} kitobi yuklanmoqda, Fayl hajmi: {self.fayl_hajmi}MB"
#
# class AudioKitob(Kitob):
#     def __init__(self, nomi, muallif, isbn, sahifa_soni, davomiylik):
#         super().__init__(nomi, muallif, isbn, sahifa_soni)
#         self.davomiylik = davomiylik
#
#     def malumot_olish(self):
#         return f"Audio Kitob: {self.nomi} - {self.muallif}, ISBN: {self.isbn}, Sahifalar: {self.sahifa_soni}, Davomiylik: {self.davomiylik} soat"
#
#     def sahifa_oqish(self):
#         if self.joriy_sahifa < self.sahifa_soni:
#             self.joriy_sahifa += 1
#             return f"{self.nomi} kitobining {self.joriy_sahifasi} sahifasini tinglayapman"
#         else:
#             return "Kitob tugadi"
#
#     def sahifa_belgilash(self):
#         return f"{self.nomi} kitobining {self.joriy_sahifasi} sahifasi belgilandi"
#
#     def tinglash(self):
#         return f"{self.nomi} kitobi tinglanmoqda, Davomiylik: {self.davomiylik} soat"
#
# def test_elektron_kitob():
#     elektron_kitob = ElektronKitob(nomi="Python Dasturlash", muallif="John Doe", isbn="1234567890", sahifa_soni=300, fayl_hajmi=5)
#
#     print(elektron_kitob.malumot_olish())
#
#     print(elektron_kitob.sahifa_oqish())
#     print(elektron_kitob.sahifa_oqish())
#
#     print(elektron_kitob.sahifa_belgilash())
#
#     print(elektron_kitob.yuklab_olish())
#
# def test_audio_kitob():
#     audio_kitob = AudioKitob(nomi="Pythonni O'rganish", muallif="Jane Smith", isbn="0987654321", sahifa_soni=200, davomiylik=10)
#
#     print(audio_kitob.malumot_olish())
#
#     print(audio_kitob.sahifa_oqish())
#     print(audio_kitob.sahifa_oqish())
#
#     print(audio_kitob.sahifa_belgilash())
#
#     print(audio_kitob.tinglash())
#
# test_elektron_kitob()
# test_audio_kitob()
