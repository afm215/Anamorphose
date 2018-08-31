#include <SFML/System/Time.hpp>
#include <SFML/System/Clock.hpp>
#include <iostream>
int main()
{
    sf::Time t1 = sf::milliseconds(5);
    //mesurer temps
    sf::Clock chrono;
    sf::Time t2 = sf::seconds(1.0f);
    int test1 = t2.asMilliseconds();
    sf::Int64 test = test1;
    std::cout << test << std::endl;
    sf::Time retour = chrono.getElapsedTime();
    int ret = retour.asMicroseconds();
    chrono.restart();
    std::cout <<ret<<std::endl;
    sf::Time retour2 = chrono.restart();
    ret = retour2.asMicroseconds();
    std::cout<<ret<<std::endl;
    

return 0;
}