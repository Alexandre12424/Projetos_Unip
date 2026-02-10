#include <stdio.h>
int main()
{
  int a = 20;
  int b = 5;
  int *ptr = &a; // ptr aponta para o endereço de 'a'

  *ptr = *ptr + b; // Modifica o valor para onde 'ptr' aponta
  ptr = &b;        // 'ptr' agora aponta para o endereço de 'b'
  *ptr = *ptr * 2; // Modifica o valor para onde 'ptr' aponta

  printf("%d, %d", a, b);
  return 0;
}
