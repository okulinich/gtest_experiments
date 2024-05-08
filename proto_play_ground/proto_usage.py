import example_pb2

person = example_pb2.Person()
person.name = "John Doe"
person.id = 1234

# Serialize to string
output = person.SerializeToString()
print("Serialized from python:\n", output)

