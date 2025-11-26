#include <stdio.h>

int main(){

    float sum_one = 0;
    int sum_two = 0;
    char ausg[12];
    char hoch[12] = "höher";
    char wen[12] = "niedriger";
    float result = 1.0;

    float my_array[] = {18.3, 17.2, 11.9, 5.5, 3.9, 1.5, 6.6, 7.5, 10, 14.9, 16.8, 18.9, 20, 15.3, 11, 5.1, 2.8, 2, 1.4, 6.1, 10.5, 12.7, 18.5, 18.4, 18.1, 14.5};
    int len_array = sizeof(my_array)/sizeof(my_array[0]);
    // 1
    // berechnen wir die Mittlere temperatur von 12 Monaten erstmal von 23-24
    for (int i = 1; i < 13; i++ ){
      sum_one += my_array[i] ; 
    }
    float mittel_one = sum_one / 12;
    printf("Die Mittlere Temperatur der zwölf Monate (09/23-08/24) ist : %.2f°C\n", mittel_one);

    for (int p = 1; p < 13; p++ ){

        if (0 > ( mittel_one - my_array[p])){
            strcpy(ausg, hoch);
            result = (mittel_one - my_array[p]) * -1;
        }else{
            strcpy(ausg, wen);
            result = mittel_one - my_array[p];
        }
        printf("Im monat n°%d waren Die Temperatur um ca. %f°C %s als dem Mittelwert\n", p, result, ausg);
    }
    // für die °t von 24-25
  for (int i = 13; i < 25; i++ ){
      sum_two += my_array[i] ; 
    }
    float mittel_two = sum_two / 12;
    printf("Die Mittlere Temperatur der zwölf Monate (09/23-08/24) ist : %.2f°C\n", mittel_two);

    for (int p = 13; p < 25 ; p++ ){

        if (0 > ( mittel_two - my_array[p])){
            strcpy(ausg, hoch);
            result = (mittel_two - my_array[p]) * -1;
        }else{
            strcpy(ausg, wen);
            result = mittel_two - my_array[p];
        }
        printf("Im monat n°%d waren Die Temperatur um ca. %f°C %s als dem Mittelwert\n", p, result, ausg);
    }
    // 2 ist nur eine wiederholung kein spaß

    // 3 
    for (int i = 5, p = 17, n = 1; i < 14 && p < 26 && n < 10; i++, p++, n++){
        printf("Im Monat n°%d: %.2f°C - %.2f = %.2f\n", n, my_array[i], my_array[p], my_array[i] - my_array[p]);
    }
  
    return 0;

}