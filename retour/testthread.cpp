#include <SFML/System/Clock.hpp>
#include <SFML/System/Time.hpp>
#include <SFML/System/Thread.hpp>
#include <iostream>
#include <thread>
#include <SFML/System/Mutex.hpp>

void affiche(int *nombrethread, sf::Mutex *m)
{
    m->lock();
    for (int i = 0; i <= 10; i++)
    {
        std::cout <<"thread"<< *nombrethread <<std::endl;;
    }
    m->unlock();
}

int main()
{   
    sf::Mutex m1;
    int nbr(1);
    int nbr2(2);
    int *nbr3 = new int(5);
    std::thread t1(affiche,&nbr, &m1 );
    std::thread t2 (affiche,&nbr2,&m1);
    //std::thread t3(affiche,3);//
    
    for (int i = 0; i <= 10; i++)
    {
        std::cout <<"thread principal"<<std::endl;;
    }

    sf::Time premiere = sf::microseconds(1000);
    int test = premiere.asMicroseconds();
    std::cout << test << std::endl;
    

//t3.join();//
t1.join();
t2.join();
return 0;
}