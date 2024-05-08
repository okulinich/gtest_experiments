*How to run:*
`clang++ -lgtest -lgtest_main -pthread -std=c++14 gtest_sample.cpp`
`./a.out`

*How to compile protobuf file:*
- For C++:
`protoc -I=. --cpp_out=. example.proto`
- For Python:
`protoc -I=. --python_out=. example.proto`

*How to run protobuf example:*
- For Python:
`source venv_proto/bin/activate`
`python proto_usage.py`
`deactivate`
