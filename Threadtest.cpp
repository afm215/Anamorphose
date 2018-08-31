#include <iostream>
#include <SFML/System.hpp>
void testfocntion()
{
    for(int i = 0; i<16; i++)
    {
        std::cout << "coucou thread 1"<< std::endl;
    }
}


int main()
{
    sf::Thread thread1(&testfocntion);
    thread1.launch();
    for(int i = 0; i< 16; i++)
    {
        std::cout<<"fonction main "<< i <<std::endl;
    }
    return 0;
}