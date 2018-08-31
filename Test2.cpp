#include <thread>
#include <SFML/Window.hpp>
#include <iostream>


int main()
{
    sf::Window fenetre;
    fenetre.create(sf::VideoMode(600,400),"Fenetre test");
    
    bool test(true);
    int passage(0);
    while (fenetre.isOpen())
    {
        sf::Event event;
        std::cout<<"passage boucle "<<std::endl;

        while (fenetre.pollEvent(event))
        {
        

        if(event.type == sf::Event::KeyPressed)
        {
            if (event.key.code == sf::Keyboard::Left)
            {
                std::cout << "clavier pressé"<<std::endl;
            }
        }


        if (event.type == sf::Event::Closed)
        {
            fenetre.close();
        }

        }    
    }
    return 0;

}