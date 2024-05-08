#include <gtest/gtest.h>

#include <string>
#include <map>
#include <iostream>

class TestableClass
{
public:
    void printSmth(const std::string& smth)
    {
        std::cout << smth << std::endl;
    }
};

class StringTest : public testing::TestWithParam<
    std::pair<std::string, std::string>>
{
protected:
    TestableClass m_testable;
};

INSTANTIATE_TEST_SUITE_P(Default, StringTest, testing::Values(
    std::pair<std::string, std::string>{"Hello", "Goodbye"},
    std::pair<std::string, std::string>{"Test1", "Test2"}
));

TEST_P(StringTest, NonEmpty)
{
    auto const& str_pair = GetParam();
    m_testable.printSmth(str_pair.first);
    m_testable.printSmth(str_pair.second);
    EXPECT_FALSE(str_pair.first.empty());
    std::cout << "Done" << std::endl;
}

int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
