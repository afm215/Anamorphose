#include <iostream>
#include <thread>
#include <SFML/Window.hpp>

int main()
{
    sf::Window window(sf::VideoMode(800,600) ,"my window");
    while (window.isOpen())
    {
        sf::Event event;
        
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Resized)
            {
                window.setSize(sf::Vector2u(640,700));
            }
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }
    }
    return 0;

}
