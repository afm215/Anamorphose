#include <SFML/System/Clock.hpp>
#include <SFML/System/Time.hpp>
#include <iostream>

int main()
{
    sf::Time premiere = sf::microseconds(1000);
    int test = premiere.asMicroseconds();
    std::cout << test << std::endl;
    


}