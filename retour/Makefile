CC = g++
RM = rm -f
NAME = test
ALL = *.o
SRCS = testthread.cpp
OBJS = $(SRCS:.c=.o)
LIB = -lsfml-graphics -lsfml-window -lsfml-system 
LIBs = -lpthread -std=c++11 -std=gnu++11 
EXEC = ./test

all:bin exec
	
bin:
	$(CC) -c $(SRCS) $(LIBs)
exec: 
	$(CC) $(ALL) -o $(NAME) $(LIB) $(LIBs)

clean:
	$(RM) $(ALL)

fclean: clean
	$(RM) $(NAME)
re: fclean all

full : re 
	$(EXEC)

.PHONY: all clean fclean re