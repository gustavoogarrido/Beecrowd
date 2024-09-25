#include <stdio.h>
#include <string.h>
 
int main()
{
    char frase[1000];
    int teste;
    scanf("%d", &teste);
    for(int i = 0; i < teste; i++)
    {
        int inv, aux;
        scanf(" %[^\n]", frase);
        int tam = strlen(frase);
        for(long int j = 0; j < tam; j++)
        {
            if((frase[j] >= 'A' && frase[j] <= 'Z') || (frase[j] >= 'a' && frase[j] <= 'z'))
            {
                frase[j] += 3;
            }
        }
        for(int j = 0; j < tam/2; j++)
        {
            inv = tam - 1 - j, aux = frase[j];
            frase[j] = frase[inv];
            frase[inv] = aux;
        }
        for(int k = tam/2; k < tam; k++)
        {
            frase[k] -= 1;
        }
        printf("%s\n", frase);
    }
}