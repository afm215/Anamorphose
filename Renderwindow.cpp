#include <thread>
#include <SFML/Graphics.hpp>
#include <iostream>
void changevalue(bool *value)
{
    if (*value)
    {
        *value = false;
    }
    else
    {
        *value = true;
    }
}

 
 
 
    sf::Sprite *createsprite(sf::Texture *texture)
{
    sf::Sprite *monsprite = new sf::Sprite;
    monsprite->setTexture(*texture);
    return monsprite;
}


int main()
{
    sf::RenderWindow mafenetre;
    mafenetre.create(sf::VideoMode(800,600),"mafenetre");
    sf::Event event;
    bool check(false);


    sf::Texture texture;
    if(texture.loadFromFile("/home/alexandre/Téléchargements/texture.jpg"))
    {
        std::cout <<"good"<<std::endl;
    }
    texture.setSmooth(true);
    texture.setRepeated(false);
    sf::Sprite sprite;
    sf::Sprite *spritesec = NULL;


    while(mafenetre.isOpen())
    {
        
        
        while(mafenetre.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                mafenetre.close();
            }
            if (event.type == sf::Event::KeyPressed)
            {
                if (event.key.code == sf::Keyboard::Space)
                {
                    changevalue(&check);
                }
            }
            
        }
        if(check)
            {
            
                mafenetre.clear();
                spritesec = createsprite(&texture);
                mafenetre.draw(*spritesec);
                
                std::cout << "espace pressé"<<std::endl;
            } 
        else
        {
            mafenetre.clear();
        }    

        
        sprite.setTextureRect(sf::IntRect(0,0, 800,600));;
        sprite.setRotation(90.f);
        //sprite.scale(sf::Vector2f(4.f,4.f));
        
        
        mafenetre.display();
    }

    delete spritesec;
    spritesec = NULL;
    return 0;
}