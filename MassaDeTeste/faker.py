
from faker import Faker

faker = Faker('pt.BR')

persona = {
    'nome'= faker.name(),
    'cidade' = faker.address()
}  

print(persona)