#include <iostream>

using namespace std;

int main()
{
    int PEDROS_AMOUNT_NUMBERS;
    int DIVISOR;
    
    int counter = 0;
    int numbers_divisibles = 0;
    
    cin>>PEDROS_AMOUNT_NUMBERS;
    cin>>DIVISOR;
    
    while (counter < PEDROS_AMOUNT_NUMBERS)
    {
        counter++;
        int NUMBER_TO_DIVIDED;
        cin>>NUMBER_TO_DIVIDED;
        bool IS_DIVISBLE = NUMBER_TO_DIVIDED % DIVISOR == 0;
        if (IS_DIVISBLE)
        {
            numbers_divisibles++;
        }
    }

    cout<<numbers_divisibles;
    return 0;
}
