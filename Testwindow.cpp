#include <iostream>
#include <SFML/Window.hpp>
#include <SFML/System/Vector2.hpp>
#include <SFML/System/Time.hpp>
#include <SFML/System/Clock.hpp>
#include <thread>
#include <unistd.h>

void traitementfennetre(sf::Window *fen, sf::Event *e1)
{

    sf::Clock chrono;
    sf::Time temps;
    int recu;
    bool test(true);
    std::cout <<"threadlaunched"<<std::endl;
    while(fen->isOpen())
    {
        if(((e1->type == sf::Event::MouseLeft)!=test) && (test == false))
        {
            chrono.restart();
            temps = chrono.getElapsedTime();
            recu = temps.asMicroseconds();
            std::cout << recu << std::endl;
            test = true;
        }
        else if(((e1->type == sf::Event::MouseLeft)!=test) && (test == true))
        {
            test = false;
        }
    }
    std::cout<<"thread terminer" <<std::endl;
}

int main()
{
    sf::Window fenetre;
    
    fenetre.create(sf::VideoMode(800, 600), "Mafenetre", sf::Style::Default);
    sf::Event event1;
    std::thread t1(traitementfennetre, &fenetre, &event1);
    sf::Clock chrono;
    sf::Time tempsraffraichissement;
    sf::Time ftd = sf::microseconds(1000000/30);


    while (fenetre.isOpen())
    {
        chrono.restart();
        
        
        while (fenetre.pollEvent(event1))
        {
            if (event1.type == sf::Event ::Closed)
            {
                fenetre.close();
                t1.join();
                
            }
            
        }
        tempsraffraichissement = chrono.getElapsedTime();
        tempsraffraichissement = ftd - tempsraffraichissement;
        if (tempsraffraichissement > sf::Time::Zero)
        {
            sf::sleep(tempsraffraichissement);
        } 
        
    }
    
    return 0;
}