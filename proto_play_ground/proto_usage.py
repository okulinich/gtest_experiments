import example_pb2
from google.protobuf.descriptor import FieldDescriptor

cpp_type_to_string = {
    FieldDescriptor.CPPTYPE_BOOL: "bool",
    FieldDescriptor.CPPTYPE_DOUBLE: "double",
    FieldDescriptor.CPPTYPE_ENUM: "enum",
    FieldDescriptor.CPPTYPE_FLOAT: "float",
    FieldDescriptor.CPPTYPE_INT32: "int32_t",
    FieldDescriptor.CPPTYPE_INT64: "int64_t",
    FieldDescriptor.CPPTYPE_MESSAGE: "{{}}",
    FieldDescriptor.CPPTYPE_STRING: "string",
    FieldDescriptor.CPPTYPE_UINT32: "uint32_t",
    FieldDescriptor.CPPTYPE_UINT64: "uint64_t",
}

def print_message(message, indent=0):
    indent_space = ' ' * indent
    descriptor = message.DESCRIPTOR

    for field in descriptor.fields:
        value = getattr(message, field.name)
        if field.type == FieldDescriptor.TYPE_MESSAGE:
            # For nested messages, recursively call the function
            if field.label == FieldDescriptor.LABEL_REPEATED:
                print(f"{indent_space}{field.name}: [{{")
                # Create a temporary message object to get the structure
                temp_msg = getattr(message, field.name).add()
                print_message(temp_msg, indent + 2)
                # Remove the temporary object after printing the structure
                getattr(message, field.name).pop()
                print("}]")
            else:
                print(f"{indent_space}{field.name}: {{")
                print_message(value, indent + 2)
                print(f"{indent_space}}}")
        elif field.label == FieldDescriptor.LABEL_REPEATED:
            print(f"{indent_space}{field.name}: [{cpp_type_to_string[field.cpp_type]}]")
        else:
            # For scalar fields, just print the value
            cpp_type_str = cpp_type_to_string[field.cpp_type]
            print(f"{indent_space}{field.name}: {cpp_type_str}")

message_empty = example_pb2.Person()
print_message(message_empty)
